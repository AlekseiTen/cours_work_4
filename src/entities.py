from dataclasses import dataclass


@dataclass
class Vacancy:
    """
    исп. дата-класс вместо метода __init__
    """
    name: str
    url: str
    salary_currency: str = 'RUR'
    salary_from: int | None = None
    salary_to: int | None = None

    def __post_init__(self):
        self.__validate_salary(self.salary_from)
        self.__validate_salary(self.salary_to)


    def __validate_salary(self, salary: int | None) -> None:
        """
        метод валидации зп
        """
        if salary is not None and salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")

    def __lt__(self, other: 'Vacancy') -> bool:
        """
        метод меньше чем (<), сравниваем объект self с объектом other
        """
        if self.salary_from and other.salary_from:
            return self.salary_from < other.salary_from

        if self.salary_to and other.salary_to:
            return self.salary_to < other.salary_to

        self_salary = self.salary_from or self.salary_to
        other_salary = other.salary_from or other.salary_to
        return self_salary < other_salary

    def __eq__(self, other: 'Vacancy') -> bool:
        """Метод сравнения классов"""
        eq_from = self.salary_from == other.salary_from
        eq_to = self.salary_to == other.salary_to
        return eq_from and eq_to
