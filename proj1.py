"""
DecodeLabs - Project 1: Rule-Based AI Chatbot
Batch: 2026
"""

responses = {
    "hello": "Hello! Welcome to DecodeLabs. How can I help you?",
    "hi": "Hi there! Ready to build some logic?",
    "hey": "Hey! Let's get to work.",
    "how are you": "I'm just a rule-based bot, but I'm running flawlessly!",
    "what is your name": "I am DecodeBot, your deterministic AI companion.",
    "who made you": "The brilliant minds at DecodeLabs, Greater Lucknow, India.",
    "help": "I can greet you, tell you my name, or exit. Try 'hello' or 'bye'.",
    "bye": "Goodbye! Keep building. See you in Project 2.",
    "exit": "Exiting now. Remember: rules first, then intelligence.",
    "quit": "Quitting. Stay curious."
}

exit_commands = {"bye", "exit", "quit"}


def sanitize_input(user_input):
    cleaned = user_input.lower().strip()
    for char in ".,!?;:":
        cleaned = cleaned.replace(char, "")
    return cleaned


def get_response(user_input):
    return responses.get(user_input, "I don't understand that yet. Try 'help' for options.")


def run_chatbot():
    print("=" * 50)
    print("DecodeLabs Rule-Based AI Chatbot (Project 1)")
    print("=" * 50)
    print("Type 'bye', 'exit', or 'quit' to stop.\n")

    while True:
        raw_input = input("You: ")
        clean_input = sanitize_input(raw_input)

        if clean_input in exit_commands:
            print(f"Bot: {responses.get(clean_input, 'Shutting down.')}")
            print("\n[System] Chatbot terminated.")
            break

        reply = get_response(clean_input)
        print(f"Bot: {reply}\n")


if __name__ == "__main__":
    run_chatbot()