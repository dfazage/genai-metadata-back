from .utils import (
    get_transcription,
    convert_mp3,
    aget_answer_from_model,
    aget_image_from_model,
    prompt_config,
    truncate_tokens,
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
{truncate_tokens(self.transcription)}
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
{truncate_tokens(self.transcription)}
Give me a catchy one-sentence summary.
        """,
            ),
            "language": prompt_config(
                """
You are an assistant expert in language detection for audio and video transcriptions.
            """,
                f"""
Here is the text transcription from the video/audio :
{truncate_tokens(self.transcription)}
Give me the language only.
            """,
            ),
            "detailed_summary": prompt_config(
                """
You are an assistant expert in quick summary from audio and video. Your goal is to create a quick summary of a long text. This quick summary is based on the transcription given by the user. The summary reflect the keys information from the text. You only answer with information from the text. The tone is casual and fluent. Only answer, don't provide context or other information. No more than 50 words. 
            """,
                f"""
Here is the text transcription from the video/audio :
{truncate_tokens(self.transcription)}
Give me the quick summary.
            """,
            ),
            "teaser": prompt_config(
                """
You are a community manager's assistant, and your role is to generate short and engaging LinkedIn posts that will generate views and clicks, based on transcripts that I will provide.
Based on each transcript, please generate an engaging LinkedIn text post teasing the subject, with 5 relevant hashtags. No more than 250 characters for the post. For this post, use a friendly, fun, witty, dynamic and smart tone, as well as emojis.
            """,
                f"""
Here is the transcript:
{truncate_tokens(self.transcription)}
Generate the LinkedIn post.
            """,
            ),
            "key_phrases": prompt_config(
                """
You are an assistant expert in quick summary from audio and video. Your goal is to extract key quotes from a long text. The sentences extract are based on the transcription given by the user. The sentences reflect the key message from the text. You only answer with exact words and sentence from the text. Only answer, don't provide context or other information.
            """,
                f"""
Here is the text transcription from the video/audio :
{truncate_tokens(self.transcription)}
Give me the 4 most important sentences from the text. Use exactly the same words and sentences as in the text. The output format must be python list. Give me only the python list. ['value_phrase1', 'value_phrase2','value_phrase3', 'value_phrase4']
            """,
            ),
            "acquired_skills": prompt_config(
                """
You are an expert in learning and development. Your goal is to detect the skills developed when the user watch/listen a video/audio. The skills identified are based on the text transcription given by users. Only answer, don't provide context or other information. You only answer with the 3 skills in this order level 1, level 2, level 3. Only one skill per each level. Only skills in the lists provided. 

Skills Level 1 :
Business Skills
Personal Development
Safety and Compliance
Technology Skills

Skills Level 2 :
People and Communication Skills
General Personal Development
General Management
HR Compliance
Human Resources
Data & Analytics
Devops Networking and Security
Data Compliance
Marketing
Leadership
Time Management
Sales and Customer Services
Language and Literature

Skills Level 3:
Business Ethics
Product marketing
Conflict Resolution
Emotional Intelligence
Performance Management
Negotiation
Presentation Skills
Diversity & Culture
            """,
                f"""
Here is the text transcription from the video/audio :
{truncate_tokens(self.transcription)}
Give me the 3 skills levels associated with the text. Give me the output in a python list only.
            """,
            ),
            "prerequisites": prompt_config(
                """
You are a learning and development expert. Your goal is to detect the prerequisite knowledge for understanding the video/audio. The text transcription is given by the user. Answer the knowledge needed to understand this text. Answer only, without providing context or other information. Do not describe the knowledge of this text, only the knowledge required to understand it.
            """,
                f"""
Here is the text transcription from the video/audio :
{truncate_tokens(self.transcription)}
Give me 3 sentences for the knowledge needed for a better understanding. Give me the output in a python list only like so: ['value_sentence1', 'value_sentence2','value_sentence3']       
            """,
            ),
            "followups": prompt_config(
                """
You are an expert library assistant in any field. Your goal is to give advice on books. The suggested books will help to deepen the themes developed in the text transcript given by the user. Answer only, do not give context or other information. You recommend as a priority scientifically validated books. Give me the answer in English.            
            """,
                f"""
Here is the text transcription from the video/audio :
{truncate_tokens(self.transcription)}
Give me three books recommandation in the following format: author's name, book title, publisher's name and publication date. For each book you provide a short explanation. (no more than 20 words) and the internet link to the goodreads reference.
            """,
            ),
            "glossary": prompt_config(
                """
You are an expert assistant in creating glossaries.
Your task is to provide a glossary containing detailed, simple, concise and clear explanations of key words in a given text.

Your objective is to create a 10-word glossary that explains difficult word or key information about the main topic from a transcript of an audio/video text given by the user. The glossary consists solely of words from the text. Only answer, don't provide context or other information. Do not specify the language of the words. Give me the answer in english. 
            """,
                f"""
Here is the text transcription from the video/audio :
{truncate_tokens(self.transcription)}
Give me 10 words for the glossary. The output format must be python list of dict with keys "name" and "def". Give me only the python list [{{'name': 'value_name1', 'def'': 'value_def1'}},...,\{{'name': 'value_name10', 'def': 'value_def10'\}}]
            """,
            ),
            "assessement": prompt_config(
                """
You are a friendly instructional designer assistant. Your goal is to provide key learning factors/information/resource/material based on a transcript I am providing, extracted from a podcast.
            """,
                f"""
Here is the text transcription from the video/audio :
{truncate_tokens(self.transcription)}
Please generate a quiz that highlights the key ideas in the provided text. The quiz will be made of 2 true or false questions. No more than 30 words for each question.
For each answer, tell me which is correct and please provide a 30-word explanation as to why it is correct, in relation to the subject. For each question, generate a fun fact vaguely related to the subject to bring extra information - no more than 40 words. Provide quiz only with answers.
            """,
            ),
            "thumbnail": prompt_config(
                """
You are an assistant expert prompt generation for dall-e's artificial intelligence program. Your task is to provide detailed and creative descriptions that will inspire unique, poetic and interesting images in the AI. The prompt need to be a description that represent a poetic image. The more detailed and simple your description, the more interesting the resulting image will be. The desired image is simple and poetic. You give a descriptive prompt to generate an image that represents the text given by the user. Only answer, don't provide context or other information. No more than 20 words.
            """,
                f"""
Here is the text transcription from the video/audio :
{truncate_tokens(self.transcription)}
Give me the suitable prompt for a thumbnail. Image only, no text in the thumbnail.
            """,
            ),
        }

    async def get_title(self):
        print("get_title")
        return await aget_answer_from_model(
            self.prompt_config["title"].system_prompt,
            self.prompt_config["title"].prompt,
        )

    async def get_language(self):
        print("get_language")
        return await aget_answer_from_model(
            self.prompt_config["language"].system_prompt,
            self.prompt_config["language"].prompt,
        )

    async def get_summary(self):
        print("get_summary")
        return await aget_answer_from_model(
            self.prompt_config["summary"].system_prompt,
            self.prompt_config["summary"].prompt,
        )

    async def get_teaser(self):
        print("get_teaser")
        return await aget_answer_from_model(
            self.prompt_config["teaser"].system_prompt,
            self.prompt_config["teaser"].prompt,
        )

    async def get_detailed_summary(self):
        print("get_detailed_summary")
        return await aget_answer_from_model(
            self.prompt_config["detailed_summary"].system_prompt,
            self.prompt_config["detailed_summary"].prompt,
        )

    async def get_key_phrases(self):
        print("get_key_phrases")
        return await aget_answer_from_model(
            self.prompt_config["key_phrases"].system_prompt,
            self.prompt_config["key_phrases"].prompt,
        )

    async def get_acquired_skills(self):
        print("get_acquired_skills")
        return await aget_answer_from_model(
            self.prompt_config["acquired_skills"].system_prompt,
            self.prompt_config["acquired_skills"].prompt,
        )

    async def get_prerequisites(self):
        print("get_prerequisites")
        return await aget_answer_from_model(
            self.prompt_config["prerequisites"].system_prompt,
            self.prompt_config["prerequisites"].prompt,
        )

    async def get_followups(self):
        print("get_followups")
        return await aget_answer_from_model(
            self.prompt_config["followups"].system_prompt,
            self.prompt_config["followups"].prompt,
        )

    async def get_glossary(self):
        print("get_glossary")
        return await aget_answer_from_model(
            self.prompt_config["glossary"].system_prompt,
            self.prompt_config["glossary"].prompt,
        )

    async def get_assessement(self):
        print("get_assessement")
        return await aget_answer_from_model(
            self.prompt_config["assessement"].system_prompt,
            self.prompt_config["assessement"].prompt,
        )

    async def get_thumbnail(self):
        print("get_thumbnail")
        image_prompt = await aget_answer_from_model(
            self.prompt_config["thumbnail"].system_prompt,
            self.prompt_config["thumbnail"].prompt,
        )
        return await aget_image_from_model(
            f"{image_prompt}. Surrealism, futurist, digital art."
        )

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
            "assessement": await self.get_assessement(),
            "thumbnail": await self.get_thumbnail(),
        }
