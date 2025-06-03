class Association:

    def __init__(self, item_type, type_importance, name, importance, location, reg_schedule) -> None:
        self.item_type = item_type  # Type of item (Ex. Academic, EC, Social)
        # Importance of type (Ex. Academic > Social), user defined (0-10)
        self.type_importance = type_importance
        self.name = name  # Name of item
        # Importance of item itself, user defined (0-10)
        self.importance = importance
        self.location = location  # Location of item (Ex. Room no., address)
        # Dictionary of dates and respective DailySchedules
        self.reg_schedule = reg_schedule

    # Getters and setters for each attribute

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        self._item_type = item_type

    @property
    def type_importance(self):
        return self._type_importance

    @type_importance.setter
    def type_importance(self, type_importance):
        self._type_importance = type_importance

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def importance(self):
        return self._importance

    @importance.setter
    def importance(self, importance):
        self._importance = importance

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def reg_schedule(self):
        return self._reg_schedule

    @reg_schedule.setter
    def reg_schedule(self, reg_schedule):
        self._reg_schedule = reg_schedule


class Course(Association):
    item_type = "Course"
    type_importance = 5

    def __init__(self, name, importance, grade, room_n, reg_schedule, special_schedules, weight=4.0, assignment_list=[]):
        super._init_(self, "Course", 5, name, importance, room_n, reg_schedule)
        self.grade = grade
        self.weight = weight
        self.assignment_list = assignment_list
        self.special_schedules = special_schedules

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def assignement_list(self):
        return self._assignment_list

    @assignment_list.setter
    def assignment_list(self, assignment_list):
        self._assignment_list = assignment_list

    def add_assignment(self, assignment):
        self._assignment_list.append(assignment)

    def remove_assignment(self, assignment):
        self._assignment_list.remove(assignment)


class EC(Association):

    def __init__(self, item_type, type_importance, name, importance, location, reg_schedule, is_team_based, goals, next_event, is_active=True):
        super.__init__(self, item_type, type_importance,
                       name, importance, location, reg_schedule)
        self.is_team_based = is_team_based
        self.goals = goals
        self.next_event = next_event

    # Boolean stating if the EC is team-based
    @property
    def is_team_based(self):
        return self._is_team_based

    @is_team_based.setter
    def is_team_based(self, is_team_based):
        self._is_team_based = is_team_based

    # List containing Goals for the EC
    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, goals):
        self._goals = goals

    # The closest event currently for the EC
    @property
    def next_event(self):
        return self._next_event

    @next_event.setter
    def next_event(self, next_event):
        self._next_event = next_event

    # Boolean stating if the EC is active
    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        self._is_active = is_active


class Club(EC):

    def __init__(self, item_type, type_importance, name, importance, location, reg_schedule, goals, next_event, role, num_hours, is_active=True):
        super.__init__(self, item_type, type_importance,
                       name, importance, location, reg_schedule, True, goals, next_event, is_active)
        self.role = role
        self.num_hours = num_hours

    # Defines role within club
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    # Keeps track of # of hours performing in the club
    @property
    def num_hours(self):
        return self._num_hours

    @num_hours.setter
    def num_hours(self, num_hours):
        self._num_hours = num_hours
