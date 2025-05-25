# Defines any specific task, holding at least a name and an association
class Item:
    def __init__(self, name, association):
        self.name = name  # Name of event
        # Item the event is associated with (course, EC, NA)
        self.association = association

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

    def display(self):
        return [self.name, self.association]

# Defines an event with a specific timeframe (anything scheduled)


class ScheduledEvent(Item):
    def __init__(self, name, association, time, is_repeated):
        super.__init__(self, name, association)
        self.time = time  # List containing the start and end times
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
        return super().display().append(self.time, self.is_repeated)
