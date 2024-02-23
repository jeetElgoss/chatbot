from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Set your API key
client = OpenAI(
    api_key=os.getenv("OPEN_AI_API_KEY")  # this is also the default, it can be omitted
)

conversation_history = []


class ChatBot:

    def chat_with_openai(self, prompt):
        try:
            response = client.completions.create(
                model='gpt-3.5-turbo',
                prompt=prompt,
                max_tokens=150,  # Adjust the response length as needed
                n=1,  # Number of responses to generate
                stop=None,  # You can specify stop words if needed
                temperature=0.7,  # Adjust the temperature for more creative or focused responses
            )

            # Update conversation history
            conversation_history.append(prompt)
            conversation_history.append(response.choices[0].text.strip())

            return response.choices[0].text.strip()
        except Exception as e:
            print("Error :", e)

    def call_chat_with_openai(self):
        # Example usage
        user_input = input("Enter your question?")
        chatbot_response = self.chat_with_openai(user_input)
        print(chatbot_response)
