from bs4 import BeautifulSoup
import requests


class HabrScraper():
    def __init__(self, name, profession, date):  # every vacancy like an object
        self.company_name = name.text
        self.profession = profession.text
        self.date = date.text

    def show_result(self):
        print(f'Company name: {self.company_name}')
        print(f'Profession: {self.profession}')
        print(f'Publicated date: {self.date}', end='\n\n')

    def write_result(self):
        write_in_file = (f'Company name: {self.company_name}\n'
                         f'Profession: {self.profession}\n'
                         f'Publicated date: {self.date}\n\n')

        with open('vacancy.txt', 'a') as file:
            file.write(write_in_file)


def vacancy(html_text) -> list:
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find('div', class_='section-group section-group--gap-medium')
    company_name = jobs.find_all('div', class_='vacancy-card__company-title')
    professions = jobs.find_all('a', class_='vacancy-card__title-link')
    publication_time = jobs.find_all('time', class_='basic-date')

    vacancy_list = []

    for n in range(len(company_name)):
        vacancy_list.append(HabrScraper(company_name[n], professions[n], publication_time[n]))

    return vacancy_list


def main():
    #working = True
    #URL = input('Write the URL: ')
    URL = 'https://career.habr.com/vacancies?page=1&s[]=2&s[]=3&skills[]=446&type=all'
    html_text = requests.get(URL).text
    vacancy_list = vacancy(html_text)

    for el in vacancy_list:
        el.show_result()
        el.write_result()


if __name__ == '__main__':
    main()