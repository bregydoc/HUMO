from bs4 import BeautifulSoup
html_doc = open('cursos.html', 'r')
soup = BeautifulSoup(html_doc, 'html.parser')

for el in soup.find_all('td'):
	if not el.string is None:
		print el.string.replace('entitled', '')