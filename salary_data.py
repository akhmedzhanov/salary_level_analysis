import csv
import numpy as np
from matplotlib import pyplot as plt

with open('salary_data.csv', 'r', encoding='utf-8') as filename:
    data = csv.DictReader(filename, delimiter=';')
    salary_grouped = {}
    for elem in data:
        salary_grouped.setdefault(elem['company_name'], []).append(int(elem['salary']))
    salary_grouped = {company: round(sum(salary)/len(salary), 2) for company, salary in salary_grouped.items()}

    company, avg_salary = [], []
    for c, s in sorted(salary_grouped.items(), key=lambda x: -x[1]):
        company.append(c)
        avg_salary.append(s)

    avg_salary = np.array(avg_salary)
    median_salary_line = np.median(avg_salary)

    fig = plt.figure(figsize=(13, 6.5))
    fig.set_facecolor('#eee')
    ax = fig.add_subplot()
    plt.figtext(0.1, 0.9, 'Информация о зарплатах сотрудников в различных компаниях', fontsize=24)
    ax.set_xlabel('Заработная плата')
    ax.barh(company, avg_salary, height=0.4, color='y')
    plt.axvline(x=median_salary_line, label='Медианная заработная плата по выборке компаний')
    plt.tick_params(axis='y', which='major', labelsize=8)
    ax.legend(loc='upper left', fontsize=8)
    ax.set(facecolor='#AAFFAA')
    ax.grid(axis='x')

    plt.show()

