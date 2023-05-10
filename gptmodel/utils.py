import os
from pytube import YouTube
from collections import namedtuple
from dotenv import load_dotenv
import openai
import ast

load_dotenv()

MODEL = "gpt-3.5-turbo"

DEFAULT_PATH = "temp"

IMG_SIZE = "256x256"

MAX_TOKENS = 2000

MAX_CHAR = 10400

openai.api_key = os.environ["OPENAI_API_KEY"]

prompt_config = namedtuple(
    "prompt_config", ["system_prompt", "prompt"], defaults=["", ""]
)


def message_dict(role, content):
    return {"role": role, "content": content}


def get_answer_from_model(system_prompt, prompt, model=MODEL):
    openai_object = openai.ChatCompletion.create(
        model=model,
        messages=[
            message_dict("system", system_prompt),
            message_dict("user", prompt),
        ],
    )
    return openai_object["choices"][0]["message"]["content"]


async def aget_answer_from_model(system_prompt, prompt, model=MODEL):
    openai_object = await openai.ChatCompletion.acreate(
        model=model,
        messages=[
            message_dict("system", system_prompt),
            message_dict("user", prompt),
        ],
    )
    return openai_object["choices"][0]["message"]["content"]


def get_image_from_model(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size=IMG_SIZE)
    return response["data"][0]["url"]


async def aget_image_from_model(prompt):
    response = await openai.Image.acreate(prompt=prompt, n=1, size=IMG_SIZE)
    return response["data"][0]["url"]


def convert_mp3(video_url):
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=DEFAULT_PATH)

    base, __ = os.path.splitext(out_file)
    new_file = base.replace(" ", "-") + ".mp3"
    os.rename(out_file, new_file)

    print(f"{base} has been successfully converted.")

    return new_file


def get_transcription(audio_filename):
    audio_file = open(f"{audio_filename}", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    print(f"{audio_file} has been successfully transcribed.")

    os.remove(audio_filename)

    return transcript.text


def truncate_tokens(text):
    return text[:MAX_CHAR] if len(text) >= MAX_CHAR else text


def convert_stringlist(text, separator=", "):
    try:
        ll = text.strip("][").split(separator)
        return [elem.replace("'", "") for elem in ll]
    except Exception:
        return text


def convert_stringarray(text):
    try:
        ll = text.strip("][").split(",\n")
        return [ast.literal_eval(val) for val in ll]
    except:
        return text