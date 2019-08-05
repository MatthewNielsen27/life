from environment import World
from creature import Cell

from random import randint, choice

def main():
    env = World(10, 10)
    creatures = list()

    env.replenish(20)

    env.display()

    num_creatures = 10

    for i in range(0, num_creatures):
        x, y = env.random_location()
        creatures.append(Cell(x, y))

        print(creatures[i])


    total_rounds = 10


    iterations = 0
    for i in range(0, total_rounds):
        
        creatures_can_move = True

        while(creatures_can_move and iterations < 1000000):
            for creature_i in range(0, len(creatures)):
                creature = creatures[creature_i]

                if creature.will_move():
                    possible_moves = {"left", "right", "up", "down"}

                    while(len(possible_moves) and not creature.satisfied):
                        direction = choice(tuple(possible_moves))
                        xpos, ypos = creature.pos_with_move(direction)

                        if env.valid_spot(xpos, ypos):
                            print(f'Moving: {creature_i}  ({creature.moves_this_turn})')
                            creature.move(direction)
                            if env.board[creature.x][creature.y].total_nutrients() > 0:
                                creature.eat(env.board[creature.x][creature.y].consume().nutrients)
                                creature.satisfied = True  # Conditions for satisfaction will change
                            break

                        possible_moves.remove(direction)

            iterations += 1


            # Continue this round if any creature can continue to move
            creatures_can_move = False
            for creature_i in range(0, len(creatures)):
                creature = creatures[creature_i]
                
                if creature.will_move():
                    # print(f'Creature: {creature_i} still wants to move after doing {creature.moves_this_turn} moves')
                    creatures_can_move = True
                

        print("Round ended")
        env.display()
        for creature in creatures:
            print(creature)
            creature.return_home()

        
        
    



                    






        


    
    



    





if __name__ == "__main__":
    main()
