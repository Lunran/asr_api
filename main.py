from flask import (
    Flask, request
)
import whisper


SAVE_PATH = "./tmp.wav"


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

model = whisper.load_model("medium")


@app.route('/asr', methods=['POST'])
def asr():
    if request.method == 'POST':
        wav = request.files['file']
        wav.save(SAVE_PATH)
        output = request.form.get('output')
        
        audio = whisper.load_audio(SAVE_PATH)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        options = whisper.DecodingOptions(language=output, without_timestamps=True)
        result = whisper.decode(model, mel, options)
        text = result.text

        return text


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8003, debug=True)
