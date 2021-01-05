class NodeData:

    def __init__(self, key: int, position: tuple):
        self.__key = key
        self.__tag = 0
        self.__info = ""
        self.__position = position
        self.__weight = 0

    def get_key(self) -> int:
        return self.__key

    def get_pos(self) -> tuple:
        return self.__position

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_info(self):
        return self.__info

    def set_info(self, info):
        self.__info = info

    def get_tag(self):
        return self.__tag

    def set_tag(self, tag):
        self.__tag = tag

    def __eq__(self, o: object) -> bool:
        if type(o) is not NodeData:
            return False
        if o.__class__ != self.__class__:
            return False
        elif self.__key != NodeData.get_key(o):
            return False
        elif self.__position != NodeData.get_pos(o):
            return False
        elif self.__tag != NodeData.get_tag(o):
            return False
        elif self.__info != NodeData.get_info(o):
            return False
        elif self.__weight != NodeData.get_weight(o):
            return False
        return True

    def __str__(self):
        return "NodeData(key: %s , position: %s , information: %s  , weight : %s  , tag: %s)" % (
            self.__key, self.__position, self.__info, self.__weight, self.__tag)
