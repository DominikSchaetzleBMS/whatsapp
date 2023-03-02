from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from huggingsound import SpeechRecognitionModel
from twilio.rest import Client
import requests

app = Flask(__name__)
account_sid = 'ACac4f5cfefacdf147060315f0f3c79ae8'
auth_token = '5213568bbf72740e3b922fd554094d71'
client = Client(account_sid, auth_token)

@app.route("/bot", methods=['POST'])
def whatsapp():
    # get the message and audio file url from the Twilio request
    message = request.form.get('Body')
    media_url = request.form.get('MediaUrl0')

    # save the audio file to a local directory and transcribe it using the Hugging Face model
    audio_path = 'temp_audio.mp3'
    with open(audio_path, 'wb') as f:
        f.write(requests.get(media_url).content)
    model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-german")
    transcriptions = model.transcribe([audio_path])
    transcription = transcriptions[0]

    # send the transcription back to the user via WhatsApp
    resp = MessagingResponse()
    resp.message(transcription["transcription"])
    return str(resp)

if __name__ == "__main__":
    app.run(port=4000)

