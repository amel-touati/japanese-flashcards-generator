from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import json
# method object to list:
def get_meaning_list(row):
    mean = []
    for meaning in df['meanings'][row].split(','):
        cleaned_string = meaning.replace("[", "").replace("]", "").replace("'", "")
        mean.append(cleaned_string)
    cleaned_list = [element.strip() for element in mean]
    
    return cleaned_list

#preprocessing meaning
df = pd.read_csv('data/kanji_data.csv')
mean = []
for meaning in df['meanings'][0].split(','):
    cleaned_string = meaning.replace("[", "").replace("]", "").replace("'", "")
    mean.append(cleaned_string)
    
cleaned_list = [element.strip() for element in mean]



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/{1}", response_class=HTMLResponse)
async def home(request: Request):
    df = pd.read_csv("data/kanji_data.csv", nrows=1)
    df['ja_kuns'][0]=df['ja_kuns'][0].replace("[", "").replace("]", "").replace("'", "").replace(",", "、")
    df['ja_ons'][0]=df['ja_ons'][0].replace("[", "").replace("]", "").replace("'", "").replace(",", "、")

    js = df.to_json(orient="records")
    data=json.loads(js)
    return templates.TemplateResponse("main.html", 
                                      {"request": request, 
                                       "flashcards": data,
                                       "meanings": cleaned_list,
                                       })


