import json
import os
import tempfile
from pathlib import Path

import cog

import speech_recognition as sr


class RecognizeSpeech(cog.Predictor):
    def setup(self):
        """Init speech recognizer"""
        self.recognizer = sr.Recognizer()

    @cog.input("input", type=Path, help="Content image")
    def predict(self, input):
        """Transcript audio file using Sphinx engine"""

        # read audio file
        with sr.AudioFile(str(input)) as source:
            audio = self.recognizer.record(source)

        # recognize speech using Sphinx
        try:
            recog = self.recognizer.recognize_sphinx(audio)
            #print("Sphinx thinks you said: " + recog)
        except sr.UnknownValueError:
            recog = "Sphinx could not understand audio"
            #print(recog)
        except sr.RequestError as e:
            recog = "Sphinx error; {0}".format(e)
            #print(recog)

        return recog
