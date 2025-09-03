from numbers import Number
from typing import List
from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, HTMLResponse
from pydantic import BaseModel

app = FastAPI()
#PING fonctionnel
@app.get("/ping")
def ping():
    return {"message": "pong"}
#Q1
@app.get("/health")
def health():
    return Response(content="ok", media_type="text/plain", status_code=200)

phone_stocking = []
class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic
@app.post("/phones")

def phones(new_phones: List[Phone]):
    for phones in new_phones:
        phone_stocking.append(phones)
    return phone_stocking, Response(content="created", status_code=201)

