# play2048 - a program that opens the game and keep sending up, right,
# down and left keystrokes to automatically play the game.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
html = browser.find_element_by_tag_name('html')
while True:
    html.send_keys(Keys.UP)
    sleep(0.1)
    html.send_keys(Keys.RIGHT)
    sleep(0.1)
    html.send_keys(Keys.DOWN)
    sleep(0.1)
    html.send_keys(Keys.LEFT)
    sleep(0.1)
