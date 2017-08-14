from selenium import webdriver

browser = webdriver.Firefox(executable_path='D:\\soft\\geckodriver-v0.18.0-win64\\geckodriver.exe')
browser.get('http://www.facebook.com')
emailElem = browser.find_element_by_id('email')
passElem = browser.find_element_by_id('pass')
submitIt = browser.find_element_by_id('u_0_r')
email_id = 'alpit_anand@yahoo.co.in'
password = 'Alpit@123'
status = 'Hie all'
emailElem.send_keys(email_id)
passElem.send_keys(password)
submitIt.click()
statusBox = browser.find_element_by_xpath("//*[@name='xhpc_message']")
statusBox.click()
statusBox.send_keys("Hie this is posted by bot")
post_it = browser.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
post_it.click()
