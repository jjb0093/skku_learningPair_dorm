from bs4 import BeautifulSoup
import requests

def getDorm(loc, page):

    url_Seoul = 'https://dorm.skku.edu/dorm_seoul/notice/notice_all.jsp?mode=list&board_no=78&pager.offset=' + str((page - 1) * 10)
    url_Suwon = 'https://dorm.skku.edu/dorm_suwon/notice/notice_all.jsp?mode=list&board_no=16&pager.offset=' + str((page - 1) * 10)
    if(loc == "Seoul"): url = url_Seoul
    elif(loc == "Suwon"): url = url_Suwon

    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    tr = soup.select("table tbody tr")

    tr_count = len(tr)
    notice_count = 0

    content = []
    for i in range(tr_count):
        list = []

        td = tr[i].select("td")
        list.append(td[0].text)
        for k in range(len(td)):
            td_text = td[k].text.strip()
            if(td_text == '' and k == 0): notice_count += 1
            if(k >= 1 and td_text != ''): list.append(td_text)
        list.append(td[2].find('a')["href"])

        content.append(list)

    return (notice_count, content)