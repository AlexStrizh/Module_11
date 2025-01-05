import requests
import pandas as pd
import matplotlib.pyplot as plt

r = requests.get('https://urban-university.pro/student/lesson/1076')
r.encoding = 'utf-8'
print(r.url)
print(r.headers)
print(r.text)


if __name__ == '__main__':
    df = pd.read_excel('price-goods.xls', sheet_name=0)
    df.head()
    df.to_csv('data_out.txt', header=df.columns, index=None, sep=' ')
    df = pd.read_csv('data_out.txt', delimiter='\t')
    df.to_excel('output.xlsx')


x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [25, 76, 45, 34, 76]

plt.bar(x, y, label='Количество часов')
plt.xlabel('Месяц года')
plt.ylabel('Количество, час')
plt.title('Демонстрация')
plt.legend()
plt.show()