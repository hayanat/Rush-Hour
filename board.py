#############################################################
# FILES : board.py, car.py, game.py
# WRITER : haya_natsheh , hayanat2002 , 325098440
# EXERCISE : ex9
# Sources and links: None
#############################################################

from car import Car


class Board:

    """
    This is a class of the board, it has many methods which are related
    to class car.
    """

    def __init__(self):
        self.__bsize = 7
        self.__cars = {}

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        res = []
        row = ""
        for square in self.cell_list():
            if square == (3, 7):
                continue
            if self.cell_content(square):
                row += self.cell_content(square)
            else:
                row += "_"
            if len(row) == 7:
                if square == (3, 6):
                    new = list(square)
                    new[1] = 7
                    if self.cell_content(tuple(new)):
                        row += self.cell_content(square)
                    else:
                        row += "_"
                res.append(row)
                row = ""
        return str(res)

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        lst = []
        for i in range(self.__bsize):
            for j in range(self.__bsize):
                lst.append((i, j))
                if i == 3 and j == 6:
                    lst.append((3, 7))
        return lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        res = []
        for name, car in self.__cars.items():
            possible = car.possible_moves()  # >> possible is dictionary
            for direction in possible.keys():
                cell = car.movement_requirements(direction)
                if cell[0] not in self.cell_list():
                    continue
                if self.cell_content(cell[0]) is not None:
                    continue
                res.append((name, direction, car.possible_moves()[direction]))
        return res

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return tuple([3, 7])

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for name, car in self.__cars.items():
            for one_coord in car.car_coordinates():
                if coordinate == one_coord:
                    return name
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        car_name = car.get_name()
        car_position = car.car_coordinates()
        if car_name not in self.__cars.keys():
            for position in car_position:
                if position not in self.cell_list():
                    return False
                if self.cell_content(position):
                    return False
            self.__cars[car_name] = car
            return True
        return False

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for option in self.possible_moves():
            option_name, option_key, option_msg = option
            if option_name == name and option_key == movekey:
                car = self.__cars[name]
                car.move(movekey)
                self.__cars[name] = car
                return True
        return False
