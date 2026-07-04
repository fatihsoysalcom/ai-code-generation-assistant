import openai
import os

# IMPORTANT: Replace with your actual OpenAI API key
# It's recommended to use environment variables for security.
# export OPENAI_API_KEY='your-api-key'
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_code_suggestion(prompt):
    """
    Uses OpenAI's GPT-3.5 Turbo to generate code suggestions based on a prompt.
    This simulates an AI tool that helps developers write code faster.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI coding assistant. Provide concise and functional code snippets."},
                {"role": "user", "content": f"Generate Python code for: {prompt}"}
            ],
            max_tokens=150, # Limit the response length
            temperature=0.7 # Adjust for creativity vs. determinism
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("--- AI Code Generation Assistant ---")
    print("Enter a description of the code you want to generate, or type 'quit' to exit.")

    while True:
        user_input = input("\nYour request: ")
        if user_input.lower() == 'quit':
            break
        
        if not openai.api_key:
            print("Error: OPENAI_API_KEY environment variable not set.")
            print("Please set it before running the script.")
            continue

        print("Generating code suggestion...")
        suggestion = generate_code_suggestion(user_input)
        print("\n--- AI Suggestion ---")
        print(suggestion)
        print("---------------------")

    print("Exiting AI Code Generation Assistant.")
