from open_ai_chatbot import ChatBot

# Example usage
user_input = input("Enter your question?")
chatbot_response = ChatBot.chat_with_openai(user_input)
print(chatbot_response)
