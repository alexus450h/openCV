import bs4

with open('index.html','r') as html_file:
    content=html_file.read()

    soup=bs4.BeautifulSoup(content,features='html.parser')
    res=soup.find_all('div',class_='col-5 ml-4 pl-4')
    for text in res:
        print(text.a.text)