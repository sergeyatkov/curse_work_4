from src import hh_api
from src.hh_api import HhParser
from src.json_saver import JsonSaver
from src.vacancy import Vacancy


def user_interaction():
    hh_info = HhParser()
    json_connector = JsonSaver()

    search_query = input("Введите ключевое слово для поиска вакансий: ")
    range_salary = input("Введите желаемую сумму заработной \n"
                         "платы от и до через дефис '-' : ")
    number_of_vacancies = int(input("Введите количество вакансий,\n"
                                    "которое вы желаете просмотреть: "))

    hh_vacancies = hh_info.load_vacancies(search_query)
    json_connector.insert(hh_vacancies)
    vacancies = json_connector.select()

    ordered_vacancies = Vacancy.weed_on_salary(range_salary, vacancies)

    for vacancy in ordered_vacancies:
        print(vacancy)
        number_of_vacancies -= 1
        if number_of_vacancies == 0:
            break


if __name__ == "__main__":
    user_interaction()
