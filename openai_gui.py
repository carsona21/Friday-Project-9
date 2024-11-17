import openai
import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the .env file
api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = api_key

# Function to generate a response from OpenAI
def get_openai_response():
    # Get the user input from the text box
    user_input = prompt_entry.get()

    if user_input.strip() == "":
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please enter a prompt.")
        return

    # Make a request to OpenAI API
    try:
        # Using the new API method `completions.create`
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you prefer
            prompt=user_input  # Pass the prompt here
        )
        
        # Extract the generated text from the response
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, response['choices'][0]['text'].strip())  # Get 'text' field
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("OpenAI Chatbot")

# Create and pack the components in the window
prompt_label = tk.Label(root, text="Enter your prompt:")
prompt_label.pack(pady=10)

# Create the input field for the user to type their prompt
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=10)

# Create the button to submit the prompt
submit_button = tk.Button(root, text="Submit", command=get_openai_response)
submit_button.pack(pady=10)

# Create the output area where the response will be displayed
output_text = scrolledtext.ScrolledText(root, width=60, height=10)
output_text.pack(pady=10)

# Start the GUI
root.mainloop()
