from abc import ABC, abstractmethod


class EdgeDataInterface(ABC):
    """This abstract class represents an interface of a edge."""

    @abstractmethod
    def get_src(self) -> int:
        """

        """
        pass

    @abstractmethod
    def get_w(self) -> float:
        """

        """
        pass

    @abstractmethod
    def get_dest(self) -> int:
        """

        """
        pass

    @abstractmethod
    def get_tag(self) -> int:
        """

        """
        pass

    @abstractmethod
    def set_tag(self, tag):
        """

        """
        pass

    @abstractmethod
    def get_info(self):
        """

        """
        pass

    @abstractmethod
    def set_info(self, info):
        """

        """
        pass
