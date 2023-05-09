from .utils import get_transcription, get_answer_from_model, convert_mp3, prompt_config
from pytube import YouTube


class VideoMetadata:
    def __init__(self, video_url):
        self.video_url = video_url
        self.audio_filename = convert_mp3(self.video_url)

        self.transcription = get_transcription(f"{self.audio_filename}")
        self.prompt_config = {
            "title": prompt_config(
                """
You are an assistant expert in quick summary from audio and video. Your goal is to create a catchy one-sentence summary to entice the user to watch/listen to the video/audio. This one-sentence is based on the transcription given by the user.
You only answer with information from the text. Only answer, don't provide context or other information.
        """,
                f"""
Here is the text transcription from the video/audio :
{self.transcription}
Give me a catchy one-sentence summary
        """,
            ),
            "language": prompt_config(),
        }

    def get_title(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_language(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_summary(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_teaser(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_detailed_summary(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_key_phrases(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_acquired_skills(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_prerequisities(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_followups(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_glossary(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_assessement(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def get_thumbnail(self):
        return get_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    def buildPayload(self):
        return {
            "title": self.get_title(),
            "language": self.get_language(),
            "summary": self.get_summary(),
            "teaser": self.get_teaser(),
            "detailed_summary": self.get_detailed_summary(),
            "key_phrases": self.get_key_phrases(),
            "acquired_skills": self.get_acquired_skills(),
            "prerequisities": self.get_prerequisities(),
            "glossary": self.get_glossary(),
            "followups": self.get_followups(),
            "assessment": self.get_assessement(),
            "thumbnail": self.get_thumbnail(),
        }
