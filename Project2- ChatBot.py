# Making a personalised chatbot

# Welcoming the user
print("Hello budy! Your personal ChatBot is here.")
print("Type 'bye' anytime to exit.")

# bot memory
responses = {
    "hello" : "Hi there, query me your problem",
    "good morning": "Good Morning dear!",
    "good evening": "Good Evening buddy",
    "motivate me": "Don't get upset. Your mistake improves you.\n Today's pain is tomorrow's strenght🔥",
    "how are you": "I am fine !",
    "bye" : "Ok bye, see you soon."
    
}
def botresponse(userQ):
    userQ = userQ.lower()
    for eachresponse in responses:
        if eachresponse in userQ:
            return responses[eachresponse]
    # return "Sorry, I don'know about this yet. I am learning."
        
    

#Taking user Input

while True :
    UserInput = input("Write your quarries here -> ")
    reply = botresponse(UserInput)
    print("ChatBot: ", reply)
    
    if "bye" in UserInput.lower():
        break