try:
    from googlesearch import search
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing module")

print('Enter the movie')
movie = input()
query = movie + 'box office mojo'
for j in search(query, tld='com', lang='en', num=1, stop=1, pause=2):
    link = j
#print(link)
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

#titletable = soup.find(id="body")
#title = titletable.select("table tbody tr td table tbody tr td")
#title = title[0].get_text()

grosstable = soup.find(class_="mp_box_content")
gross = grosstable.select("tr td b")
grossDomestic = gross[0].get_text()
grossNum = gross[1].get_text()

#print(title)
print(movie.title())
print(grossDomestic)
print(grossNum)

#def titleCase(str):
#    str = str.title()
#return