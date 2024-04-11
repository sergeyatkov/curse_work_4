from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Класс Parser является образцом для создания
    классов наследников.
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
