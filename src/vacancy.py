class Vacancy:
    name: str
    to_salary: int
    from_salary: int
    requirements: str
    responsibility: str

    def __init__(self, name, url, to_salary, from_salary, requirements, responsibility):
        self.name = name
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
