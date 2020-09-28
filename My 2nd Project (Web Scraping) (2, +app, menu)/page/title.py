from locators.category_and_title_locator import TitleLocator
from bs4 import BeautifulSoup


class TitleParser:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def __repr__(self):
        return f"{self.title_class}"

    @classmethod
    def title(cls, parent):
        return parent.select_one(TitleLocator.TITLE).string

    @property
    def title_class(self):
        return [self.title(t) for t in
                self.soup.select(TitleLocator.CLASS)]




