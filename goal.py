# Describes a specific goal associated with a specific association
class Goal():
    def __init__(self, association, description, importance=5, timeframe="NA"):
        self.association = association  # Association that the goal is associated with
        self.description = description  # Description of the goal
        # [start, end] of the goal if applicable, else "NA"
        self.timeframe = timeframe
        # Importance of the goal from 1-10 (5 if not specified)
        self.importance = importance

    # Getters and setters for instance variables
    @property
    def association(self):
        return self._association

    @association.setter
    def association(self, association):
        self._association = association

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def timeframe(self):
        return self._timeframe

    @timeframe.setter
    def timeframe(self, timeframe):
        self._timeframe = timeframe

    @property
    def importance(self):
        return self._importance

    @importance.setter
    def importance(self, importance):
        self._importance = importance
