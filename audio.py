import gtts
from playsound import playsound
import pandas as pd

df = pd.read_csv('data/kanji_data.csv') 

for ind in range(1834,len(df)):
    tts = gtts.gTTS(df['example'][ind], lang='ja')
    tts.save(f'examples/{ind}.mp3')
    tts = gtts.gTTS(df['literal'][ind], lang='ja')
    tts.save(f'words/{ind}.mp3')
