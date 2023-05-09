from .utils import (
    get_transcription,
    convert_mp3,
    aget_answer_from_model,
    aget_image_from_model,
    prompt_config,
)

class VideoMetadata:
    def __init__(self, video_url):
        self.video_url = video_url
        self.audio_filename = convert_mp3(self.video_url)

        self.transcription = get_transcription(f"{self.audio_filename}")
        self.prompt_config = {
            "title": prompt_config(
                """
You are an assistant expert in title creation for audio and video. Your goal is to create a fancy title based on the transcription given by the user. Only answer, don't provide context or other information.
                """,
                f"""
Here is the text transcription from the video/audio :
{self.transcription}
Give me a fancy title.
                """,
            ),
            "summary": prompt_config(
                """
You are an assistant expert in quick summary from audio and video. Your goal is to create a catchy one-sentence summary to entice the user to watch/listen to the video/audio. This one-sentence is based on the transcription given by the user.
You only answer with information from the text. Only answer, don't provide context or other information.
        """,
                f"""
Here is the text transcription from the video/audio :
{self.transcription}
Give me a catchy one-sentence summary.
        """,
            ),
            "language": prompt_config(),
            "teaser": prompt_config(),
            "detailed_summary": prompt_config(),
            "key_phrases": prompt_config(),
            "acquired_skills": prompt_config(),
            "prerequisites": prompt_config(),
            "followups": prompt_config(),
            "glossary": prompt_config(),
            "assessement": prompt_config(),
            "thumbnail": prompt_config(),
        }

    async def get_title(self):
        print('get_title')
        return await aget_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    async def get_language(self):
        print('get_language')
        return await aget_answer_from_model(
            self.prompt_config["language"].system_prompt,
            self.prompt_config["language"].prompt,
        )

    async def get_summary(self):
        print('get_summary')
        return await aget_answer_from_model(
            self.prompt_config["summary"].system_prompt,
            self.prompt_config["summary"].prompt,
        )

    async def get_teaser(self):
        return await aget_answer_from_model(
            self.prompt_config["teaser"].system_prompt,
            self.prompt_config["teaser"].prompt,
        )

    async def get_detailed_summary(self):
        return await aget_answer_from_model(
            self.prompt_config["detailed_summary"].system_prompt,
            self.prompt_config["detailed_summary"].prompt,
        )

    async def get_key_phrases(self):
        return await aget_answer_from_model(
            self.prompt_config["key_phrases"].system_prompt,
            self.prompt_config["key_phrases"].prompt,
        )

    async def get_acquired_skills(self):
        return await aget_answer_from_model(
            self.prompt_config["acquired_skills"].system_prompt,
            self.prompt_config["acquired_skills"].prompt,
        )

    async def get_prerequisites(self):
        return await aget_answer_from_model(
            self.prompt_config["prerequisites"].system_prompt,
            self.prompt_config["prerequisites"].prompt,
        )

    async def get_followups(self):
        return await aget_answer_from_model(
            self.prompt_config["followups"].system_prompt,
            self.prompt_config["followups"].prompt,
        )

    async def get_glossary(self):
        return await aget_answer_from_model(
            self.prompt_config["glossary"].system_prompt,
            self.prompt_config["glossary"].prompt,
        )

    async def get_assessement(self):
        return await aget_answer_from_model(
            self.prompt_config["assessement"].system_prompt,
            self.prompt_config["assessement"].prompt,
        )

    async def get_thumbnail(self):
        image_prompt = await aget_answer_from_model(
            self.prompt_config["thumbnail"].system_prompt,
            self.prompt_config["thumbnail"].prompt,
        )
        return await aget_image_from_model(image_prompt)

    async def buildPayload(self):
        return {
            "title": await self.get_title(),
            "language": await self.get_language(),
            "summary": await self.get_summary(),
            "teaser": await self.get_teaser(),
            "detailed_summary": await self.get_detailed_summary(),
            "key_phrases": await self.get_key_phrases(),
            "acquired_skills": await self.get_acquired_skills(),
            "prerequisites": await self.get_prerequisites(),
            "glossary": await self.get_glossary(),
            "followups": await self.get_followups(),
            "assessment": await self.get_assessement(),
            "thumbnail": await self.get_thumbnail()
        }
