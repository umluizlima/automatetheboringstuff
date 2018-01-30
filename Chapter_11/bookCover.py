from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_css_selector('body > div.container > div:nth-child(2) > div:nth-child(2) > a > img')
    print('Found <%s> element with that css selector!' %elem.tag_name)
except:
    print('Was not able to find an element with that name.')
browser.quit()
