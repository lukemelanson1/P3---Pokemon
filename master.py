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

class Move():
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points):
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points

    def get_info(self):
        return f"{self.move_name} (Type: {self.elemental_type}: {self.low_attack_points} to {self.high_attack_points} Attack Points)"
    
    def generate_attack_value(self):
        random_attack_points = rd.randrange(self.low_attack_points, self.high_attack_points + 1)
        return random_attack_points

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Create the pokemon objects
# Luke pt 2
bulbasaur = Pokemon("Bulbasaur", "Grass", 60)
charmander = Pokemon("Charmander", "Fire", 55)
squirtle = Pokemon("Squirtle", "Water", 65)

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Create the move objects
# Xander pt 2
    
oTackle = Move("Tackle", "Normal", 5, 20)
oQuick_attack = Move("Quick Attack", "Normal", 6, 25)
oSlash = Move("Slash", "Normal", 10, 30)
oFlamethrower = Move("Flamethrower", "Fire", 5, 30)
oEmber = Move("Ember", "Fire", 10, 20)
oWater_gun = Move("Water Gun", "Water", 5, 15)
oHydro_pump = Move("Hydro Pump", "Water", 20, 25)
oVine_whip = Move("Vine Whip", "Grass", 10, 25)
oSolar_Beam = Move("Solar Beam", "Grass", 18, 27)

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Run the game
# Reece
