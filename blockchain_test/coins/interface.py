from abc import ABC, abstractmethod
from decimal import Decimal


class Interface(ABC):

    # @abstractmethod
    # def __init__(self, *args, **kwargs) -> None:
    #     pass

    @abstractmethod
    def get_height_block(self) -> int:
        pass

    @abstractmethod
    def get_balance(self, address: str) ->Decimal:
        pass
