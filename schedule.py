# TO-DO Fix the schedule ordering

import schedule
import time
from item import Item


class DailySchedule():
    def __init__(self, start, end):
        self.start = start  # Start of the day
        self.end = end  # End of the day (bedtime)
        self.current_event = None  # Sets current event to none
        self.daily_schedule = {}  # Dictionary containing events, assignments, and other items

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self._end

    @current_event.setter
    def end(self, end):
        self._end = end

    @property
    def current_event(self):
        return self._current_event

    @current_event.setter
    def current_event(self, current_event):
        self._current_event = current_event

    def add_event(self, event, time):
        # Updates current event when time is reached
        def update_current_event(self, event):
            self.current_event = event
        # Add feature to check if event is already occuring? Then provide a warning?
        schedule.every().day.at(time).do(update_current_event(self, event))

# Updates a given schedule with a specific item given a fixed time


def time_order_update(schedule, items):
    for item in items:
        # If item doesn't have a time to sort, then move to next item
        if item.output_time_in_seconds() == -1:
            continue
        schedule.update({item.name: item})
        {k: v for k, v in sorted(
            schedule.items(), key=lambda item: item.output_time_in_seconds())}
