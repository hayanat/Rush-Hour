#############################################################
# FILES : board.py, car.py, game.py
# WRITER : haya_natsheh , hayanat2002 , 325098440
# EXERCISE : ex9
# Sources and links: None
#############################################################

import sys
from car import Car
from board import Board
from helper import load_json


class Game:
    """
    This is the class of the game, the game gets input from the player and
    moves the car according to the input, if the input was wrong it prints
    appropriate message.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board
        self.__legal_names = ["Y", "B", "O", "W", "G", "R"]
        self.__legal_keys = ["d", "u", "l", "r"]

    def __single_turn(self):
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        while not (self.__board.cell_content(self.__board.target_location())):
            user = input("please enter LETTER , direction: ")
            if user == "!":
                break
            if len(user) != 3:
                print("it must be 3")
                continue
            car_name, comma, car_key = user
            if car_name not in self.__legal_names:
                print("illegal name")
                continue
            if car_key not in self.__legal_keys:
                print("illegal key")
                continue
            if comma != ",":
                print("enter it correctly")
                continue
            if self.__board.move_car(car_name, car_key):
                print(self.__board)
            else:
                print("cannot do that")
        if self.__board.cell_content(self.__board.target_location()):
            print("You won !!!")


def json_file(board):
    legal_names = ["Y", "B", "O", "W", "G", "R"]
    legal_length = [2, 3, 4]
    legal_orientation = [0, 1]
    dic = load_json(sys.argv[1])
    for name, attributes in dic.items():
        if name not in legal_names or len(name) != 1:
            continue
        if attributes[0] not in legal_length:
            continue
        if tuple(attributes[1]) not in board.cell_list():
            continue
        if attributes[2] not in legal_orientation:
            continue
        my_car = Car(name, attributes[0], tuple(attributes[1]), attributes[2])
        adding = board.add_car(my_car)
        if adding is False:
            continue
    return board


if __name__ == "__main__":
    board = Board()
    game = Game(board)
    json_file(board)
    print(board)
    game.play()
