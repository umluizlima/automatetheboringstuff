#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import bs4, os, requests

search = input('Enter search term: ')
url = 'https://imgur.com/search?q=' + '+'.join(search.split(' '))
os.makedirs('imgur', exist_ok=True)  # store comics in ./imgur

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

imgElems = soup.select('a[class="image-list-link"]')
numOpen = min(10, len(imgElems))

for i in range(numOpen):
    imgPage = requests.get('https://imgur.com' + imgElems[i].attrs['href'])
    imgPage.raise_for_status()
    imgSoup = bs4.BeautifulSoup(imgPage.text, 'html.parser')
    
    img = imgSoup.select('div[class="post-image"]')
    #img = img.select('img')
    imgFile = open(os.path.join('imgur', img[0].contents[1].attrs['src'].split('/')[-1]), 'wb')
    for chunk in img. iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()
