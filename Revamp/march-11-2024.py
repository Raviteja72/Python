'''[9:53 AM] Sanyal, Dibakar (Cognizant)
Define a class : Player
with instance attributes:
     playerName , countryName, age
define its constructors to assign some initial values.
Define a method to show details for that particular player.
Define a main class with main-method to make demo for it.'''

class Player:
    def __init__(self, playerName , countryName, age):
          self.playerName = playerName
          self.countryName = countryName
          self.age = age 
    def show_details(self):
         print("Player name : ",self.playerName)
         print("Country Name : ",self.countryName)
         print("Age : ",self.age)

def main():
    player = Player("Ravi","Ind",22)
    player.show_details()

main()

#     @classmethod
#     def main(cls):
#          player = Player("Ravi","Ind",22)
#          player.show_details()

# Player.main()

# player = Player("Ravi","Ind",22)
# player.show_details()

from arrays import *
class main():
     arr = array("i",[12,32,45,78,41,32,])