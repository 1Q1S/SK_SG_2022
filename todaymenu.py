from selenium import webdriver
from selenium.webdriver.common.keys import Keys                        
import time
from datetime import datetime

url = 'http://massmail.sk.com/menu/print.aspx?rcode=no11'
driver = webdriver.Chrome('.\chromedriver.exe')
driver.get(url)
time.sleep(5)

news_titles = driver.find_elements_by_css_selector("#form1 > div:nth-child(3) > table > tbody > tr:nth-child(1) > th")

time.sleep(2)

for i in news_titles:
    a=i.text()
    print(a)


# now = datetime.now()
# now.strftime("%Y년 %m월 %d일")   
