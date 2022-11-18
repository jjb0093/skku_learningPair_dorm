import requests
import xml.etree.ElementTree as elt
from datetime import datetime, timedelta, date
import warnings

warnings.filterwarnings('ignore')

def getWeather(loc):
    now = datetime.now()

    serviceKey = "ya3j1ObxHL8p6TfZnHJZ9uGlUCexBZIbhJrzI%2FG9TYvVn3MwnQdL4j%2FROSg%2BJy2a4M%2F8etQYRfZMnqoeDPyjOw%3D%3D"
    numOfRows = 84
    pageNum = 1
    if(loc == "Seoul"):
        nx = 60
        ny = 127
    elif(loc == "Suwon"):
        nx = 60
        ny = 121

    baseTime = '2300'
    baseDate = (date.today() - timedelta(1)).strftime("%Y%m%d")
    skipCount = 0

    if(now.hour >= 3):
        baseDate = now.strftime("%Y%m%d")
        if((now.hour - 2) % 3 == 0):
            baseTime = str((now - timedelta(hours = 3)).strftime("%H00"))
            skipCount = 3
        else:
            baseTime = str((now - timedelta(hours = ((now.hour - 2) % 3))).strftime("%H00"))
            skipCount = int((now.hour - 2) % 3)
    else: skipCount = int(now.hour) + 1

    numOfRows += (skipCount + 1) * 12

    nowHour = now.hour

    url = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?'
    url += 'serviceKey=' + str(serviceKey)
    url += '&pageNo=' + str(pageNum)
    url += '&numOfRows=' + str(numOfRows)
    url += '&dataType=XML'
    url += '&base_date=' + str(baseDate)
    url += '&base_time=' + str(baseTime)
    url += '&nx=' + str(nx)
    url += '&ny=' + str(ny)
    print(url)

    response = requests.get(url, verify = False)
    data = elt.fromstring(response.text)

    weatherDetails = []
    rotate_count = 0
    plus_count = 0

    start = (skipCount - 1) * 12
    for i in range(7):
        details = {}

        details["dayTime"] = str(data[1][1][start + (rotate_count * 12) + plus_count][3].text) + '-' + str(data[1][1][start + (rotate_count * 12) + plus_count][4].text)
        details["sky"] = str(data[1][1][5 + start + (rotate_count * 12) + plus_count][5].text)
        details["tmp"] = str(data[1][1][0 + start + (rotate_count * 12) + plus_count][5].text)
        details["reh"] = str(data[1][1][10 + start + (rotate_count * 12) + plus_count][5].text)
        details["pop"] = str(data[1][1][7 + start + (rotate_count * 12) + plus_count][5].text)
        details["pty"] = str(data[1][1][6 + start + (rotate_count * 12) + plus_count][5].text)

        rotate_count += 1

        if (nowHour == 23):
            nowHour = 0
        else:
            nowHour += 1
        if (nowHour == 7 or nowHour == 16): plus_count += 1

        weatherDetails.append(details)
    weatherDetails.append(baseDate + "-"  + baseTime)

    return weatherDetails

def getNowWeather(loc):
    now = datetime.now()

    serviceKey = "ya3j1ObxHL8p6TfZnHJZ9uGlUCexBZIbhJrzI%2FG9TYvVn3MwnQdL4j%2FROSg%2BJy2a4M%2F8etQYRfZMnqoeDPyjOw%3D%3D"
    numOfRows = 12
    pageNum = 1
    if (loc == "Seoul"):
        nx = 60
        ny = 127
    elif (loc == "Suwon"):
        nx = 60
        ny = 121

    baseTime = '2300'
    baseDate = (date.today() - timedelta(1)).strftime("%Y%m%d")

    if (now.hour >= 3):
        baseDate = now.strftime("%Y%m%d")
        if ((now.hour - 2) % 3 == 0):
            baseTime = str((now - timedelta(hours=3)).strftime("%H00"))
            pageNum = 3
        else:
            baseTime = str((now - timedelta(hours=((now.hour - 2) % 3))).strftime("%H00"))
            pageNum = int((now.hour - 2) % 3)
    else: pageNum = int(now.hour) + 1

    nowHour = now.hour

    weatherDetails = []
    url = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?'
    url += 'serviceKey=' + str(serviceKey)
    url += '&pageNo=' + str(pageNum)
    url += '&numOfRows=' + str(numOfRows)
    url += '&dataType=XML'
    url += '&base_date=' + str(baseDate)
    url += '&base_time=' + str(baseTime)
    url += '&nx=' + str(nx)
    url += '&ny=' + str(ny)

    response = requests.get(url, verify=False)
    data = elt.fromstring(response.text)

    details = {}
    details["dayTime"] = str(data[1][1][5][3].text) + '-' + str(data[1][1][5][4].text)
    details["sky"] = data[1][1][5][5].text
    details["tmp"] = data[1][1][0][5].text
    #details["reh"] = data[1][1][10][5].text
    #details["pop"] = data[1][1][7][5].text
    details["pty"] = data[1][1][6][5].text

    weatherDetails.append(details)

    return weatherDetails