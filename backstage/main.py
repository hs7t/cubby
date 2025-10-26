from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
v1Router = APIRouter(prefix="/v1", tags=["v1"])



app.include_router(v1Router)