from .utils import get_transcription, get_answer_from_model, convert_mp3
from pytube import YouTube


class VideoMetadata:
    def __init__(self, video_url):
        self.video_url = video_url
        self.audio_filename = convert_mp3(self.video_url)

        self.transcription = get_transcription(f"{self.audio_filename}")

    def getTitle(self):
        systemPrompt = """
You are an assistant expert in quick summary from audio and video. Your goal is to create a catchy one-sentence summary to entice the user to watch/listen to the video/audio. This one-sentence is based on the transcription given by the user.
You only answer with information from the text. Only answer, don't provide context or other information.
        """
        prompt = f"""
Here is the text transcription from the video/audio :
{self.transcription}
Give me a catchy one-sentence summary
        """
        return get_answer_from_model(systemPrompt, prompt)

    def getSummary(self):
        systemPrompt = ""
        prompt = ""
        return get_answer_from_model(systemPrompt, prompt)
