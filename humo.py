import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains
import requests
import json

jsonPath = 'credentials.json'

jo = open(jsonPath, 'r')
r_credentials = jo.read()
credentials = json.loads(r_credentials)

email = credentials['email']
password = credentials['password']
epoch = credentials['cycle']

driver= webdriver.PhantomJS()
# driver= webdriver.Chrome("E:\QA\Resource\WEBDRIVER\chromedriverserver\chromedriver.exe")
driver.get("http://core.utecsup.com/UTEC-Web")

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

# 2nd Way: EXPORT THE NOTES
# downloadGrades = 'http://core.utecsup.com/UTEC-Web/action/exportarconsultanotasactuales'

# session = requests.Session()
# cookies = driver.get_cookies()

# for cookie in cookies:
#     session.cookies.set(cookie['name'], cookie['value'])
# response = session.get(downloadGrades)
# print type(response.content)
# filename = 'gradesss.xls'
# with open(filename, mode='wb') as localfile:
# 	localfile.write(response.content)
# action.send_keys(Keys.ENTER)
# action.send_keys('password')
# action.send_keys(Keys.ENTER)
