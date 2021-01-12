from src.NodeDataInterface import NodeDataInterface


class NodeData(NodeDataInterface):

    def __init__(self, key: int, pos: tuple = None, weight: float = 0, info: str = ""):
        self.__key = key
        self.__info = ""
        self.__pos = pos
        self.__weight = weight
        self.__info = info
        self.__counter_edges_in = 0
        self.__counter_edges_out = 0

    def get_key(self) -> int:
        """
        @return the key (id) associated with this node.
        """
        return self.__key

    def get_pos(self) -> tuple:
        """
        @return the location of this node
        """
        return self.__pos

    def set_pos(self, pos: tuple):
        """
        Allows changing this node's location
        @param pos - new location  (position) of this node.
        """
        self.__pos = pos

    def get_weight(self) -> float:
        """
        @returns the weight associated with this node used for algorithm
        """
        return self.__weight

    def set_weight(self, weight):
        """
        Allows changing this node's weight.
        @param weight - the new weight
        """
        self.__weight = weight

    def get_info(self):
        """
        @return the remark (meta data) associated with this node.
        """
        return self.__info

    def set_info(self, info):
        """
        Allows changing the remark (meta data) associated with this node.
        """
        self.__info = info

    def get_counter_edges_in(self) -> int:
        """
        @return the counter of the edges in to this node
        """
        return self.__counter_edges_in

    def set_counter_edges_in(self, counter_edges_in: int):
        """
        update the counter of the edges in to this node
        """
        self.__counter_edges_in = counter_edges_in

    def get_counter_edges_out(self) -> int:
        """
        @return the counter of the edges out from this node
        """
        return self.__counter_edges_out

    def set_counter_edges_out(self, counter_edges_out: int):
        """
        update the counter of the edges out from this node
        """
        self.__counter_edges_out = counter_edges_out

    def encoder(self):
        """

        """
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
        return "NodeData(key: %s , position: %s , information: %s  , weight : %s)" % (
            self.__key, self.get_pos(), self.__info, self.__weight)

    def __repr__(self):
        return f"{self.__key}: |edges out| {self.get_counter_edges_out()} |edges in| {self.get_counter_edges_in()}"
