import requests,csv
from bs4 import BeautifulSoup
user_agent='''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'''
req=requests.get('https://html.com/tables/',headers={'User-Agent': user_agent}).text
soup=BeautifulSoup(req, "html5lib")
tables=soup.findAll('table')
with open('tables.csv','w',newline='') as f:
    csv_writer=csv.writer(f)
    for table in tables:
        for row in table.findAll('tr'):
            cell_list=[]
            for cell in row.findAll('th'):
                cell_list.append(cell.get_text().strip())
            for cell in row.findAll('td'):
                cell_list.append(cell.get_text().strip())
            csv_writer.writerow(cell_list)
        csv_writer.writerow([])