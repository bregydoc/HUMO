from selenium import webdriver
import time
 
driver = webdriver.PhantomJS()
driver.get('http://core.utecsup.com/UTEC-Web')
 
html = driver.page_source
filet = open('test.txt', 'w+')
filet.write(html.encode('utf8'))
filet.close()