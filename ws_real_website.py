import time

from bs4 import BeautifulSoup
import requests


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name}\n')
                    f.write(f'Required Skills: {skills}\n')
                    f.write(f'More info: {more_info}\n')
                print(f'Company Name: {company_name}')
                print(f'Required Skills: {skills}')
                print(f'More info: {more_info}')
                print()


if __name__ == '__main__':
    
    print('Put some skill that you are not familiar with')
    unfamiliar_skill: str = input('> ')
    print(f'Filtering out {unfamiliar_skill}:\n')
    
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} minute(s)...\n')
        time.sleep(time_wait * 60)
