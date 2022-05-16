from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 


chrome_driver_path = "/opt/homebrew/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get('https://orteil.dashnet.org/cookieclicker/')
cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')




while True :
    cookie.click()





