from locators.jobs_locators import JobsLocators


class JobsParser:
    def __init__(self, parent):
        self.parent = parent
    
    def __repr__(self):
        return f"{self.title} at {self.company}, location: {self.location}, posted date: {self.date}"
    
    @property
    def title(self):
        return self.parent.select_one(JobsLocators.TITLE).string

    @property
    def company(self):
        try:
            return self.parent.select_one(JobsLocators.COMPANY).string
        except:
            return self.parent.select_one(JobsLocators.COMPANY1).string

    @property
    def location(self):
        try:
            return self.parent.select_one(JobsLocators.LOCATION).string
        except:
            return self.parent.select_one(JobsLocators.LOCATION1).string

    @property
    def date(self):
        return self.parent.select_one(JobsLocators.DATE).string
