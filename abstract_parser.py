from bs4 import BeautifulSoup
import requests
from abc import ABC, abstractmethod
import json


class AbstractScraper:
    def __init__(self, url, file_name='New'):
        self._url = url
        self.file_name = file_name


    def get_data(self):
        html_file = requests.get(self._url).text
        return html_file

    def save_data(self, data):
        with open(f'{self.file_name}.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @abstractmethod
    def parse(self):
        ...


class HabrWorkScraper(AbstractScraper):
    def parse(self):
        html_text = self.get_data()
        vacancy_data = {}

        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find('div', class_='section-group section-group--gap-medium')
        company_name = jobs.find_all('div', class_='vacancy-card__company-title')
        professions = jobs.find_all('a', class_='vacancy-card__title-link')
        publication_time = jobs.find_all('time', class_='basic-date')
        print(jobs.text)

        for n in range(len(company_name)):
            vacancy_info = {}
            vacancy_info['Company name: '] = company_name[n].text
            vacancy_info['Profession: '] = professions[n].text
            vacancy_info['Publicatacion_time'] = publication_time[n].text
            vacancy_data[f'№{n+1}'] = vacancy_info

        self.save_data(data=vacancy_data)


class YouTubeScraper(AbstractScraper):
    def parse(self):
        html_text = self.get_data()
        data = {}

        soup = BeautifulSoup(html_text, 'lxml')
        videos = soup.find('div', class_= 'class="style-scope ytd-two-column-browse-results-renderer"')
        video_name = videos.find_all('div', class_='style-scope ytd-rich-grid-media')
        video_views = videos.find_all('span', class_='inline-metadata-item style-scope ytd-video-meta-block')

        for n in range(len(video_name)):
            data[video_name[n].text] = video_views[n].text

        self.save_data(data=data)


class OnlinerScrapper(AbstractScraper):
    def get_data(self):
        url = self._url.format('products')
        data = requests.get(url, params={'query': 'Телевизор', 'page': '1'}).json()
        return data

    def parse(self):
        page = self.get_data()
        data = {}
        data = self.get_data()
        self.save_data(data)


def main():
    habr_URL = 'https://career.habr.com/vacancies?page=1&s[]=2&s[]=3&skills[]=446&type=all'
    NAME_OF_FILE_1 = 'habr_parse'
    habr = HabrWorkScraper(habr_URL, NAME_OF_FILE_1)
    habr.parse()

    #yt_URL = 'https://www.youtube.com/@Alex007/videos'
    #NAME_OF_FILE_2 = 'youtube_parse'
    #youtube = YouTubeScraper(yt_URL, NAME_OF_FILE_2)
    #youtube.parse()

    onl_URL = 'https://catalog.onliner.by/sdapi/catalog.api/search/{}'
    NAME_OF_FILE_3 = 'onliner_parse'
    onliner = OnlinerScrapper(onl_URL, NAME_OF_FILE_3)
    onliner.parse()
    print('+')


if __name__ == '__main__':
    main()
