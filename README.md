# Speech to Text Sentiment Analysis Python Project

## Project Overview
The project enables sentiment analysis of spoken sentences that have been transcribed into text, utilizing the TextBlob 
and Speech Recognition libraries with the Google recognizer (Internet connection required).

## Instalation
~~~ 
$ git clone (repository address)
$ pip install -U textblob
$ python -m textblob.download_corpora
$ pip install PyAudio
$ pip install SpeechRecognition
$ pip install setuptools
~~~

## How to use
Run the 'main.py' located in the 'src' folder, enter the number of sentences you want to analyze. Speak your 
sentences after the prompt 'Starting listening...', and wait until your sentence is printed before speaking another one.

## License
This project is licensed under the MIT license