import json
from abc import ABC, abstractmethod
from dataclasses import asdict
from pathlib import Path

from src.entities import Vacancy


class Connector(ABC):

    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        """Абстрактный метод получения вакансии"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Абстрактный метод добавления вакансии"""
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy: Vacancy) -> None:
        """Абстрактный метод удаления вакансии"""
        pass

    @staticmethod
    def _parse_vacancy_to_dict(vacancy: Vacancy) -> dict:
        """Статический метод преобразования класса в словарь"""
        return asdict(vacancy)

    @staticmethod
    def _parse_dict_to_vacancy(raw_data: dict) -> Vacancy:
        """Метод парсит список в вакансию"""
        return Vacancy(**raw_data)


class JsonConnector(Connector):

    def __init__(self, file_path: Path, encoding: str = 'utf-8') -> None:
        """Инициализируем путь до файла и кодировку"""

        self.file_path = file_path
        self.encoding = encoding

    def get_vacancies(self) -> list[Vacancy]:
        """Метод чтения вакансии, если файла нет то вернем пустой список, если файл есть то
        читаем и парсим в вакансию, добавляем вакансию в список и возв. список
        """

        if not self.file_path.exists():
            return []

        vacancies = []
        with self.file_path.open(encoding=self.encoding) as f:
            for item in json.load(f):
                vacancy = self._parse_dict_to_vacancy(item)
                vacancies.append(vacancy)
        return vacancies


    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод добавления новой вакансии, сначала с помощью метода get_vacancies() считываем вакансию,
         если ее не существует только затем добавляем ее"""

        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            self._save(*vacancies)


    def remove_vacancy(self, vacancy: Vacancy) -> None:
        """Метод удаления  вакансии, сначала с помощью метода get_vacancies() считываем вакансию,
         если она существует только затем удаляем ее"""

        vacancies = self.get_vacancies()
        if vacancy in vacancies:
            vacancies.remove(vacancy)
            self._save(*vacancies)


    def _save(self, *vacancies: Vacancy) -> None:
        """Метод записи вакансии в файл json"""
        raw_data = [self._parse_vacancy_to_dict(vac) for vac in vacancies]
        with self.file_path.open(mode='w', encoding=self.encoding) as file:
            json.dump(raw_data, file, indent=2, ensure_ascii=False)