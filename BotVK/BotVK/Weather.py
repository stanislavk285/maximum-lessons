import requests
import bs4
def get_content(city):
    url="https://yandex.ru/pogoda/"+city
    response=requests.get(url)
    soup=bs4.BeautifulSoup(response.content,"lxml")
    return soup
def get_temp(soup):
    result=soup.find("span",{"class":"temp__value"})
    return result.text
def get_condition(soup):
    result=soup.find("div",{"class":"link__condition"})
    return result.text
def get_wind(soup):
    result=soup.find("dl",{"class":"term term_orient_v fact__wind-speed"})
    return result.text
def get_humidity(soup):
    result=soup.find("dl",{"class":"term term_orient_v fact__humidity"})
    return result.text
def get_pressure(soup):
    result=soup.find("dl",{"class":"term term_orient_v fact__pressure"})
    return result.text
def main(city):
    soup=get_content(city)
    content=get_content(city)
    return"Погода в Москве:""\n"+"Температура "+get_temp(soup)+"°","\n"+get_condition(soup),"\n"+"Скорость ветра "+get_wind(soup),"\n""Влажность "+get_humidity(soup),"\n""Давление "+get_pressure(soup),"\n"

