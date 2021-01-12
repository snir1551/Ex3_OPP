from abc import ABC, abstractmethod


class NodeDataInterface(ABC):
    """This abstract class represents an interface of a node."""

    @abstractmethod
    def get_key(self) -> int:
        """
        @return the key (id) associated with this node.
        """
        pass

    @abstractmethod
    def get_pos(self) -> tuple:
        """
        Returns the location of this node
        """
        pass

    @abstractmethod
    def set_pos(self, pos: tuple) -> tuple:
        """
        Allows changing this node's location
        @param pos - new location  (position) of this node.
        """
        pass

    @abstractmethod
    def get_weight(self) -> float:
        """
        @returns the weight associated with this node.
        """
        pass

    @abstractmethod
    def set_weight(self, weight):
        """
        Allows changing this node's weight.
        @param weight - the new weight
        """
        pass

    @abstractmethod
    def get_info(self) -> str:
        """
        @return the remark (meta data) associated with this node.
        """
        pass

    @abstractmethod
    def set_info(self, info):
        """
        Allows changing the remark (meta data) associated with this node.
        """
        pass
