from bs4 import BeautifulSoup
import requests

page = 1
url = 'https://dorm.skku.edu/dorm_seoul/notice/notice_all.jsp?mode=list&board_no=78&pager.offset=' + str((page - 1) * 10)
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
tr = soup.select("table tbody tr")

tr_count = len(tr)
notice_count = 0

content = []
for i in range(tr_count):
    list = []

    td = tr[i].select("td")
    for k in range(len(td)):
        td_text = td[k].text.strip()
        if(td_text == '' and k == 0): notice_count += 1
        list.append(td_text)

    content.append(list)

print(content)