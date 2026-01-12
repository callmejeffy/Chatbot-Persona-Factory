import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class Persona:
    """Blueprint for a chatbot's personality traits."""
    def __init__(self, name, description, instructions):
        self.name = name
        self.description = description
        self.instructions = instructions

class ChatBot:
    """The engine that manages conversation state and OpenAI calls."""
    def __init__(self, persona: Persona):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.persona = persona
        # 'System' message sets the personality
        self.history = [{"role": "system", "content": self.persona.instructions}]

    def get_response(self, user_input: str) -> str:
        # 1. Add user input to history
        self.history.append({"role": "user", "content": user_input})

        # 2. Call OpenAI API
        response = self.client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = self.history
        )

        # 3. Extract and save the reply
        reply = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return reply