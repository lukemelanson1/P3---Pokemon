# Authors: Xander Green, Reece Bunnage, Luke Melanson

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Create the pokemon class
# Luke pt 1
class Pokemon : 
    def __init__(self, name, elemental_type, hit_points) : 
        self.name = name
        self.elemtal_type = elemental_type
        self.hit_points = hit_points

    def get_info(self) :
        return f"{self.name} - Type: {self.elemtal_type} - Hit Points: {self.hit_points}"

    def heal(self) : 
        self.hit_points += 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Create the move class
# Xander pt 1









#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Create the pokemon objects
# Luke pt 2
bulbasaur = Pokemon("Bulbasaur", "Grass", 60)
charmander = Pokemon("Charmander", "Fire", 55)
squirtle = Pokemon("Squirtle", "Water", 65)

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Create the move objects
# Xander pt 2





#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Run the game
# Reece
