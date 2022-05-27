class Desk:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Dessert:
    name = Desk()
    calories = Desk()

    def __init__(self, name='', calories=0):
        self.name = name
        self.calories = calories

    def is_healthy(self):
        if self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    flavor = Desk()

    def __init__(self, name='', calories=0, flavor=''):
        super().__init__()
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True