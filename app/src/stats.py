class Stats:

    def __init__(self, MAX_VALUE, map):
        self.__less = [0]*MAX_VALUE
        self.__greater = [0]*MAX_VALUE
        self.__calculate_stats(map)

    def __calculate_stats(self, map):
        for i in range(1, len(map)):
            self.__less[i] = map[i-1]+self.__less[i-1]
        for i in range(len(map)-2, -1, -1):
            self.__greater[i] = map[i+1]+self.__greater[i+1]

    def less(self, value):
        return self.__less[value]

    def greater(self, value):
        return self.__greater[value]

    def between(self, value1, value2):
        if value1 > value2:
            value1, value2 = value2, value1
        return self.__less[value2+1]-self.__less[value1]