# Authors: Xander Green, Reece Bunnage, Luke Melanson
# Program Description: Pokemon battle!

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
oBulbasaur = Pokemon("Bulbasaur", "Grass", 60)
oCharmander = Pokemon("Charmander", "Fire", 55)
oSquirtle = Pokemon("Squirtle", "Water", 65)

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
import random as rd

#Create a list that stores each of the 9 objects in it.
lstMoves = [oTackle, oQuick_attack, oSlash,
            oFlamethrower, oEmber, oWater_gun,
            oHydro_pump, oVine_whip, oSolar_Beam]
        



"""
Do a for loop that runs 3 times, and in each iteration, do the following:

Randomly select a Move object from the list you created

Print out the result of the get_info method of the randomly selected object.
Print out Generated attack value:  and then the returned value from running the generate_attack_value method 
on the randomly selected object.
Then delete the move from the list of moves. 
This ensures that you won't randomly select the same move twice. 
If you randomly select the same move twice, the automated tests won't pass."""
for move in range(3):
    move = rd.choice(lstMoves)
    print(move.get_info())
    print("Generated attack value: " + str(move.generate_attack_value()))
    lstMoves.remove(move)

input("Press enter to continue...")

#---Part 2---
#Call the get_info method on the object storing the Charmander Pokémon and print out the result
print(oCharmander.get_info())

#Then call the heal method on the same Charmander object
oCharmander.heal()

#Then call the get_info method on the same Charmander object again and print out the result 
# (you should see that the hit_points have increased)
print(oCharmander.get_info())

#Put the 3 Pokemon objects into a list
lstPokemon = [oCharmander, oSquirtle, oBulbasaur]

#Loop through the list and print out the result of get_info on each Pokemon object in the list.
for pokemon in lstPokemon:
    print(pokemon.get_info())
