import schedule
import time


class DailySchedule():
    def __init__(self, start, end):
        self.start = start  # Start of the day
        self.end = end  # End of the day (bedtime)
        self.current_event = None  # Sets current event to none

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
        def update_current_event(self, event):
            self.current_event = event
        # Add feature to check if event is already occuring? Then provide a warning?
        schedule.every().day.at(time).do(update_current_event(self, event))

    def display_current_event(self):
        print(self.current_event)
