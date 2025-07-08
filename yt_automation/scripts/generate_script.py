import openai
import os
from utils.config import Config

def generate_script(topic):
    config = Config()
    openai_conf = config.get_openai_config()
    script_conf = config.get_script_config()

    openai.api_key = openai_conf["api_key"]
    model = openai_conf["model"]
    max_tokens = openai_conf.get("max_tokens", 1500)

    style = script_conf.get("style", "engaging")
    niche = script_conf.get("niche", "general audience")

    prompt = f"Write a {style} YouTube script on '{topic}' for an audience interested in {niche}."

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You're a YouTube scriptwriter."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )

    script_text = response.choices[0].message.content.strip()

    os.makedirs("output/scripts", exist_ok=True)
    with open(f"output/scripts/{topic.replace(' ', '_')}.txt", "w", encoding="utf-8") as f:
        f.write(script_text)

    print(f"[✅] Script saved: output/scripts/{topic.replace(' ', '_')}.txt")

if __name__ == "__main__":
    topic = input("Enter your video topic: ")
    generate_script(topic)
