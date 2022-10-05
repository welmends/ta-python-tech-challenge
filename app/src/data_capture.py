from .stats import Stats

class DataCapture:

    def __init__(self, MAX_VALUE=1000):
        self.__MAX_VALUE = MAX_VALUE
        self.__map = [0]*self.__MAX_VALUE

    def add(self, value):
        if type(value) != int or value < 0 or value >= 1000:
            raise ValueError("Value must a positive integer less than {}".format(self.__MAX_VALUE))
        self.__map[value]+=1

    def build_stats(self):
        return Stats(self.__MAX_VALUE, self.__map)

    def clean(self):
        self.__map = [0]*self.__MAX_VALUE