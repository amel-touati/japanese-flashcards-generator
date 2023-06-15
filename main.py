from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import json

# Read the CSV file and preprocess the data
df = pd.read_csv('data/kanji_data.csv')

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def get_meaning_list(row):
    meanings = df['meanings'][row].split(',')
    cleaned_list = [meaning.strip().replace("[", "").replace("]", "").replace("'", "") for meaning in meanings]
    return cleaned_list

for ind in range(len(df)):
    @app.get("/{ind}", response_class=HTMLResponse)
    async def home(request: Request, ind: int):
        if ind < 0 or ind >= len(df):
            return "Invalid index"
        
        df['ja_kuns'][ind]=df['ja_kuns'][ind].replace("[", "").replace("]", "").replace("'", "").replace(",", "、")
        df['ja_ons'][ind]=df['ja_ons'][ind].replace("[", "").replace("]", "").replace("'", "").replace(",", "、")
        
        mini_df = df.iloc[[ind]]
        js = mini_df.to_json(orient="records")
        data = json.loads(js)

        meanings = get_meaning_list(ind)

        return templates.TemplateResponse(
            "main.html",
            {"request": request, "flashcards": data, "meanings": meanings},
        )
