import openai


MODEL = "gpt-3.5-turbo"

DEFAULT_PATH = "./temp"


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
    openai_object = openai.ChatCompletion.acreate(
        model=model,
        messages=[
            message_dict("system", system_prompt),
            message_dict("user", prompt),
        ],
    )
    return openai_object["choices"][0]["message"]["content"]


def get_transcription(audio_filename):
    audio_file = open(f"{DEFAULT_PATH}/{audio_filename}", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript.text