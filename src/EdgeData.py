from src.EdgeDataInterface import EdgeDataInterface


class EdgeData(EdgeDataInterface):

    def __init__(self, src: int, w: float, dest: int, tag: int = 0, info: str = ""):
        self.__src = src
        self.__weight = w
        self.__dest = dest
        self.__tag = tag
        self.__info = info

    def get_src(self) -> int:
        """

        """
        return self.__src

    def get_w(self) -> float:
        """

        """
        return self.__weight

    def get_dest(self) -> int:
        """

        """
        return self.__dest

    def get_tag(self) -> int:
        """

        """
        return self.__tag

    def set_tag(self, tag: int):
        """

        """
        self.__tag = tag

    def get_info(self):
        """

        """
        return self.__info

    def set_info(self, info: str):
        """

        """
        self.__info = info

    def __str__(self):
        return "EdgeData(src: %s , weight: %s , dest: %s  , tag : %s  , info: %s)" % (
            self.__src, self.__weight, self.__dest, self.__tag, self.__info)
