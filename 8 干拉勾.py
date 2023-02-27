from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

opt = Options()
opt.binary_location = 'C:/Program Files/RunningCheeseFirefox/Firefox/firefox.exe'
web = Firefox(options=opt)
web.get('https://www.lagou.com')
el = web.find_element('xpath','//*[@id="changeCityBox"]/p[1]/a')
time.sleep(1)
el.click()
time.sleep(1)
web.find_element('xpath','//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(1)
li_list = web.find_elements('xpath','/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div')
for li in li_list:
    job = li.find_element('xpath','./div[1]/div[1]/div[1]/a').text
    price = li.find_element('xpath','./div[1]/div[1]/div[2]/span').text
    print(job,price)