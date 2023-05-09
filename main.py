from fastapi import FastAPI
from .gptmodel import get_transcription

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Coucou api"}


@app.get("/video/{url}")
async def converter(url):
    textFinal = get_transcription()

    title = getTitleFromText()


    return get_transcription(url)