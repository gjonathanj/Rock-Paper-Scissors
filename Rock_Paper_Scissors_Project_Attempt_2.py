"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0 

    def __init__(self):
        self.my_move = None
        self.his_move = None
        # self.score = 0


    def learn(self, my_move, his_move):
        self.my_move = my_move
        self.his_move = his_move

    
class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
    
    def move(self):
        while True:
            move = input("Select your choice! Rock, Paper, Scissors...")
            if move in moves:
                return move
            else:
                print("Sorry, I dont quite understand, please try again.")
        

class RandomPlayer(Player):
    def move(self):
        return(random.choice(moves))



class ReflectPlayer(Player):
    def move(self):
        if self.my_move is None:
            return(random.choice(moves))
        else:
            return self.my_move


class CyclePlayer(Player):
    def move(self):
        if self.his_move is None:
            return(random.choices(moves))
        else:
            index = moves.index(self.his_move) + 1 
            #previous +1 % 



def p1_beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or 
            (one == 'rock' and two == 'cockroach') or
            (one == 'cockroach' and two == 'paper') or
            (one == 'bomb' and two == 'scissors') or
            (one == 'bomb' and two == 'rock') or 
            (one == 'cockroach' and two == 'bomb') or 
            (one == 'scissors' and two == 'cockroach') or
            (one == 'paper' and two == 'bomb'))



def p2_beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or 
            (one == 'rock' and two == 'cockroach') or
            (one == 'cockroach' and two == 'paper') or
            (one == 'bomb' and two == 'scissors') or
            (one == 'bomb' and two == 'rock') or 
            (one == 'cockroach' and two == 'bomb') or 
            (one == 'scissors' and two == 'cockroach') or
            (one == 'paper' and two == 'bomb'))



class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if p1_beats(move1, move2) is True and p2_beats(move1, move2) is False:
            self.p1.score += 1
            print("I sense a disturbance in the force...\n")
        elif p2_beats(move1, move2) is True and p1_beats(move1, move2) is False:
            self.p2.score += 1
            print("You are in this council, but we do not grant you the rank of Master...\n")
        else:
            print("I do not want to fight you, but I will do what I must...\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()