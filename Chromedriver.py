from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.get('https://discord.com/channels/881507710993063936/881507710993063939')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/section/div[2]/button[2]').click() 
time.sleep(3000)