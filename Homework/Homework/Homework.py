import requests
import bs4
import random
import tkinter
from datetime import datetime
url="https://myfin.by/crypto-rates/bitcoin-rub"
today = datetime.now().strftime("%d/%m/%Y")
payload = {"data_req": today}
response = requests.get(url, params=payload)
 
soup = bs4.BeautifulSoup(response.content, "lxml")
def get_value(soup):
    result=soup.find("div",{"class":"birzha_info_head_rates"})
    return "За 1 Биткоин дают {}".format(result.text)
window=tkinter.Tk()
window.geometry("400x350")
window.title("Курс биткоина")
label=tkinter.Label(text="Курс биткоина",font="Arial 22")
label.place(y=25,x=100)
course_info=tkinter.Label(text="Курс на {}".format(today.replace("/",".")),font="Arial 18")
course_info.place(x=90,y=100)
bit=tkinter.Label(text=get_value(soup),font="arial 22")
bit.place(x=50,y=150)
window.mainloop()

