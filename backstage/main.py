from fastapi import FastAPI
from fastapi import APIRouter
import data

app = FastAPI()
v1Router = APIRouter(prefix="/v1", tags=["v1"])

@v1Router.get('/websites/all')
def getAllWebsites():
    return data.getWebsites()

@v1Router.post('/website/new')
def createWebsite(website: data.Website):
    data.addWebsite(website)

app.include_router(v1Router)