# type: ignore      // pylance doesn't like dataset

import dataset
from pydantic import BaseModel

DATABASE_URL = "sqlite:///_data.db"
db = dataset.connect

websites = db['websites']

def getWebsites():
    return websites.all()

class Website(BaseModel):
    id: str
    name: str
    url: str

def addWebsite(website: Website):
    with dataset.connect() as tx:
        tx['websites'].insert(website)