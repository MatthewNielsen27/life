# This code will implement a simple creature
from random import randint

# Generic organism
class Cell:
    def __init__(self, world_x, world_y):
        # Identification
        self.name = "dove"
        self.age = 0
        self.hp = 100
        self.base_hp = 100
        self.life_expectancy = 20
        
        # Move semantics
        self.moves_per_turn = 5
        self.moves_this_turn = 0
        self.satisfied = False
        self.cost_per_move = 20

        # Positional elements
        self.x = world_x
        self.y = world_y
        self.home_x = world_x
        self.home_y = world_y


    def __str__(self):
        return f'Type: {self.name}\t Health: {self.hp}\t Age: {self.age}\t X: {self.x}\t Y: {self.y} Moves: {self.moves_this_turn}'


    def eat(self, _food = 100):
        self.hp += _food  # Add 100hp for now, will vary based on food later


    # Split the Cell !!
    def reproduce(self):
        return Cell()


    # Move the cell based on this direction
    def move(self, direction):
        if direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "down":
            self.y -= 1
        else:
            self.y += 1
        
        self.moves_this_turn += 1  # Increment the move counter
        self.hp -= self.cost_per_move  # Take the cut to health

    
    def pos_with_move(self, direction):
        if direction == "left":
            return self.x - 1, self.y
        elif direction == "right":
            return self.x + 1, self.y
        elif direction == "down":
            return self.x, self.y - 1
        else:
            return self.x, self.y + 1

    # If the creature has the intention to move this turn
    def will_move(self):
        return (not self.satisfied) and self.moves_this_turn < self.moves_per_turn and self.is_alive


    # Returns the fraction of remaining hp vs base_hp
    def health(self):
        return self.hp / self.base_hp


    def fight(self, creature):
        self.hp /= 2

    def is_alive(self):
        return self.hp > 0
    

    def return_home(self):
        # Add cost to return home
        self.x = self.home_x
        self.y = self.home_y

        self.hp -= (self.moves_this_turn * self.cost_per_move)
        self.moves_this_turn = 0
        self.satisfied = False

