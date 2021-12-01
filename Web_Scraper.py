import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=Computer%20Science&l=Naples%2C%20FL"
website_data = requests.get(url)
response = website_data.text

# https://www.Indeed.com/jobs?q=Part%20Time&l=Naples%2C%20FL&vjk
# html.parser allows for picking through html
soup = BeautifulSoup(response, 'html.parser')
job = soup.find_all('div', class_="slider_container")

file = 'job_list.csv'
f = open(file, 'w')
headers = 'Position, Company, Location, Salary \n'
f.write(headers)


for jobs in job:
    position = jobs.find('div', class_="singleLineTitle").text
    company = jobs.find('span', class_="companyName").text
    location = jobs.find('div', class_="companyLocation").text
    try:
        salary = jobs.find('span', class_="salary-snippet").text
    except AttributeError:
        salary = 'None Listed'
    #f.write(position + ',' + company + ',' + location + ',' + salary + '\n')
    print(position)
f.close()
