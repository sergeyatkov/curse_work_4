from src.vacancy import Vacancy


def convert_to_object(data):
    """
    Функция преобразовывает список объектов Json в список объектов класса Vacancy
    :param data: Список JSON объектов
    :return: Список объектов Vacancy
    """
    vacancies = []

    for vacancy in data:
        obj_vacancy = Vacancy(vacancy["name"],
                              vacancy["link"],
                              vacancy["to_salary"],
                              vacancy["from_salary"],
                              vacancy["requirements"],
                              vacancy["responsibility"])
        vacancies.append(obj_vacancy)

    return vacancies
