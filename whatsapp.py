from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Firefox(executable_path='D:\\soft\\geckodriver-v0.18.0-win64\\geckodriver.exe')
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 6000)
friendName = '"Replace by friends name"'
x_path = "//span[contains(@title," + friendName + ")]"
friend = wait.until(EC.presence_of_element_located((
    By.XPATH, x_path)))
friend.click()
x_path2 = "//div[@class='input'][@dir='auto'][@data-tab='1']"
inputText = wait.until(EC.presence_of_element_located((
    By.XPATH, x_path2)))
for i in range(200):
    inputText.send_keys("Replace with msg"+Keys.ENTER)
    print(i)




