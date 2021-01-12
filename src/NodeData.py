from src.NodeDataInterface import NodeDataInterface


class NodeData(NodeDataInterface):

    def __init__(self, key: int, pos: tuple = None):
        self.__key = key
        self.__info = ""
        self.__pos = pos
        self.__weight = 0
        self.__counter_edges_in = 0
        self.__counter_edges_out = 0

    def get_key(self) -> int:
        return self.__key

    def get_pos(self) -> tuple:
        return self.__pos

    def set_pos(self, pos: tuple):
        self.__pos = pos

    def get_weight(self) -> float:
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_info(self):
        return self.__info

    def set_info(self, info):
        self.__info = info

    def get_counter_edges_in(self) -> int:
        return self.__counter_edges_in

    def set_counter_edges_in(self, counter_edges_in: int):
        self.__counter_edges_in = counter_edges_in

    def get_counter_edges_out(self) -> int:
        return self.__counter_edges_out

    def set_counter_edges_out(self, counter_edges_out: int):
        self.__counter_edges_out = counter_edges_out

    def encoder(self):
        if self.get_pos() is None:
            return {
                'id': self.get_key()}
        return {
            'id': self.get_key(),
            'pos': self.get_pos()
        }

    def __eq__(self, other) -> bool:
        if type(other) is not NodeData:
            return False
        if other.__class__ != self.__class__:
            return False
        elif self.__key != NodeData.get_key(other):
            return False
        elif self.get_pos() != NodeData.get_pos(other):
            return False
        elif self.__info != NodeData.get_info(other):
            return False
        elif self.__weight != NodeData.get_weight(other):
            return False
        return True

    def __lt__(self, other):
        if self.__weight == other.__weight:
            return True
        else:
            return self.__weight < other.__weight

    def __str__(self):
        return "NodeData(key: %s , position: %s , information: %s  , weight : %s  , tag: %s)" % (
            self.__key, self.get_pos(), self.__info, self.__weight, self.__tag)

    def __repr__(self):
        return f"{self.__key}: |edges out| {self.get_counter_edges_out()} |edges in| {self.get_counter_edges_in()}"
