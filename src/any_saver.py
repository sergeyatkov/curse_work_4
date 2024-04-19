from abc import ABC, abstractmethod


class Saver(ABC):
    """
    Класс Saver является образцом для создания
    классов наследников.
    """

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def delete(self):
        pass
