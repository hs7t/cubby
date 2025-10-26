# type: ignore      // pylance doesn't like dataset

import dataset
from pydantic import BaseModel

DATABASE_URL = "sqlite:///_data.db"
db = dataset.connect()

websites = db['websites']

def getWebsites():
    """
    Returns all websites on the database.
    """
    return websites.all()

class Website(BaseModel):
    cubbyId: str
    name: str
    url: str

def addWebsite(website: Website):
    """
    Creates an entry in the database for a new Website.
    """
    with dataset.connect() as tx:
        tx['websites'].insert(website)