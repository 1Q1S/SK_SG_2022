from selenium import webdriver
from selenium.webdriver.common.keys import Keys                        
import time
from time import strftime
from datetime import datetime

def today_time():
    import time
    from time import strftime

    tm = time.localtime(time.time())
    
    date=strftime('%Y년 %m월 %d일', tm)
    time=strftime('%H:%M:%S', tm)

    return date, time

def fomating_date(date):
    day = date[-4:].replace(' ','')
    date = date.replace(day,'')
    date=date.replace('년',',').replace('월',',').replace('일',',').replace(' ','')
    date=date.split(',')

    year=date[0]
    month=date[1].zfill(2)
    days=date[2].zfill(2)

    return year, month, days, day


url = 'http://massmail.sk.com/menu/print.aspx?rcode=no11'
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
#driver = webdriver.Chrome('.\chromedriver.exe')
browser.get(url)
time.sleep(5)

for i in range(1,8):
    news_titles = browser.find_elements_by_css_selector("#form1 > div:nth-child(3) > table > tbody > tr:nth-child(%d) > th"%(i))
    menu=browser.find_elements_by_xpath('//*[@id="form1"]/div[3]/table/tbody/tr[%d]/td[1]/ul/li'%(i))
    news_text = [i.text for i in news_titles]
    menu_text= [i.text for i in menu]
    time.sleep(1)
    for text in news_text:
        year, month, days,day = fomating_date(text)    
        date = year+'년 '+month+'월 '+days+'일'
        
        to_date,to_time=today_time()    
    
        if to_date == date:
            a=date
            b=menu_text
            
#form1 > div:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(2)

#form1 > div:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(2) > ul > li:nth-child(1)
#form1 > div:nth-child(3) > table > tbody > tr:nth-child(2) > td:nth-child(2) > ul
#form1 > div:nth-child(3) > table > tbody > tr:nth-child(2) > td:nth-child(2) > ul > li:nth-child(1)
#form1 > div:nth-child(3) > table > tbody > tr:nth-child(2) > td:nth-child(2) > ul > li:nth-child(1)
# now = datetime.now()
# now.strftime("%Y년 %m월 %d일")   
# //*[@id="form1"]/div[3]/table/tbody/tr[2]/td[1]/ul
# //*[@id="form1"]/div[3]/table/tbody/tr[1]/td[1]/ul

from selenium.webdriver.common.keys import Keys                        
from selenium import webdriver
import time
from time import strftime
from datetime import datetime

def today_time():
    import time
    from time import strftime

    tm = time.localtime(time.time())
    
    date=strftime('%Y년 %m월 %d일', tm)
    time=strftime('%H:%M:%S', tm)

#     return date, time

# def fomating_date(date):
#     day = date[-4:].replace(' ','')
#     date = date.replace(day,'')
#     date=date.replace('년',',').replace('월',',').replace('일',',').replace(' ','')
#     date=date.split(',')

#     year=date[0]
#     month=date[1].zfill(2)
#     days=date[2].zfill(2)

#     return year, month, days, day

'''20220604'''
# url = 'http://massmail.sk.com/menu/print.aspx?rcode=no11'
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument('--headless')
# browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# #driver = webdriver.Chrome('.\chromedriver.exe')
# browser.get(url)
# time.sleep(5)

# for i in range(1,8):
#     news_titles = browser.find_elements_by_css_selector("#form1 > div:nth-child(3) > table > tbody > tr:nth-child(%d) > th"%(i))
#     menu=browser.find_elements_by_xpath('//*[@id="form1"]/div[3]/table/tbody/tr[%d]/td[1]/ul/li'%(i))
#     news_text = [i.text for i in news_titles]
#     menu_text= [i.text for i in menu]
#     time.sleep(1)
#     for text in news_text:
#         year, month, days,day = fomating_date(text)    
#         date = year+'년 '+month+'월 '+days+'일'
        
#         to_date,to_time=today_time()    
    
#         if to_date == date:
#             print(date)
#             print('오늘의 메뉴:',end='')
#             print(menu_text)