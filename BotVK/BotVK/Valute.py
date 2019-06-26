import requests
import bs4
from datetime import datetime
url="http://www.cbr.ru/scripts/XML_daily.asp"
today=datetime.now().strftime("%d/%m/%Y")
payload={"date_req":today}
response=requests.get(url,params=payload)
soup=bs4.BeautifulSoup(response.content, "lxml")
def get_course(id):
    valute= soup.find("valute",{"id":id})
    nominal=valute.nominal 
    name=nominal.next_sibling
    value=valute.value
    return "За {} {} дают {}руб.".format(nominal.text, name.text, value.text)


