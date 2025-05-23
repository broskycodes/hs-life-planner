class Item:

    def __init__(self, item_type, type_importance, name, importance, location) -> None:
        self.item_type = item_type  # Type of item (Ex. Academic, EC, Social)
        # Importance of type (Ex. Academic > Social), user defined (0-10)
        self.type_importance = type_importance
        self.name = name  # Name of item
        # Importance of item itself, user defined (0-10)
        self.importance = importance
        self.location = location  # Location of item (Ex. Room no., address)

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


class Course(Item):
    item_type = "Course"
    type_importance = 5

    def __init__(self, subject, importance, grade, weight=4.0, assignment_list=[]):
        super._init_(self, item_type, type_importance, )
