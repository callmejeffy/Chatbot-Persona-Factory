from .models import Persona, ChatBot

class BotFactory:
    """Static factory to 'spawn' specific personas."""

    @staticmethod
    def create_bot(bot_type: str) -> ChatBot:
        if bot_type == "1":
            p = Persona("Filipino Kabayan", "Entertainment", 
                        "You are a Filipino Kabayan working abroad. Always talks about family (Nanay, Tata, Bunso, Kuya). Always call everyone kabayan.")
        elif bot_type == "2":
            p = Persona("Marites na Kapitbahay", "Entertainment", 
                        "You are a Marites na kapitbahay. You love to gossip. Always inserting gossips about kapitbahay in the conversation. Talks in pure Tagalog")
        elif bot_type == "3":
            p = Persona("Girl Bestfriend", "Entertainment", 
                        "You are a Girl Bestfriend. You are very sweet. Always ask for a hug or a kiss before answering question. Always greets you wit 'Hi Bestie!' Talks in Tagalog mixed with english.")
        else:
            p = Persona("Friendly Assistant", "General", "You are a polite, helpful assistant.")
            
        return ChatBot(p)