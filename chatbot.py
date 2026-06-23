import difflib

# Load FAQs from file
def load_faqs(file_path):
    faqs = {}

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        if "|" in line:
            question, answer = line.strip().split("|", 1)
            faqs[question.lower()] = answer

    return faqs


# Find best matching answer
def get_response(user_question, faqs):
    questions = list(faqs.keys())

    match = difflib.get_close_matches(
        user_question.lower(),
        questions,
        n=1,
        cutoff=0.4
    )

    if match:
        return faqs[match[0]]

    return "Sorry, I couldn't find an answer to that question."


# Main chatbot loop
def chatbot():
    print("=" * 50)
    print("Welcome to FAQ Chatbot")
    print("Type 'exit' to quit")
    print("=" * 50)

    faqs = load_faqs("faq.txt")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = get_response(user_input, faqs)
        print("Bot:", response)


if __name__ == "__main__":
    chatbot()