from abc import ABC, abstractmethod

import requests


from src.entities import Vacancy


class Parser(ABC):

    @abstractmethod
    def get_vacancies(self, search_text: str) -> list[dict]:
        pass


class HHVacanciesAPI(Parser):

    def get_vacancies(self, search_text: str) -> list[Vacancy]:
        """Метод для получения вакансий по параметрам"""

        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': search_text,
            'only_with_salary': True,
            'per_page': 10,
        }

        raw_vacancies = self._get_list(url, params, max_pages=2)
        return [
            Vacancy(
                name=data['name'],
                url=data['alternate_url'],
                salary_currency=data['salary']['currency'],
                salary_from=data['salary']['from'],
                salary_to=data['salary']['to'],
            )
            for data in raw_vacancies
        ]

    def _get_list(self, url: str, params: dict, max_pages: int = 1) -> list[dict]:
        """
        Метод получения вакансий в виде списка по слову кот. задаст пользователь
        :param url:
        :param params:
        :param max_pages:
        :return:
        """
        items = []
        for current_page in range(0, max_pages):
            params['page'] = current_page
            response = requests.get(url, params=params, timeout=10)
            data = response.json()
            items.extend(data['items'])

        return items

