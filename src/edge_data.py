class EdgeData:

    def __init__(self, src: int, w: float, dest: int):
        self.__src = src
        self.__weight = w
        self.__dest = dest
        self.__tag = 0
        self.__info = ""

    def get_src(self) -> int:
        return self.__src

    def get_w(self) -> float:
        return self.__weight

    def get_dest(self) -> int:
        return self.__dest

    def get_tag(self) -> int:
        return self.__tag

    def set_tag(self, tag):
        self.__tag = tag

    def get_info(self):
        return self.__info

    def set_info(self, info):
        self.__info = info

    def __str__(self):
        return "EdgeData(src: %s , weight: %s , dest: %s  , tag : %s  , info: %s)" % (
            self.__src, self.__weight, self.__dest, self.__tag, self.__info)
