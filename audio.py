import gtts
from playsound import playsound
import pandas as pd

df = pd.read_csv('data/kanji_data.csv') 

tts = gtts.gTTS(df['literal'][0], lang='ja')
tts.save(f'audio/{0}.mp3')