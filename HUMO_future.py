# 2nd Way: EXPORT THE NOTES
downloadGrades = 'http://core.utecsup.com/UTEC-Web/action/exportarconsultanotasactuales'

session = requests.Session()
cookies = driver.get_cookies()

for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])
response = session.get(downloadGrades)
print type(response.content)
filename = 'gradesss.xls'
with open(filename, mode='wb') as localfile:
	localfile.write(response.content)
action.send_keys(Keys.ENTER)
action.send_keys('password')
action.send_keys(Keys.ENTER)
