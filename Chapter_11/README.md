https://automatetheboringstuff.com/chapter11/

1. The webbrowser module allows you to open web pages on your default browser. Requests downloads whole web pages to be stored locally or to be thoroughly explored with BeautifulSoup. Selenium runs a real browser window and takes commands to emulate user's interaction.
2. The object returned by requests.get() is of the 'requests.models.Response' type. To access the downloaded content as a string value you must access the Response's text attribute.
3. The method that checks if the download worked is Response.raise_for_status().
4. To get the HTTP status code of a Requests response you can access the status_code attribute.
5. By writing chunks of its content using the iter_content method and regular file writing.
6. F12 will open a browser's developer tools.
7. Inspecting elements will allow you to view the HTML of a specific element on a web page.
8. The CSS selector string that would find the element with an id attribute of main is: soup.select('#main')
9. The CSS selector string that would find the elements with a CSS class of highlight is: soup.select('.highlight')
10. The CSS selector string that would find all the <div> elements inside another <div> element is: soup.select('div div')
11. The CSS selector string that would find the <button> element with a value attribute set to favorite is: soup.select('button[value="favorite"]')
12. To get a string from a Tag object you call the text attribute.
13. To store all the attributes of a Beautiful Soup Tag object in a variable named linkElem: linkElem = bs4.element.Tag.attrs
14. To properly import the selenium module: from selenium import webdriver
15. The find_element_* will return the first occurence of given search argument, while find_elements_* returns a list with all its occurences.
16. A WebElement object have the .click() and .send_keys() methods for simulating clicks and keyboards keys.
17. Calling .click() on the Submit button's WebElement.
18. browser.forward(), browser.back(), browser.refresh()