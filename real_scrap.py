from bs4 import BeautifulSoup
import requests  # library, what can go to the websites

html_text = requests.get('https://career.habr.com/vacancies?page=1&s[]=2&s[]=3&skills[]=446&type=all').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find('div', class_='section-group section-group--gap-medium')
company_name = jobs.find_all('div', class_='vacancy-card__company-title')
professions = jobs.find_all('a', class_='vacancy-card__title-link')
publication_time = jobs.find_all('time', class_='basic-date')

for num in range(len(company_name)):
    print(f'№{num+1}')
    print(f'Company: {company_name[num].text}')
    print(f'Profession: {professions[num].text}')
    print(f'Data: {publication_time[num].text}', end='\n\n')
