import random
from datetime import datetime

# Response patterns
responses = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "howdy", "greetings"],
        "replies": ["Hello! How can I help you?", "Hey there!", "Hi! Nice to meet you!"]
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "see you", "exit", "quit"],
        "replies": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
    },
    "how_are_you": {
        "keywords": ["how are you", "how's it going", "what's up", "how do you do"],
        "replies": ["I'm doing great, thanks for asking!", "All good! How about you?", "Fantastic! Ready to chat!"]
    },
    "name": {
        "keywords": ["your name", "who are you", "what are you"],
        "replies": ["I'm PyBot, your simple Python chatbot!", "The name's PyBot!"]
    },
    "time": {
        "keywords": ["time", "what time", "current time"],
        "replies": [f"The current time is {datetime.now().strftime('%H:%M:%S')}"]
    },
    "date": {
        "keywords": ["date", "what date", "today", "what day"],
        "replies": [f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"]
    },
    "thanks": {
        "keywords": ["thank", "thanks", "thank you", "appreciate"],
        "replies": ["You're welcome!", "Happy to help!", "Anytime!"]
    },
    "help": {
        "keywords": ["help", "what can you do", "features", "commands"],
        "replies": ["I can chat, tell you the time/date, answer basic questions. Just talk to me!"]
    }
}

default_replies = [
    "Hmm, I'm not sure about that. Can you rephrase?",
    "Interesting! Tell me more.",
    "I didn't quite get that. Try asking something else!",
    "I'm still learning. Could you clarify?"
]

def get_response(user_input):
    user_input_lower = user_input.lower()

    for category, data in responses.items():
        if any(keyword in user_input_lower for keyword in data["keywords"]):
            # Re-evaluate time/date dynamically
            if category == "time":
                return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
            if category == "date":
                return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"
            return random.choice(data["replies"])

    return random.choice(default_replies)

def chatbot():
    print("=" * 40)
    print("      Welcome to PyBot!      ")
    print("  Type 'quit' or 'bye' to exit  ")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("PyBot: Please type something!")
            continue

        print(f"PyBot: {get_response(user_input)}")

        if any(word in user_input.lower() for word in ["bye", "goodbye", "quit", "exit"]):
            break

chatbot()
