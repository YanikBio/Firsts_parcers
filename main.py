from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')  # создаём объект, парсер lxml, content - html страничка
    tag = soup.find('h5')  # находит первую строку с тегом и останавливается
    tags = soup.find_all('h5')  # находит все строки с тегом (save like a list)
    print(tag)
    print(tags)
    for t in tags:
        print(t.text)  # show inner text in tag

    print()
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_cost = course.a.text.split()[-1]

        print(f'{course_name} costs {course_cost}')

