import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌
def fire_gun():
   bulletChamber = spin_chamber()
   endMessage = "Keep playing!"

   if(bulletChamber == bullet_position):
       endMessage = "You are dead!" 

   return endMessage


print(fire_gun())
