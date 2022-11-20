from bs4 import BeautifulSoup
import requests
from datetime import date

def getFood(loc):

    today = date.today().strftime("%Y-%m-%d")

    url_Seoul = "https://dorm.skku.edu/_custom/skku/_common/board/schedule_menu/food_menu_page.jsp?date=" + today + "&board_no=117&lng=ko#a"
    url_Suwon = "https://dorm.skku.edu/_custom/skku/_common/board/schedule_menu/food_menu_page.jsp?date=" + today + "&board_no=61&lng=ko#a"
    if (loc == "Seoul"): url = url_Seoul
    elif (loc == "Suwon"): url = url_Suwon

    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    foodList = soup.find_all('div', class_="board-foodlist-box")

    content = []
    for foodLists in foodList:
        list = {}

        span = foodLists.select("ul li span")
        p = foodLists.select("ul li p")
        for i in range(len(span)):
            list[span[i].text] = p[i].text[12:]

        content.append(list)

    return content