from selenium import webdriver

browser = webdriver.Firefox(executable_path='D:\\soft\\geckodriver-v0.18.0-win64\\geckodriver.exe')
browser.get('http://www.facebook.com')
emailElem = browser.find_element_by_id('email')
passElem = browser.find_element_by_id('pass')
submitIt = browser.find_element_by_id('u_0_r')
email_id = 'XXXXXXXXXXXXX'
password = 'XXXXXXXX'
status = 'Hie all'
emailElem.send_keys(email_id)
passElem.send_keys(password)
submitIt.click()
statusBox = browser.find_element_by_xpath("//*[@name='xhpc_message']")
statusBox.click()
statusBox.send_keys("Hie this is posted by bot")
