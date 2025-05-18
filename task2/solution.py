import csv

import requests
from bs4 import BeautifulSoup


class WorkCSV:

    @staticmethod
    def save(path: str, data: dict[str, int]):
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Letter', 'Count'])
            writer.writeheader()
            [writer.writerow({'Letter': key, 'Count': value}) for key, value in data.items()]


class AnimalsCounter:

    def __init__(self):
        self._url_wiki: str = 'https://ru.wikipedia.org'
        self._end_url: str = '/wiki/Категория:Животные_по_алфавиту'
        self._headers: dict[str, str] = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        self.total_number_animals: dict[str, int] = {}

    def _send_request(self):
        return requests.get(url=self._url_wiki + self._end_url, headers=self._headers)

    def _add_animals(self, animals, stop_iter):
        for animal in animals.next_elements:
            if animal.name == 'li':
                self.total_number_animals[animal.text[0]] = self.total_number_animals.get(animal.text[0], 0) + 1
            if animal.next_element == stop_iter:
                break

    @staticmethod
    def _get_next_url(div_pages_animals) -> str:
        urls = div_pages_animals.find_all('a', {'title': 'Категория:Животные по алфавиту'})
        for url in urls:
            if url.text == 'Следующая страница':
                return url.get('href')
        return ''

    def get_total_number_animals(self) -> dict[str, int] | None:
        while True:
            if not self._end_url:
                break
            response = self._send_request()
            if not response.status_code == 200:
                return None
            soup = BeautifulSoup(response.text, 'html.parser')
            stop_iter = soup.find('div', {'id': 'catlinks'})
            div_pages_animals = soup.find('div', {'id': 'mw-pages'})
            self._end_url = self._get_next_url(div_pages_animals)

            animals = div_pages_animals.find('div', {'class': 'mw-category-group'}).find('ul')
            self._add_animals(animals, stop_iter)
        return self.total_number_animals


if __name__ == '__main__':
    animals_counter = AnimalsCounter()
    WorkCSV.save('result.csv', animals_counter.get_total_number_animals())
