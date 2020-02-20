from selenium import webdriver
import schedule
import time
import datetime
import sys

driver = webdriver.Firefox()
driver.get("http://mobile.njit.edu/parking/")
sys.stdout = open('master.txt', 'a')


def scrub():
    login_form = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[2]/div/div[2]')
    print(str(datetime.datetime.now()) + '  ' + login_form.text)
    # Import Module for Website X


schedule.every(1).seconds.do(scrub)

while 1:
    schedule.run_pending()
    time.sleep(0)
