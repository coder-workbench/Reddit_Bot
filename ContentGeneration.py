import os
from dotenv import load_dotenv
from groq import Groq, GroqError
import praw

# Load environment variables

def loadKey():
    load_dotenv(dotenv_path=".env")
    return os.environ.get("GROQ_API_KEY")
  


def generate_reddit_post():
    try:
        
        # Initialize the Groq client
        client = Groq(api_key=loadKey())

        # Define the chat messages
        messages = [
            {
                "role": "user",
                "content": "Generate a short engaging post for Reddit about a random topic with a title and subreddit name and give me in dictionary format not a string. It should not be NSFW content.The keys should be title, subreddit and post. dont give me r/ in subreddit name",
            }
        ]

        # Attempt to get chat completion
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile")

        # Extract and validate the content
        response_content = chat_completion.choices[0].message.content
        print("*"*100)
        print("Content to be posted: " ,response_content)
        return response_content

    except GroqError as e:
        raise RuntimeError(f"Failed to generate a response from Groq: {e}")
    except (KeyError, IndexError, AttributeError):
        raise ValueError("Unexpected response format from Groq API.")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")



def generateComments(top_post):
    try:
        
        # Initialize the Groq client
        client = Groq(api_key=loadKey()) 
        
        # Define the chat messages
        messages = [
            {
                "role": "user",
                "content": f"Generate a comment for the top post in the subreddit {top_post}.",
            }
        ]
        
        # Attempt to get chat completion
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile")

        # Extract and validate the content
        response_content = chat_completion.choices[0].message.content
        print("*"*100)
        print("Comment to be posted: " ,response_content)
        return response_content


    except GroqError as e:
        raise RuntimeError(f"Failed to generate a response from Groq: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")