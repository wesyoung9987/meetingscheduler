from datetime import datetime, timedelta

def find_availability(people, office_hours, lunch):
    """Takes people, office hours and lunch times formatted as
    people -> [
      {
        'name': 'Dave',
        'meetingTimes': [
          '08:00:00',
          '15:30:00'
        ]
      },
      ...
    ]
    office_hours -> {
      'startTime': '08:00:00',
      'endTime': '17:00:00'
    }
    lunch -> {
      'startTime': '12:00:00',
      'endTime': '13:00:00'
    }

    and returns times when at least three people are available
    and who those people are formatted as
    output -> {
      '11:00:00': [
        'Dave',
        'Jim',
        ...
      ],
      ...
    }
    """

    # Check if inputs are valid
    if ('startTime' not in lunch) or ('endTime' not in lunch):
        raise Exception('Lunch times are required')

    if ('startTime' not in office_hours) or ('endTime' not in office_hours):
        raise Exception('Office hours are required')

    if (type(people) is not list) or (len(people) == 0):
        raise Exception('Please provide a list of people')

    lunch_start = datetime.strptime(lunch['startTime'], '%H:%M:%S')
    lunch_end = datetime.strptime(lunch['endTime'], '%H:%M:%S')

    if lunch_start > lunch_end:
        raise Exception('Lunch end time must be later than start time')

    # Create a store for all times and people available at those times
    schedule = {}
    for person in people:
        _individual_availability(person, office_hours, lunch_start, lunch_end, schedule)

    # Filter out any times that do not have at least three available people
    return {key: value for (key, value) in schedule.items() if len(value) > 2}


def _check_lunch_hours(time, lunch_start, lunch_end):
    """Checks if the time is during lunch"""
    return (time < lunch_start) or (time >= lunch_end)


def _individual_availability(person, office_hours, lunch_start, lunch_end, schedule):
    """Checks the availability of each person and adds them to the schedule"""

    # Check if inputs are valid
    if ('name' not in person):
        raise Exception('Please provide a name for each person')

    if ('meetingTimes' not in person):
        raise Exception('Please provide a list of meeting times for each person')

    time = datetime.strptime(office_hours['startTime'], '%H:%M:%S')
    office_end = datetime.strptime(office_hours['endTime'], '%H:%M:%S')

    if time > office_end:
        raise Exception('Office hours end time must be later than start time')

    # Go through the office hours and check against the persons schedule
    while time < office_end:
        time_key = time.strftime('%H:%M:%S')

        # check if the person has a meeting during this time or if it is during lunch hours
        if time_key not in person['meetingTimes'] and _check_lunch_hours(time, lunch_start, lunch_end):
            # Check if the time exists in the schedule and add persons name
            if time_key in schedule:
                schedule[time_key].append(person['name'])
            else:
                schedule[time_key] = [person['name']]

        time = time + timedelta(minutes=30)
