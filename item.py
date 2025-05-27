# Defines any specific task or event, holding at least a name and an association
class Item:
    def __init__(self, name, association, current_status, description=""):
        self.name = name  # Name of event
        # Item the event is associated with (course, EC, NA)
        self.association = association
        # Current status of the item (Upcoming, Completed, Late, etc)
        self.current_status = current_status
        self.description = description  # A description of the item, blank if not specified

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def association(self):
        return self._association

    @association.setter
    def association(self, association):
        self._association = association

    @property
    def current_status(self):
        return self._current_status

    @current_status.setter
    def current_status(self, current_status):
        self._current_status = current_status

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._current_status = description

    def display(self):
        return {"Name": self.name, "Association": self.association, "Current Status": self.current_status, "Description": self.description}

    def output_time_in_seconds(self):
        return -1

    def title_display(self):
        return self.name

# Defines an event with a specific timeframe (anything scheduled)


class Event(Item):
    def __init__(self, name, association, start, end, is_repeated, current_status, description=""):
        super.__init__(self, name, association, current_status, description)
        self.start = start  # Start time of event
        self.end = end  # End time of event
        self.is_repeated = is_repeated  # Boolean containing if the event is repeated

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time

    @property
    def is_repeated(self):
        return self._is_repeated

    @is_repeated.setter
    def start(self, is_repeated):
        self._is_repeated = is_repeated

    def display(self):
        return super().display().update({"Time": self.time, "Is repeated": self.is_repeated})

    def change_start(self, start):
        self.time[0] = start

    def change_end(self, end):
        self.time[1] = end

    def output_time_in_seconds(self):
        return self.start.timestamp()

    # Displays daily time or full time as formatted string
    def display_daily_time(self):
        title_start_time = format_datetime(self.time[0], False, True)
        title_end_time = format_datetime(self.time[1], False, True)
        return f"{title_start_time} - {title_end_time}: {self.name}"

    def display_full_time(self):
        title_start_datetime = format_datetime(self.time[0], True, True)
        title_end_datetime = format_datetime(self.time[1], True, True)
        return f"{title_start_datetime} - {title_end_datetime}: {self.name}"

# Broad category of any task to be completed


class Assignment(Item):
    def __init__(self, name, association, due_date, current_status, description=""):
        super.__init__(self, name, association, current_status, description)
        self.due_date = due_date

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    def display(self):
        return super().display().update({"Due Date": self.due_date})

    def output_time_in_seconds(self):
        return self.due_date.timestamp()

    def daily_title_display(self):
        return self.name


class GradedAssignment(Assignment):
    def __init__(self, name, association, due_date, current_status, points, grade_affect):
        super.__init__(self, name, association, due_date, current_status)
        self.points = points  # Points the assignment is worth
        # Percentage the assignment will affect your grade (work in progress)
        self.grade_affect = grade_affect

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        self._points = points

    @property
    def grade_affect(self):
        return self._grade_affect

    @grade_affect.setter
    def grade_affect(self, grade_affect):
        self._grade_affect = grade_affect

    def display(self):
        return super().display().update({"Grade Effect %": self.due_date})

# Defines how to turn a datetime object into a displayable date and/or time


def format_datetime(datetime, use_date=False, use_time=True):
    current_datetime = datetime.now()
    title_datetime = ""
    if use_date:
        title_date = current_datetime.strftime("%b %d, %Y")
        title_datetime += title_date
    if use_time:
        title_datetime += " "
        title_time = current_datetime.strftime("%H:%M")
        title_datetime += title_time
    return title_datetime
