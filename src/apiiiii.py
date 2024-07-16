# def __init__(self):
#     self.url = 'https://api.hh.ru/vacancies'
#     self.headers = {'User-Agent': 'HH-User-Agent'}
#     self.params = {'text': '',
#                    'page': 0,
#                    'per_page': 5}
#     self.vacancies = []
#
#
# def load_vacancies(self, keyword: str) -> list[dict]:
#     self.params['text'] = keyword
#     while self.params.get('page') != 5:
#         response = requests.get(self.url, headers=self.headers, params=self.params)
#         data = response.json()['items']
#         self.vacancies.extend(data)
#         self.params['page'] += 1
#
#     return self.vacancies