import spacy
import re


nlp = spacy.load("en_core_web_sm")


def identify_intent(user_input):
    user_input = user_input.lower()
    doc = nlp(user_input)


    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", user_input):
        return "greeting"
    elif re.search(r"\b(how are you|how's it going|what's up)\b", user_input):
        return "wellbeing"
    elif re.search(r"\b(what is your name|who are you|introduce yourself)\b", user_input):
        return "introduction"
    elif re.search(r"\b(weather|temperature|forecast)\b", user_input):
        return "weather"
    elif re.search(r"\b(joke|funny|make me laugh)\b", user_input):
        return "joke"
    elif re.search(r"\b(lol|haha|lmao)\b", user_input):
        return "funny"
    elif re.search(r"\b(bye|goodbye|see you|later)\b", user_input):
        return "farewell"
    elif len(doc.ents) > 0:  
        return "entity_based"
    else:
        return "unknown"


def chatbot_response(user_input):
    intent = identify_intent(user_input)

    responses = {
        "greeting": "Hello! How can I help you today?",
        "wellbeing": "I'm doing great, thanks for asking! How about you?",
        "introduction": "I’m your friendly chatbot assistant. Ask me anything!",
        "weather": "I can’t check the weather right now, but you can try asking your favorite weather app!",
        "joke": "Why don’t scientists trust atoms? Because they make up everything!",
        "farewell": "Goodbye! Have a great day!",
        "entity_based": f"I see you mentioned a location or date! Let me help you with that.",
        "funny": "Haha, I'm happy you found the joke funny :P",
        "unknown": "I’m not sure I understand. Can you ask something else?",
    }

    return responses.get(intent, "I’m sorry, I didn’t quite get that. Could you rephrase?")


def run_chatbot():
    print("Chatbot: Hi! I’m here to chat with you. Type 'exit' to end the conversation.")
    conversation_history = []  
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        conversation_history.append(f"You: {user_input}")

        response = chatbot_response(user_input)
        
        conversation_history.append(f"Chatbot: {response}")

        print(f"Chatbot: {response}")
        
        
if __name__ == "__main__":
    run_chatbot()

