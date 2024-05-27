class BasicChatbot:
    def __init__(self):
        self.context = {}
        self.greetings = ["hello", "hi", "hey"]
        self.farewells = ["bye", "goodbye", "see you"]
        self.basic_responses = {
            "how are you": "I'm just a bot, but I'm doing great! How can I assist you today?",
            "what is your name": "I'm your friendly chatbot. You can call me Chatz.",
            "what can you do?": "I can chat with you and help with basic questions.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "what is the time?": "I don't have a clock, but you can check your device!"
        }

    def greet(self):
        return "Hello! How can I help you today?"

    def farewell(self):
        return "Goodbye! Have a great day!"

    def remember_context(self, user_input, user_response):
        self.context[user_input] = user_response

    def recall_context(self, user_input):
        return self.context.get(user_input, "I don't remember talking about that.")

    def ask_questions(self):
        questions = [
            "What's your name?",
            "How old are you?",
            "What's your favorite color?"
        ]
        responses = {}
        for question in questions:
            print(question)
            response = input("> ")
            responses[question] = response
        return responses

    def handle_error(self):
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def respond(self, user_input):
        if user_input.lower() in self.greetings:
            return self.greet()
        elif user_input.lower() in self.farewells:
            return self.farewell()
        elif user_input.lower() in self.basic_responses:
            return self.basic_responses[user_input.lower()]
        elif user_input.lower() in self.context:
            return self.recall_context(user_input.lower())
        else:
            return self.handle_error()

# Main interaction loop
def main():
    bot = BasicChatbot()
    print(bot.greet())

    user_responses = bot.ask_questions()
    for question, response in user_responses.items():
        bot.remember_context(question.lower(), response)

    while True:
        user_input = input("> ")
        if user_input.lower() in bot.farewells:
            print(bot.farewell())
            break
        response = bot.respond(user_input)
        print(response)

if __name__ == "__main__":
    main()
