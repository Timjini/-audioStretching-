from flask import Blueprint, jsonify, send_file
from services.audio_processing import process_audio
import os

audio_processing_controller_blueprint = Blueprint('audio_processing_controller', __name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@audio_processing_controller_blueprint.route('/process_audio', methods=['POST'])
def process_audio_endpoint():
    try:
        # Hardcoded file paths for testing
        pre_generated_path = './uploads/50seconds.mov'
        personalized_path = './uploads/2minutes.mp3'
        background_music_path = './uploads/background_music.mp3'

        # Validation before continuing
        if not all(map(os.path.exists, [pre_generated_path, personalized_path, background_music_path])):
            return jsonify({"error": "One or more audio files are missing in the hardcoded paths."}), 400

        output_path = os.path.join(UPLOAD_FOLDER, 'final_output_with_music.mp3')
        process_audio(pre_generated_path, personalized_path, background_music_path, output_path)

        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
