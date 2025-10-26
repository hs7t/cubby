from fastapi import FastAPI
from fastapi import APIRouter
import interfaces.data

app = FastAPI()
v1Router = APIRouter(prefix="/v1", tags=["v1"])

@v1Router.get('/websites/all')
def getAllWebsites():
    return interfaces.data.getWebsites()

@v1Router.post('/website/new')
def createWebsite(website: interfaces.data.Website):
    interfaces.data.addWebsite(website)

app.include_router(v1Router)