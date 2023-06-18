from bs4 import BeautifulSoup
import csv

with open("dns.html") as file:
    src = file.read()
    
soup = BeautifulSoup(src, 'lxml')

laptops = soup.find_all("div", class_="catalog-product ui-button-widget")

fields = ['diagonal', 'name', 'color']
temp = []

for _ in range(0, len(laptops)):
    diagonal = laptops[_].find_all("span")[1].text.split()[0]
    name = (laptops[_].find_all("span")[1].text.split()[2],laptops[_].find_all("span")[1].text.split()[3])
    color = laptops[_].find_all("span")[1].text.split()[4]
    temp.append(diagonal)
    temp.append(name) 
    temp.append(color)

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    write = csv.writer(f, delimiter=';')
   # write.writerow(fields)
    write.writerows(temp)
