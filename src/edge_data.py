class EdgeData:

    def __init__(self, src: int, w: float, dest: int):
        self.__src = src
        self.__weight = w
        self.__dest = dest
        self.tag = 0
        self.info = ""

    def get_src(self):
        return self.__src

    def get_w(self):
        return self.__weight

    def get_dest(self):
        return self.__dest

    def __str__(self):
        return "EdgeData(src: %s , weight: %s , dest: %s  , tag : %s  , info: %s)" % (
            self.__src, self.__weight, self.__dest, self.tag, self.info)
