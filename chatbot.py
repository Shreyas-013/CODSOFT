from googlesearch import search
def get_google_search_results(topic):
    try:
        search_results = list(search(topic, num=1, stop=1))
        return search_results[0] if search_results else None
    except Exception as e:
        print("An error occurred:", e)
        return None
if __name__ == "__main__":
    print("ChatBot: Hi, how can I help you today?")
    print("ChatBot: You can type 'quit' to exit the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = get_google_search_results(user_input)
        if response:
            print("ChatBot:", response)
        else:
            print("ChatBot: Sorry, I couldn't find information about that.")
