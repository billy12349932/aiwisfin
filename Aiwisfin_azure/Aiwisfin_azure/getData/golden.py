from bs4 import BeautifulSoup
import requests


def getGolden():
    res = requests.get('https://www.goldlegend.com/')
    soup = BeautifulSoup(res.text,"html.parser")
    tables = soup.find_all(class_ = "d-inline-block")
    return "國際黃金價格為"+tables[0].text.strip()
   