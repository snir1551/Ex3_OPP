from abc import ABC, abstractmethod


class NodeDataInterface(ABC):
    """This abstract class represents an interface of a node."""

    @abstractmethod
    def get_key(self) -> int:
        """

        """
        pass

    @abstractmethod
    def get_pos(self) -> tuple:
        """

        """
        pass

    @abstractmethod
    def get_weight(self) -> float:
        """

        """
        pass

    @abstractmethod
    def set_weight(self, weight):
        """

        """
        pass

    @abstractmethod
    def get_info(self) -> str:
        """

        """
        pass

    @abstractmethod
    def set_info(self, info):
        """

        """
        pass


