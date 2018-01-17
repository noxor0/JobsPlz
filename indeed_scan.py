import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    my_skills = open('skills', 'r').read().splitlines()
    all_job_list = []
    raw_url = open('url', 'r').readlines()[0].strip()
    for page in range(10):
        curr_url = raw_url.format(str(page) + '0')
        r = requests.get(curr_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        job_rows = soup.body.find('table', id='resultsBody').find('tr').find('td').find('table', id='pageContent').find_all('tr')
        for row in job_rows:
            exp = row.find('div', {'class': 'experience'})
            if set(my_skills) & set(exp):
                name = row.find('div', {'class': 'name'})
                apply_link = row.find('div', {'class': 'apply'})
                all_job_list.append({
                    'name' : name,
                    'apply': apply_link,
                    'experience' : exp
                })
    print(all_job_list)
