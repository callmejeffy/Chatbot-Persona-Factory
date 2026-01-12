from app.factory import BotFactory

def main():
    print("--- 🤖 Welcome to the Persona Factory ---")
    print("Choose your companion:")
    print("1: Filipino Kabayan | 2: Marites na Kapitbahay | 3: Girl Bestfriend")
    
    choice = input("\nEnter number (1-3): ")
    bot = BotFactory.create_bot(choice)
    
    print(f"\n--- {bot.persona.name} is now online ---")
    print("(Type 'exit' to quit)\n")

    while True:
        user_text = input("You: ")
        if user_text.lower() in ["exit", "quit"]:
            print("Shutting down ...")
            break
            
        response = bot.get_response(user_text)
        print(f"\n{bot.persona.name}: {response}\n")

if __name__ == "__main__":
    main()