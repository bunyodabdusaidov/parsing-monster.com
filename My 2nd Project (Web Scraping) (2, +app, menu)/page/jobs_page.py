from locators.jobs_page_locators import JobsPageLocators
from parsers.jobs_parser import JobsParser
from bs4 import BeautifulSoup


class JobsPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def jobs(self):
        return [JobsParser(j) for j in self.soup.select(JobsPageLocators.JOBS)]

