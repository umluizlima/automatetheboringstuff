# linkVerification - Given an URL, download every linked page on the page and flags any page
# that was not found

import bs4, requests

url = input('Enter URL: ')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')
for link in links:
    try:
        if link.attrs['href'].startswith('/'):
            res = requests.get(url + link.attrs['href'])    
        else:
            res = requests.get(link.attrs['href'])
        res.raise_for_status()
        print('Found:', res.url)
    except:
        if res.status_code == 404:
            print('Not found:', res.url)
