from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
# Set your OpenAI API key
client = OpenAI(
    api_key=os.getenv("OPEN_AI_API_KEY")  # this is also the default, it can be omitted
)

# Load your own file data
with open('data.txt', 'r') as file:
    file_data = file.read()


# Define a function to interact with the OpenAI API
def generate_response(prompt):
    try:
        response = client.completions.create(
            model='gpt-3.5-turbo',
            prompt=prompt,
            max_tokens=150,  # Adjust the response length as needed
            n=1,  # Number of responses to generate
            stop=None,  # You can specify stop words if needed
            temperature=0.7,  # Adjust the temperature for more creative or focused responses
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error :", e)


# Main loop for user interaction
while True:
    user_input = input("You: ")

    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        break

    # Concatenate user input with your file data
    prompt = f"{user_input}\n{file_data}"

    # Generate and print the model's response
    model_response = generate_response(prompt)
    print("Chatbot:", model_response)
