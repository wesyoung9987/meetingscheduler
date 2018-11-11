import unittest
import json

from meeting_scheduler import scheduler as s


class TestMeetingScheduler(unittest.TestCase):
    """Tests for Meeting Scheduler."""

    def test_find_availability(self):
        """Should return correct output"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)

        with open('tests/testoutput.json') as f:
            test_output = json.load(f)

        result = s.find_availability(
            test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertEquals(test_output, result)

    def test_find_availability_lunch(self):
        """Should be able to handle different lunch times"""

        with open('tests/testlunchinput.json') as f:
            test_input = json.load(f)

        with open('tests/testlunchoutput.json') as f:
            test_output = json.load(f)

        result = s.find_availability(
            test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertEquals(test_output, result)

    def test_find_availability_long_lunch(self):
        """Should be able to handle longer lunch"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['lunch']['endTime'] = '14:00:00'

        with open('tests/testlonglunchoutput.json') as f:
            test_output = json.load(f)

        result = s.find_availability(
            test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertEquals(test_output, result)

    def test_find_availability_work_hours(self):
        """Should be able to handle different work hours"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['officeHours']['startTime'] = '09:00:00'
            test_input['officeHours']['endTime'] = '18:00:00'

        with open('tests/testworkhoursoutput.json') as f:
            test_output = json.load(f)

        result = s.find_availability(
            test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertEquals(test_output, result)

    def test_find_availability_long_work_hours(self):
        """Should be able to handle longer work hours"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['officeHours']['endTime'] = '18:00:00'

        with open('tests/testlongworkoutput.json') as f:
            test_output = json.load(f)

        result = s.find_availability(
            test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertEquals(test_output, result)

    def test_find_availability_lunch_error(self):
        """Should raise an exception if lunch times are not specified"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['lunch'] = {}

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue('Lunch times are required' in context.exception)

    def test_find_availability_lunch_start_error(self):
        """Should raise an exception if only one lunch time is specified"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['lunch'] = {
                'endTime': '13:00:00'
            }

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue('Lunch times are required' in context.exception)

    def test_find_availability_hours_error(self):
        """Should raise an exception if office hours are not specified"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['officeHours'] = {}

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue('Office hours are required' in context.exception)

    def test_find_availability_hours_start_error(self):
        """Should raise an exception if only one office hour is specified"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['officeHours'] = {
                'endTime': '13:00:00'
            }

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue('Office hours are required' in context.exception)

    def test_find_availability_people_type(self):
        """Should raise an exception if people is not a list"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['people'] = {}

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue('Please provide a list of people' in context.exception)

    def test_find_availability_people_empty(self):
        """Should raise an exception if people is empty"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['people'] = []

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue('Please provide a list of people' in context.exception)

    def test_find_availability_people_no_name(self):
        """Should raise an exception if a person does not have a name"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['people'][0] = {
                'meetingTimes': [
                    '13:30:00',
                    '14:30:00',
                    '18:00:00'
                ]
            }

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue(
            'Please provide a name for each person' in context.exception)

    def test_find_availability_people_no_meetings(self):
        """Should raise an exception if a person does not have a name"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['people'][0] = {
                'name': 'Dave'
            }

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue(
            'Please provide a list of meeting times for each person' in context.exception)

    def test_find_availability_invalid_time(self):
        """Should raise an exception if any of the input times are not formatted correctly"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['officeHours'] = {
                'startTime': '08:00:00',
                'endTime': '17'
            }

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue(
            'Times must be formatted as hh:mm:ss' in context.exception)

    def test_find_availability_lunch_end_before_start(self):
        """Should raise an exception if lunch end time is before start time"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['lunch'] = {
                'startTime': '13:00:00',
                'endTime': '12:00:00'
            }

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue(
            'Lunch end time must be later than start time' in context.exception)

    def test_find_availability_hours_end_before_start(self):
        """Should raise an exception if office hours end time is before start time"""

        with open('tests/testinput.json') as f:
            test_input = json.load(f)
            test_input['officeHours'] = {
                'startTime': '12:00:00',
                'endTime': '08:00:00'
            }

        with self.assertRaises(Exception) as context:
            s.find_availability(
                test_input['people'], test_input['officeHours'], test_input['lunch'])

        self.assertTrue(
            'Office hours end time must be later than start time' in context.exception)


if __name__ == '__main__':
    unittest.main()
