from pydub import AudioSegment

def process_audio(pre_generated_path, personalized_path, background_music_path, output_path):
    pre_generated = AudioSegment.from_file(pre_generated_path)
    personalized = AudioSegment.from_file(personalized_path)
    background_music = AudioSegment.from_file(background_music_path)

    combined_audio = pre_generated.append(personalized, crossfade=2000)

    max_length = 100000  #  milliseconds
    if len(combined_audio) > max_length:
        combined_audio = combined_audio[:max_length]

    combined_audio = combined_audio.fade_in(5000).fade_out(5000)

    background_music = background_music - 15  # Reduce by 15 dB

    looped_background = background_music * (len(combined_audio) // len(background_music) + 1)

    final_audio = combined_audio.overlay(looped_background[:len(combined_audio)])

    final_audio.export(output_path, format="mp3")
