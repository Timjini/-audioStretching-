from pydub import AudioSegment

class AudioEditing:
    def __init__(self, audio_path):
        self.audio = AudioSegment.from_file(audio_path)

    def fadeout_and_trim(self, length_in_minutes=2, fade_duration_ms=5000):
        """
        Fades out the last 5 seconds and trims the audio to the specified length.
        
        :param length_in_minutes: Desired length of the final audio in minutes (default 2 minutes).
        :param fade_duration_ms: Duration for fade out in milliseconds (default 5 seconds).
        :return: The edited AudioSegment object.
        """
        max_length = length_in_minutes * 60 * 1000

        if len(self.audio) > max_length:
            self.audio = self.audio[:max_length]

        self.audio = self.audio.fade_out(fade_duration_ms)

        return self.audio
