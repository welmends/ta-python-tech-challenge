class Stats:
    """
    Stats class, used for computing and accessing default statistics.

    ...

    Attributes
    ----------
    __less : list<int>
        array that stores the less statistics based on some previous computations.
    __greater : list<int>
        array that stores the greater statistics based on some previous computations.

    Methods
    -------
    __calculate_stats(value)
        calculates the stats to be accessed later via public methods.
    less()
        returns the less statistics.
    greater()
        returns the greater statistics.
    between()
        returns the between statistics.
    """

    def __init__(self, MAX_VALUE: int, map: list):
        self.__less = [0]*MAX_VALUE
        self.__greater = [0]*MAX_VALUE
        self.__calculate_stats(map)

    def __calculate_stats(self, map: list) -> None:
        """Calculates the stats and put then on some arrays.

        This function works by accessing map array and iteratively 
        storing the accumalated values into the less and greater arrays.

        It has a time complexity of O(M), where M is the number of elements in map.
        Since M is a constant equal to 1000 the time complexity is O(1) or constant.

        Parameters
        ----------
        map : list<int>
            array of captures, defined on the DataCapture class.
        """
        for i in range(1, len(map)):
            self.__less[i] = map[i-1]+self.__less[i-1]
        for i in range(len(map)-2, -1, -1):
            self.__greater[i] = map[i+1]+self.__greater[i+1]

    def less(self, value: int) -> int:
        """Find the number of captures that are less than the given value.

        It has a time complexity of O(1) or constant.

        Parameters
        ----------
        value : int
            value to be used as threshold
        """
        if type(value) != int or value < 0 or value >= 1000:
            raise ValueError("Value must a positive integer less than {}".format(len(self.__less)))
        return self.__less[value]

    def greater(self, value: int) -> int:
        """Find the number of captures that are greater than the given value.

        It has a time complexity of O(1) or constant.

        Parameters
        ----------
        value : int
            value to be used as threshold
        """
        if type(value) != int or value < 0 or value >= 1000:
            raise ValueError("Value must a positive integer less than {}".format(len(self.__greater)))
        return self.__greater[value]

    def between(self, value1: int, value2: int) -> int:
        """Find the number of captures that are between two given values.

        It has a time complexity of O(1) or constant.

        Parameters
        ----------
        value1 : int
            value to be used as lower threshold
        value2 : int
            value to be used as upper threshold
        """
        if type(value1) != int or value1 < 0 or value1 >= 1000 or \
           type(value2) != int or value2 < 0 or value2 >= 1000:
            raise ValueError("Value must a positive integer less than {}".format(len(self.__less)))
        if value1 > value2:
            value1, value2 = value2, value1
        return self.__less[value2+1]-self.__less[value1]