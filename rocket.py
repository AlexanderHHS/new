from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, name = "TBD", x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        self.name = name
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return distance

    def get_name(self):
        #simply return the name
        return self.name

    def introduction(self):
        print("Hi, I am a rocket named", self.name, ". Nice to meet you.")
    
# Make two rockets, at different places.
rocket1 = Rocket()  #This one will be at default x and y position
rocket2 = Rocket("Tom",10,5)  # This one is at 10, 5

#Print the names
print("The names of the rockets are...")
print(rocket1.get_name())
print(rocket2.name)

# Show the distance between them.
distance = rocket1.get_distance(rocket2)
print("The rockets are %f units apart." % distance)

#Move rocket1 up a bit
rocket1.move_rocket(0,2)

#Move the rockets some more to test out the methods
distance = rocket1.get_distance(rocket2)
print("The rockets are,", distance, " units apart.")
rocket1.move_rocket(0,2)
distance = rocket1.get_distance(rocket2)
print("The rockets are %f units apart." % distance)

rocket1.introduction()
rocket2.introduction()

