#############################################################
# FILES : board.py, car.py, game.py
# WRITER : haya_natsheh , hayanat2002 , 325098440
# EXERCISE : ex9
# Sources and links: None
#############################################################

class Car:
    """
    This is a class for the cars, each car has name,length, location,
    orientation. and there are many methods for the car.
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        lst = []
        size = self.__length
        if self.__orientation == 1:
            for i in range(size):
                my_location = list(self.__location)
                my_location[1] = i + my_location[1]
                lst.append(tuple(my_location))
        elif self.__orientation == 0:
            for i in range(size):
                my_location = list(self.__location)
                my_location[0] = i + my_location[0]
                lst.append(tuple(my_location))
        return lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        my_dic = {}
        if self.__orientation == 1:
            my_dic["r"] = "go right"
            my_dic["l"] = "go left"
        elif self.__orientation == 0:
            my_dic["u"] = "go up"
            my_dic["d"] = "go down"
        return my_dic

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """
        size = self.__length
        my_location = list(self.__location)
        if movekey == "u" and self.__orientation == 0:
            my_location[0] -= 1
            return [tuple(my_location)]

        elif movekey == "d" and self.__orientation == 0:
            my_location[0] += size
            return [tuple(my_location)]

        elif movekey == "l" and self.__orientation == 1:
            my_location[1] -= 1
            return [tuple(my_location)]

        elif movekey == "r" and self.__orientation == 1:
            my_location[1] += size
            return [tuple(my_location)]
        else:
            return []


    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if self.__orientation == 0 and movekey == "u":
            loc = list(self.__location)
            loc[0] -= 1
            self.__location = tuple(loc)
            return True
        if self.__orientation == 0 and movekey == "d":
            loc = list(self.__location)
            loc[0] += 1
            self.__location = tuple(loc)
            return True
        if self.__orientation == 1 and movekey == "r":
            loc = list(self.__location)
            loc[1] += 1
            self.__location = tuple(loc)
            return True
        if self.__orientation == 1 and movekey == "l":
            loc = list(self.__location)
            loc[1] -= 1
            self.__location = tuple(loc)
            return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
