import json
import requests

url = "http://127.0.0.1:8000/employees-apiemployees/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

employees_data = json.loads(response.text)
print(employees_data)

salaries_lst = []

for employee in employees_data:
    salaries_lst += ([employee['salary']])
print(salaries_lst)

number_of_salaies = 0
total_salaries = 0

for salary in salaries_lst:
    number_of_salaies += 1
    total_salaries += salary

print(number_of_salaies)
print(total_salaries)

average_salary = total_salaries / number_of_salaies

print(average_salary)

import datetime

hire_dates_list = []

for employee in employees_data:
    hire_dates_list += ([employee['hire_date']])

print(hire_dates_list)

new_dates_list = []
format = "%Y-%m-%d"

for dt in hire_dates_list:
    new_dates_list.append(datetime.datetime.strptime(dt, format).date())
print(new_dates_list)

today_date = datetime.date.today()
print(today_date)

from datetime import timedelta

year_ago = 365
date_year_ago = today_date - timedelta(days=year_ago)
print(date_year_ago)

year_ago_list = []

for date in new_dates_list:
    if date < date_year_ago:
        year_ago_list.append(date)
print(year_ago_list)

last_dates_list = []

for dt in year_ago_list:
    last_dates_list.append(dt.strftime(format))
print(last_dates_list)

need_rise_list = []
for emp in employees_data:
    if emp['hire_date'] in last_dates_list and emp['salary'] < average_salary:
        need_rise_list.append(emp)
print(need_rise_list)

final_result = json.dumps(need_rise_list, indent=2)
print(final_result)

with open('file.txt', 'w') as file:
    file.write(final_result)
