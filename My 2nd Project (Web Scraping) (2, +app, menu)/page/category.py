from bs4 import BeautifulSoup
from locators.category_and_title_locator import CategoryLocator


class Category:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, "html.parser")

    def __repr__(self):
        return f"{self.find_category}"

    @property
    def category_row(self):
        return self.soup.findAll('div', {'class': 'row'})[3]

    @property
    def category_page(self):
        return self.category_row.findAll('div', {'class': 'col-md-6'})[1]

    @property
    def find_category(self):
        return [CategoryParser(c) for c in self.category_page.select(CategoryLocator.CLASS)]


class CategoryParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"{self.category}"

    @property
    def category(self):
        return self.parent.select_one(CategoryLocator.CATEGORY).string















