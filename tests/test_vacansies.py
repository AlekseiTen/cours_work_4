import pytest

from src.entities import Vacancy


@pytest.mark.parametrize('field_name', ['salary_from', 'salary_to'])
def test_vacancy_salary_failed_to_be_negative(field_name):
    """
    Тест на то, что зарплата не может быть отрицательной
    """
    with pytest.raises(ValueError, match='Зарплата не может быть отрицательной'):
        Vacancy('name', 'url', **{field_name: -1})


def test_vacancy_compare_by_salary_from():
    """Тест на <, =, > зарплат от(from)"""
    v1 = Vacancy('name', 'url', salary_from=10)
    v2 = Vacancy('name', 'url', salary_from=20)
    v3 = Vacancy('name', 'url', salary_from=20)
    assert v1 < v2
    assert v2 == v3
    assert v3 > v1


def test_vacancy_compare_by_salary_to():
    """Тест на <, =, > зарплат до(to)"""
    v1 = Vacancy('name', 'url', salary_to=10)
    v2 = Vacancy('name', 'url', salary_to=20)
    v3 = Vacancy('name', 'url', salary_to=20)
    assert v1 < v2
    assert v2 == v3
    assert v3 > v1


def test_vacancy_compare_by_different_salary():
    """ Тест на to меньше from"""
    v1 = Vacancy('name', 'url', salary_to=10)
    v2 = Vacancy('name', 'url', salary_from=20)
    assert v1 < v2


def test_test_equal_vacancies():
    """Тест на сравнение eq"""
    v2 = Vacancy('name_1', 'url', salary_to=20)
    v3 = Vacancy('name_2', 'url', salary_to=20)
    assert v2 == v3
