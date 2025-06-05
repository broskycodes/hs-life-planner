# TO-DO Fix the schedule ordering

import schedule
import time
from item import Item

# Describes the daily schedule for a person


class DailySchedule():
    def __init__(self, start=0, end=24):
        self.start = start  # Start of the day
        self.end = end  # End of the day (bedtime)
        self.current_event = None  # Sets current event to none
        self.daily_schedule = {}  # Dictionary containing events, assignments, and other items

    # Getters and setters for the instance variables
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

    @property
    def daily_schedule(self):
        return self._daily_schedule

    @daily_schedule.setter
    def daily_schedule(self, daily_schedule):
        self._daily_schedule = daily_schedule

    # Adds given events to daily schedule
    # Assumes that events and times are correspondant
    def add_events(self, events, times):
        # Updates current event when time is reached, and adds event to schedule
        for i in range(len(events)):
            def update_current_event(self, event):
                self.current_event = event
            # Add feature to check if event is already occuring? Then provide a warning?
            schedule.every().day.at(times[i]).do(
                update_current_event(self, events[i]))
        # Updates daily schedule with events
        self.daily_schedule = time_order_update(self.daily_schedule, events)

# Describes the weekly schedule for a person


class WeeklySchedule():
    def __init__(self):
        self.list_of_daily_schedules = {"Monday": DailySchedule(),
                                        "Tuesday": DailySchedule(),
                                        "Wednesday": DailySchedule(),
                                        "Thursday": DailySchedule(),
                                        "Friday": DailySchedule(),
                                        "Saturday": DailySchedule(),
                                        "Sunday": DailySchedule()}  # List of days and their schedukes within the week

    @property
    def list_of_daily_schedules(self):
        return self.list_of_daily_schedules

    @list_of_daily_schedules.setter
    def list_of_daily_schedules(self, list_of_daily_schedules):
        self.list_of_daily_schedules = list_of_daily_schedules

    # Adds events to specific days' calendars
    def add_events(self, days, events, times):
        for day in days:
            self.list_of_daily_schedules[day].add_event(events, times)
    # Updates a daily calendar

    def update_daily_calendar(self, day, daily_calendar):
        self.list_of_daily_schedules[day] = daily_calendar

# Updates and sorts a given schedule with each item if each item has a fixed time


def time_order_update(schedule, items):
    for item in items:
        # If item doesn't have a time to sort, then move to next item
        if item.output_time_in_seconds() == -1:
            continue
        schedule.update({item.daily_title_display(): item})
    return {k: v for k, v in sorted(
            schedule.values(), key=lambda item: item.output_time_in_seconds())}
