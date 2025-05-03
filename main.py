import requests

API_KEY = "sk_86db1efe0f54da0b2d9b42214a404ea4daa126853333f63f"
VOICE_ID = "OF1C0YQehjdANRkyIcs3"
TEXT = (
     "<speak>"
    "Why losing weight in your 40s feels impossible…<break time=\"800ms\"/>"
    "You’ve tried everything — from keto to Pilates.<break time=\"700ms\"/>"
    "Ever notice how your friends shed pounds with ease<break time=\"300ms\"/>while you stay stuck?<break time=\"600ms\"/>"
    "The answer is simpler than you think.<break time=\"800ms\"/>"
    "The secret no friend or doctor tells is:<break time=\"400ms\"/>when your body overheats at night,<break time=\"300ms\"/>it locks into fat-storing mode.<break time=\"800ms\"/>"
    "Excessive sweating prevents your body from reaching deep sleep<break time=\"500ms\"/> — <break time=\"300ms\"/>the stage where you burn the most fat.<break time=\"900ms\"/>"
    "Sleeping hot isn’t just uncomfortable —<break time=\"300ms\"/>it’s making weight loss nearly impossible.<break time=\"800ms\"/>"
    "That’s why we created the Ice Blanket —<break time=\"400ms\"/>the cooling blanket<break time=\"300ms\"/> designed to keep your body at the perfect temperature<break time=\"400ms\"/>all night long,<break time=\"700ms\"/>"
    "so you can finally sleep deeper,<break time=\"300ms\"/>recover faster,<break time=\"300ms\"/>and start losing weight naturally.<break time=\"800ms\"/>"
    "Its silky smooth fabric<break time=\"300ms\"/>is breathable<break time=\"300ms\"/>and cold to the touch,<break time=\"500ms\"/>"
    "thanks to Freeze Core technology<break time=\"400ms\"/>that draws heat away from your body.<break time=\"900ms\"/>"
    "Plus, it’s machine washable,<break time=\"300ms\"/>hypoallergenic,<break time=\"300ms\"/>and built for easy weight loss."
    "</speak>"
)
url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": API_KEY,
    "Accept": "audio/mpeg",
    "Content-Type": "application/json"
}
payload = {
    "text": TEXT,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}

response = requests.post(url, json=payload, headers=headers)
response.raise_for_status()

with open("outputs/output.mp3", "wb") as f:
    f.write(response.content)
print("Saved output.mp3")
