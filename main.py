import requests
from bs4 import BeautifulSoup
import os

def send_pushover(message):
    token = os.environ.get("PUSHOVER_API_TOKEN")
    user = os.environ.get("PUSHOVER_USER_KEY")
    if not token or not user:
        raise ValueError("Missing Pushover credentials")
    
    response = requests.post("https://api.pushover.net/1/messages.json", data={
        "token": token,
        "user": user,
        "message": message
    })

    if response.status_code != 200:
        raise Exception("Failed to send notification")

def check_pokemon_center():
    url = "https://www.pokemoncenter.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    if "queue-it" in response.text.lower():
        send_pushover("⚠️ Queue is active on Pokémon Center!")

if __name__ == "__main__":
    check_pokemon_center()