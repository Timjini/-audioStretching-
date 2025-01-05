from flask import Flask
from controllers.audio_processing_controller import audio_processing_controller_blueprint

app = Flask(__name__)

# Routes
app.register_blueprint(audio_processing_controller_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')