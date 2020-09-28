import requests
from selenium import webdriver

from page.category import Category
from page.title import TitleParser
from page.jobs_page import JobsPage

content = requests.get('https://www.monster.com/jobs').content
page = Category(content)

category = page.find_category

for n, c in enumerate(category):
    print(n, c)

category_choice = int(input('Enter a number for category you want to look at: '))

selected_category = category[category_choice]

chrome = webdriver.Chrome(executable_path="C:/Users/Bunyod/Downloads/chromedriver_win32/chromedriver")
chrome.get("http://monster.com/jobs")

chrome.find_element_by_link_text(str(selected_category)).click()
category_link = chrome.current_url

title_content = requests.get(category_link).content
title_page = TitleParser(title_content)

title = title_page.title_class

for n, t in enumerate(title_page.title_class):
    print(n, t)

title_choice = int(input('Enter a number for a title you want to look at: '))
selected_title = title[title_choice]

chrome.find_element_by_link_text(str(selected_title)).click()
title_link = chrome.current_url

jobs_content = requests.get(title_link).content
jobs_page = JobsPage(jobs_content)


jobs = jobs_page.jobs

for job in jobs:
    print(job)












