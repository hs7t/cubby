# type: ignore      // pylance doesn't like dataset

import dataset
DATABASE_URL = "sqlite:///_data.db"
db = dataset.connect

websites = db['websites']

def getWebsites():
    return websites.all()

