# type: ignore      // pylance doesn't like dataset

import dataset
import os
from pydantic import BaseModel

os.environ["DATABASE_URL"] = "sqlite:///_data.db"
db = dataset.connect()

websites = db['websites']

def getWebsites():
    """
    Returns all websites on the database.
    """
    return list(websites.all())

class Website(BaseModel):
    cubbyId: str
    name: str
    url: str
    address: str

class DuplicateError(Exception):
    """Raised when there's a duplicate entry."""

    def __init__(self, message):
        super().__init__(message)
        self.error_code = 10

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

def addWebsite(website: Website):
    """
    Creates an entry in the database for a new Website.
    """
    with db:
        table = db['websites']
        if not (table.find(cubbyId=website.cubbyId)):
            table.insert(website.model_dump())
        else:
            raise DuplicateError('cubbyId already registered')