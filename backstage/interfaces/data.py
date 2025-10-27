# type: ignore      // pylance doesn't like dataset

import json
import dataset
import os
from pydantic import BaseModel
from typing import List

os.environ["DATABASE_URL"] = "sqlite:///_data.db"
db = dataset.connect()

websites = db['websites']

def getWebsites():
    """
    Returns all websites on the database.
    """
    results = list(websites.all())

    for site in results:
        # Unjsonify lists from DB
        if 'mapCoordinates' in site and isinstance(site['mapCoordinates'], str):
            site['mapCoordinates'] = json.loads(site['mapCoordinates'])
        if 'directions' in site and isinstance(site['directions'], str):
            site['directions'] = json.loads(site['directions'])
    return results


class Website(BaseModel):
    cubbyId: str
    name: str
    url: str
    address: str
    mapCoordinates: List[int]
    review: str
    directions: List[str]

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
        if len(list(table.find(cubbyId=website.cubbyId))) == 0:
            data = website.model_dump()

            # DB doesn't support lists; jsonify them
            data['mapCoordinates'] = json.dumps(data['mapCoordinates'])
            data['directions'] = json.dumps(data['directions'])

            table.insert(data)
        else:
            print(list(table.find(cubbyId=website.cubbyId)))
            raise DuplicateError('cubbyId already registered')
        
class NonExistentError(Exception):
    """Raised when there is no entry to update."""

    def __init__(self, message):
        super().__init__(message)
        self.error_code = 10

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"

def deleteWebsite(cubbyId: str): 
    with db:
        table = db['websites']
        table.delete(cubbyId=cubbyId)

def updateWebsite(website: Website):
    with db:
        table = db['websites']
        if len(list(table.find(cubbyId=website.cubbyId))) > 0:
            data = website.model_dump()
            data['mapCoordinates'] = json.dumps(data['mapCoordinates'])
            table.update(data, ['cubbyId'])
        else:
            raise NonExistentError('cubbyId not found; nothing to update')