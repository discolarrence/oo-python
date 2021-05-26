class DreamCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return 'My dream car is a {} {}.'.format(self.make, self. model)