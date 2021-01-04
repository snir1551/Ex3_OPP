class NodeData:

    def __init__(self, key: int, position: tuple):
        self.__key = key
        self.tag = 0
        self.info = ""
        self.__position = position
        self.weight = 0

    def get_key(self) -> int:
        return self.__key

    def get_pos(self) -> tuple:
        return self.__position

    def __str__(self):
        return "NodeData(key: %s , position: %s , information: %s  , weight : %s  , tag: %s)" % (
            self.__key, self.__position, self.info, self.weight, self.tag)
