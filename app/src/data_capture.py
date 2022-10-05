from .stats import Stats

class DataCapture:
    """
    Data Capture class, used for capturing data and for calling a Stats object.

    ...

    Attributes
    ----------
    __MAX_VALUE : int
        maximum value of a single capture.
    __map : list<int>
        array of captures, where the index is the capture and the value is a accumulator.

    Methods
    -------
    add(value)
        add a capture to the map for accumulation.
        has a time complexity of O(1).
    build_stats()
        call the Stats class to create an object that computes default statistics.
    clear()
        clear the __map attribute.
    """

    def __init__(self, MAX_VALUE : int = 1000):
        self.__MAX_VALUE = MAX_VALUE
        self.__map = [0]*self.__MAX_VALUE

    def add(self, value: int) -> None:
        """Add a capture to the map for accumulation.

        It has a time complexity of O(1) or constant.

        Parameters
        ----------
        value : int
            A single capture that must be positive integer less than __MAX_VALUE attribute

        Raises
        ------
        ValueError
            If the parameter isn't an integer or if the value ins't a positive integer less 
            than __MAX_VALUE attribute.
        """
        if type(value) != int or value < 0 or value >= 1000:
            raise ValueError("Value must a positive integer less than {}".format(self.__MAX_VALUE))
        self.__map[value]+=1

    def build_stats(self) -> Stats:
        """Call Stats class constructor and return a Stats object.

        The constructor has a time complexity of O(M), where M is the __MAX_VALUE attribute.
        Since M is a constant equal to 1000 the time complexity is O(1) or constant.
        """
        return Stats(self.__MAX_VALUE, self.__map)

    def clean(self) -> None:
        """Clean the __map attribute and return to initial state.
        """
        self.__map = [0]*self.__MAX_VALUE