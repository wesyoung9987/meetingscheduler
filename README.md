# Meeting Scheduler

A Python library for scheduling team meetings.

## Installation

```
$ pip install meeting_scheduler
```

## Usage

```python
from meeting_scheduler import scheduler

# example inputs
people = [
  {
    "name": "Kyle",
    "meetingTimes": [
      "13:30:00",
      "14:30:00",
      "18:00:00"
    ]
  },
  {
    "name": "Paul",
    "meetingTimes": [
      "07:00:00",
      "09:00:00",
      "13:30:00",
      "15:00:00",
      "15:30:00"
    ]
  },
  {
    "name": "Alex",
    "meetingTimes": [
      "08:00:00",
      "09:30:00",
      "12:30:00",
      "15:00:00"
    ]
  },
  {
    "name": "Luis",
    "meetingTimes": [
      "09:00:00",
      "13:30:00",
      "15:00:00",
      "15:30:00"
    ]
  },
  {
    "name": "Jairo",
    "meetingTimes": [
      "08:00:00",
      "09:00:00",
      "18:00:00"
    ]
  },
  {
    "name": "Sonya",
    "meetingTimes": [
      "08:00:00",
      "12:30:00",
      "13:30:00",
      "15:30:00"
    ]
  }
]

office_hours = {
  "startTime": "08:00:00",
  "endTime": "17:00:00"
}

lunch_hours = {
  "startTime": "12:00:00",
  "endTime": "13:00:00"
}

availability = scheduler.find_availability(people, office_hours, lunch_hours)

print(availability)
# prints
# {
#   "08:00:00": [
#     "Kyle",
#     "Paul",
#     "Luis"
#   ],
#   "08:30:00": [
#     "Kyle",
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "09:00:00": [
#     "Kyle",
#     "Alex",
#     "Sonya"
#   ],
#   "09:30:00": [
#     "Kyle",
#     "Paul",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "10:00:00": [
#     "Kyle",
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "10:30:00": [
#     "Kyle",
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "11:00:00": [
#     "Kyle",
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "11:30:00": [
#     "Kyle",
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "13:00:00": [
#     "Kyle",
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "14:00:00": [
#     "Kyle",
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "14:30:00": [
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "15:30:00": [
#     "Kyle",
#     "Alex",
#     "Jairo"
#   ],
#   "15:00:00": [
#     "Kyle",
#     "Jairo",
#     "Sonya"
#   ],
#   "16:00:00": [
#     "Kyle",
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ],
#   "16:30:00": [
#     "Kyle",
#     "Paul",
#     "Alex",
#     "Luis",
#     "Jairo",
#     "Sonya"
#   ]
# }
```

## Testing locally

Clone the repository:

```
$ git clone https://github.com/wesyoung9987/meetingscheduler.git
```

Run the tests from inside the project:

```
$ cd meetingscheduler
$ python -m unittest discover
```
