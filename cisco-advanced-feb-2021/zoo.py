from animal import Wolf, Sheep, Snake, Parrot, Cage, Zoo

wolf = Wolf('black')            # species, color, # legs
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('black')

print(wolf)                      # black wolf, 4 legs
print(sheep1)                    # white sheep, 4 legs
print(sheep2)                    # white sheep, 4 legs
print(snake)                     # brown snake, 0 legs
print(parrot)                    # black parrot, 2 legs

c1 = Cage(1)
c1.add_animals(wolf, sheep1, sheep2)
print(c1)                        # cage number + animal printouts

c2 = Cage(2)                    # an ID number, not that important
c2.add_animals(snake, parrot)
print(c2)                        # cage number + animal printouts
#
z = Zoo()
z.add_cages(c1, c2)
print(z)                           # show all cages, all animals

print(z.animals_by_color('black'))
print(z.number_of_legs())