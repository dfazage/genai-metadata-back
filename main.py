from fastapi import FastAPI
from gptmodel import VideoMetadata

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Coucou api"}


@app.get("/videos")
async def converter(video_url):
    video_meta_data = VideoMetadata(video_url)
    return video_meta_data.buildPayload()
