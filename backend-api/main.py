import openai
import os
from dotenv import load_dotenv
from fastapi import FastAPI

# Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client using the new syntax
client = openai.OpenAI(api_key=api_key)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Blackjack AI Running"}

@app.post("/get-move/")
def get_move(player_hand: str, dealer_card: str):
    """Suggests the best move in blackjack based on basic strategy"""
    prompt = f"You're a blackjack expert. The player has {player_hand} and the dealer is showing {dealer_card}. What is the best move: hit, stand, double, or split?"

    try:
        response = client.chat.completions.create(  # New OpenAI API format
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a blackjack strategy AI. Follow the perfect blackjack strategy."},
                {"role": "user", "content": prompt}
            ]
        )
        return {"recommendation": response.choices[0].message.content}

    except Exception as e:
        return {"error": str(e)}

