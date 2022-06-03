from selenium import webdriver
from selenium.webdriver.common.keys import Keys                        
import time
from datetime import datetime

def fomating_date(date):
    day = text[-4:]
    text = text.removesuffix(day)
    text=text.replace('년',',').replace('월',',').replace('일',',').replace(' ','')
    text=text.split(',')

    year=text[0]
    month=text[1].zfill(2)
    days=text[2].zfill(2)

    return year, month, days, day


url = 'http://massmail.sk.com/menu/print.aspx?rcode=no11'
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
#driver = webdriver.Chrome('.\chromedriver.exe')
browser.get(url)
time.sleep(5)

for i in range(1,8):
    news_titles = browser.find_elements_by_css_selector("#form1 > div:nth-child(3) > table > tbody > tr:nth-child(%d) > th"%(i))
    news_text = [i.text for i in news_titles]
    time.sleep(1)
    for text in news_text:
        year, month, days,day = fomating_date(text)
        
        print(year+'년'+month+'월'+days+'일'+day)



# now = datetime.now()
# now.strftime("%Y년 %m월 %d일")   
