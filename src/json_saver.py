import json
from any_saver import Saver


class JsonSaver(Saver):
    """
    Класс для сохранения информации о вакансиях в JSON-файл.
    """

    def __init__(self):
        self.filename = "vacancies.json"

    def insert(self, vacancies):
        data = []

        for vacancy in vacancies:
            to_salary = vacancy["salary"].get("to") if vacancy["salary"] is not None else None
            from_salary = vacancy["salary"].get("from") if vacancy["salary"] is not None else None

            vacancies_data = {
                "name": vacancy["name"],
                "URL": vacancy["url"],
                "to_salary": to_salary,
                "from_salary": from_salary,
                "requirements": vacancy["snippet"]["requirement"],
                "responsibility": vacancy["snippet"]["responsibility"]
            }
            data.append(vacancies_data)

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def select(self):
        pass

    def delete(self):
        pass
