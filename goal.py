class Goal():
    def __init__(self, association, description, importance=5, timeframe="NA"):
        self.association = association
        self.description = description
        self.timeframe = timeframe
        self.importance = importance

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
