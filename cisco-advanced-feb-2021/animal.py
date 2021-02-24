class Animal:
    def __init__(self, color, number_of_legs):
        self.color = color
        self.species = type(self).__name__.lower()
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
    number_of_legs = 4
    def __init__(self, color):
        super().__init__(color, Wolf.number_of_legs)


class Sheep(Animal):
    number_of_legs = 4
    def __init__(self, color):
        super().__init__(color, Sheep.number_of_legs)


class Snake(Animal):
    number_of_legs = 0
    def __init__(self, color):
        super().__init__(color, Snake.number_of_legs)

class Parrot(Animal):
    number_of_legs = 0
    def __init__(self, color):
        super().__init__(color, Parrot.number_of_legs)

class Cage:
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *args):
        self.animals += args

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join([f'\t{one_animal}'
                            for one_animal in self.animals])
        return output

class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        self.cages += args

    def __repr__(self):
        return '\n'.join([str(one_cage)
                          for one_cage in self.cages])

    def animals_by_color(self, color):
        return [str(one_animal)
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color]

    def number_of_legs(self):
        return sum([one_animal.number_of_legs
                    for one_cage in self.cages
                    for one_animal in one_cage.animals])