from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gptmodel import VideoMetadata

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Coucou api"}


@app.get("/videos")
async def converter(video_url):
    video_meta_data = VideoMetadata(video_url)
    return await video_meta_data.buildPayload()
