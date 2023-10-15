import openai

# Set API key
openai.api_key = "YOUR OPENAI-API-KEY"
openai.api_base = "https://api.openai.com/v1"

def chat_with_gpt3():
    messages = []
    while True:
        # User input
        user_message = input("You: ")
        messages.append({"role": "user", "content": user_message})

        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Get the model's response
        gpt3_response = response.choices[0].message['content']
        messages.append({"role": "assistant", "content": gpt3_response})

        # Display the model's response
        print(f"GPT-3: {gpt3_response}")
        
        # You can remove the # before the comment statement below to study the role of the code
      
        #print("--------------messages[]的内容-----------------\n\n")
        #print(messages)
        #print("--------------messages的条数-----------------\n\n")
        #print(len(messages))

      
        # Keep the conversation history limited to 5 turns
        if len(messages) > 20:
            messages.pop(0)
            messages.pop(0)

        # Check for exit condition
        if user_message.lower() in ["exit", "quit", "bye"]:
            print("Exiting the chat. Goodbye!")
            break

if __name__ == '__main__':
    chat_with_gpt3()
