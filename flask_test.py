from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from huggingsound import SpeechRecognitionModel
from twilio.rest import Client
import requests


audio_path = r'C:\Users\dominik.schaetzle\Downloads\seosenf_ZPhI1ylW.mp3'
model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-german")
transcriptions = model.transcribe([audio_path])
transcription = transcriptions[0]

print(transcription["transcription"])