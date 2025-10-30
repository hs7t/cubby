from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import HTTPException
import interfaces.data

app = FastAPI()
v1Router = APIRouter(prefix="/v1", tags=["v1"])

@v1Router.get('/websites/all')
def getAllWebsites():
    return interfaces.data.getWebsites()

# @v1Router.post('/website/new')
def createWebsite(website: interfaces.data.Website):
    try:
        interfaces.data.addWebsite(website)
    except interfaces.data.DuplicateError:
        raise HTTPException(409, "This website already exists.")

# @v1Router.post('/website/amend')
def amendWebsite(website: interfaces.data.Website):
    try:
        interfaces.data.updateWebsite(website)
    except interfaces.data.NonExistentError:
        raise HTTPException(404, "Unable to find this website.")

# @v1Router.post('/website/delete')
def deleteWebsite(cubbyId: str):
    interfaces.data.deleteWebsite(cubbyId)

app.include_router(v1Router)