from src.api import HHVacanciesAPI
from src.config import DATA_DIR
from src.connector import JsonConnector
from src.user_interaction import start_user_interaction

VACANCIES_PATH = DATA_DIR / "vacancies.json"
api_client = HHVacanciesAPI()
connector = JsonConnector(VACANCIES_PATH)


def main():
    """Основная точка входа в программу."""
    print('Добро пожаловать в программу')
    search_text = input('Введите текст для поиска вакансий: ')

    print('Получаем вакансии...')
    vacancies = api_client.get_vacancies(search_text)

    print('Сохраняем в базу')
    for vac in vacancies:
        connector.add_vacancy(vac)
    start_user_interaction(connector)


if __name__ == "__main__":
    main()
