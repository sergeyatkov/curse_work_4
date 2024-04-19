class Vacancy:
    name: str
    link: str
    to_salary: int
    from_salary: int
    requirements: str
    responsibility: str

    def __init__(self, name: str, link: str, to_salary: int,
                 from_salary: int, requirements: str, responsibility: str
                 ):
        self.name = name
        self.link = link
        self.to_salary = to_salary
        self.from_salary = from_salary
        self.requirements = requirements
        self.responsibility = responsibility

    def __str__(self):
        """
        Метод для понятного пользователю вывода
        данных о вакансии
        :return: данные о вакансии в строковом формате.
        """
        return (f"Название: {self.name}\n"
                f"Оплата: от {self.from_salary} до {self.to_salary}\n"
                f"Требования: {self.requirements}\n"
                f"Должностные обязанности: {self.responsibility}")

    def __lt__(self, other) -> bool:
        """
        Метод сравнивает зарплаты вакансий.
        :param other: null
        :return: True
        """
        if self.to_salary is None or other.to_salary is None:
            return False
        return self.to_salary < other.to_salary

    def __gt__(self, other) -> bool:
        """
        Метод сравнивает зарплаты вакансий.
        :param other: null
        :return: True
        """
        if self.to_salary is None or other.to_salary is None:
            return False
        return self.to_salary > other.to_salary

    def __eq__(self, other) -> bool:
        """
        Метод сравнивает зарплаты вакансий.
        :param other: null
        :return: True
        """
        if self.to_salary is None or other.to_salary is None:
            return False
        return self.to_salary == other.to_salary
