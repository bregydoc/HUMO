import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains
import requests
import json

jsonPath = 'credentials.json'

jo = open(jsonPath, 'r')
r_credentials = jo.read()
credentials = json.loads(rawData)

email = credentials['email']
password = credentialss['password']
epoch = credentialss['cycle']

driver= webdriver.PhantomJS()
# driver= webdriver.Chrome("E:\QA\Resource\WEBDRIVER\chromedriverserver\chromedriver.exe")
driver.get("https://accounts.google.com/signin/oauth/identifier?client_id=106735915676-jgh1pts7v6lss7l5cqdi472b7lfn78lc.apps.googleusercontent.com&as=30faa23d961e91a2&destination=http%3A%2F%2Fcore.utecsup.com&approval_state=!ChRzZFh1OElpYk1sWVowWjlZWkFjShIfZzV1MlhBR1dBazRRTVBCQmxsdzFRaXQ1WXRXWUJCWQ%E2%88%99ACThZt4AAAAAWjDR120lGDiKRrPa-3azWbjS8pUz5phc&passive=1209600&oauth=1&sarp=1&scc=1&xsrfsig=AHgIfE80PelFvRLLA6vsfTBREFazdpG1lw&flowName=GeneralOAuthFlow")
time.sleep(3)

putEmail = ActionChains(driver)
putEmail.send_keys(email)
putEmail.perform()

nextEnter = ActionChains(driver)
nextEnter.send_keys(Keys.ENTER)
nextEnter.perform()
time.sleep(3)

putPassword = ActionChains(driver)
putPassword.send_keys(password)
putPassword.perform()

nextEnter = ActionChains(driver)
nextEnter.send_keys(Keys.ENTER)
nextEnter.perform()

time.sleep(10)

# driver.get('http://core.utecsup.com/UTEC-Web/Principal.jsp#consultaNotasPA:7740666')

# time.sleep(10)

driver.get_screenshot_as_file('lastscreen.png')


el = driver.find_element_by_id('nav-bar')

inter = el.find_elements_by_tag_name('li')[1]
ActionChains(driver).move_to_element(inter).perform()

opts = inter.find_element_by_class_name('subs')

opts.find_elements_by_tag_name('li')[0].click()

driver.get_screenshot_as_file('middlescreen.png')

time.sleep(5)

el = driver.find_element_by_class_name('cont-tit-sistema')
ActionChains(driver).move_to_element(el).perform()

time.sleep(1)

el = driver.find_element_by_class_name('gwt-ListBox')
for option in el.find_elements_by_tag_name('option'):
    if option.text == epoch:
        option.click() # select() in earlier versions of webdriver
        break

time.sleep(60)

# 1st Way: WEB SCRAPPING
courses = driver.find_element_by_class_name('contenedorFormulario')
print courses

for c in courses.find_elements_by_class_name('cursoNotasAcordionPanel'):
	m = c.find_element_by_class_name('cursoNotasCabecera')
	print 'clicking', c
	m.click()
	time.sleep(2)

driver.get_screenshot_as_file('screen.png')


data = courses.get_attribute('innerHTML')
finalfile = open('raw.html', 'wb')

finalfile.write(data.encode('utf-8'))
finalfile.close()
