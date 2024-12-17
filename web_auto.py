from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

#set ip chrome optiopn
opts = Options()
opts.headless = True
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=opts)


# Define a list to hold search results
search_results = []

# Open Google and perform a search
try:
    #open google
    browser.get("https://www.google.com")
    # find the search box, enter a search term and submit
    search_box = browser.find_element("name", "q")
    search_box.send_keys("Python automation with Selenium")
    search_box.submit()
    # wait for result load
    time.sleep(3)


    # Retrieve the first 5 results
    results = browser.find_elements("css selector", "div.g")[:5]
    for i, result in enumerate(results, start=1):
        title = result.find_element("tag name", "h3").text
        url = result.find_element("tag name", "a").get_attribute("href")
        search_results.append({"title": title, "url": url})

finally:
    browser.quit()
