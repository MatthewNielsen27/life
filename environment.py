import numpy
from random import randrange

from food import Food


class Spot:
    def __init__(self):
        self.m_foods = list()
        self.m_creatures = set()


    def add(self, food_item):
        self.m_foods.append(food_item)

    # Creature visits this spot (when eating)
    def visit(self, creature):
        m_creatures.add(creature)

    def consume(self):
        return self.m_foods.pop()
    

    # Creature leaves this spot (after eating)
    def leave(self, creature):
        m_creatures.remove(creature)
    

    # Clear all visitors at a spot
    def clear_visitors(self):
        m_creatures.clear()

    
    def total_nutrients(self):
        sum = 0
        for food_item in self.m_foods:
            sum += food_item.nutrients

        return sum

    


class World:
    def __init__(self, x_dim, y_dim):
        self.x_size = x_dim
        self.y_size = y_dim
        self.board = [[Spot() for x in range(x_dim)] for y in range(y_dim)] 


    def replenish(self, num_foods):
        for i in range(0, num_foods):
            x, y = self.random_location()
            self.board[x][y].add(Food(100))


    def valid_spot(self, x, y):
        return (0 <= x <= self.x_size - 1) and (0 <= y <= self.y_size - 1)


    # Returns a random tuple (x, y) within the world bounds
    def random_location(self):
        return randrange(0, self.x_size), randrange(0, self.y_size)


    # Print out the contents of the current board
    def display(self, filter="nutrients"):
        for y in range(0, self.y_size):
            for x in range(0, self.x_size):
                nutrients = self.board[x][y].total_nutrients()
                if nutrients:
                    if filter == "nutrients":
                        print(f"[{nutrients}]" , end = '')
                else:
                    print(f"[   ]" , end = '')
            print("")
