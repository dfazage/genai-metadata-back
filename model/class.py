class VideoMetadata:
    def __init__(self, videoUrl):
        self.videoUrl=videoUrl

    @property
    def filename():
        return "filename"

    @property
    def transcription():
        return "transcription"
