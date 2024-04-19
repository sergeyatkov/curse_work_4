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
        return (f"\n\nНазвание: {self.name}\n"
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

    @staticmethod
    def weed_on_salary(range_salary: str, vacancies: list) -> list:
        """
        Метод выводит упорядоченный список вакансий
        :param vacancies: список вакансий
        :param range_salary: диапазон зарплат
        :return: упорядоченный список вакансий
        """
        str_from_salary, str_to_salary = range_salary.split("-")
        from_salary = int(str_from_salary)
        to_salary = int(str_to_salary)

        ordered_vacancies = []

        for vacancy in vacancies:
            if vacancy.from_salary is not None and vacancy.to_salary is not None:
                if from_salary <= vacancy.from_salary <= to_salary or \
                        from_salary <= vacancy.to_salary <= to_salary:
                    ordered_vacancies.append(vacancy)
            elif vacancy.from_salary is not None:
                if from_salary <= vacancy.from_salary <= to_salary:
                    ordered_vacancies.append(vacancy)
            elif vacancy.to_salary is not None:
                if from_salary <= vacancy.to_salary <= to_salary:
                    ordered_vacancies.append(vacancy)

        return ordered_vacancies
