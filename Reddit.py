import os
import praw
import ast
from dotenv import load_dotenv
from ContentGeneration import generateComments

def load_reddit_credentials():

    load_dotenv(dotenv_path=".env")
    reddit_client_id = os.environ.get("Client_ID")
    reddit_client_secret = os.environ.get("Reddit_API-KEY")
    reddit_username = os.environ.get("rdt_username")
    reddit_password = os.environ.get("rdt_password")

    if not all([reddit_client_id, reddit_client_secret, reddit_username, reddit_password]):
        raise ValueError("Reddit API credentials not found in environment variables.")

    return {
        "client_id": reddit_client_id,
        "client_secret": reddit_client_secret,
        "username": reddit_username,
        "password": reddit_password,
    }

def create_reddit_instance(credentials):

    return praw.Reddit(
        client_id=credentials["client_id"],
        client_secret=credentials["client_secret"],
        username=credentials["username"],
        password=credentials["password"],
        user_agent="EngagementBot by Ayushi Lanjewar",
    )

def post_to_reddit(generatedContent):

    # Parse the engagement post string into a dictionary
    generatedContent = ast.literal_eval(generatedContent)

    # Load Reddit API credentials
    credentials = load_reddit_credentials()

    # Create a Reddit instance
    reddit_instance = create_reddit_instance(credentials)

    subreddit = reddit_instance.subreddit("testingground4bots")

    # Submit the post
    post = subreddit.submit(title=generatedContent["title"], selftext=generatedContent["post"])
    print("*"*100)
    print(f"Posted to Reddit: {post.url} \n")
    return post

def comment_on_post(subreddit_name):
    try:
        # Load Reddit API credentials
        credentials = load_reddit_credentials()

        # Create a Reddit instance
        reddit = create_reddit_instance(credentials)

        # Get the subreddit
        subreddit = reddit.subreddit(subreddit_name)

        # Fetch the top post (e.g., from 'hot', 'new', or 'top')
        top_post = next(subreddit.new(limit=1))  # Get the top post in the subreddit

        #Send the top post to Grok, analyse it and generate a comment and post it
        
        print(top_post)
        print(top_post.title)
        print(top_post.selftext)
        print("*"*100)
        print("Commented Here \n",top_post.url)
        print("*"*100)

        if top_post.selftext:
            comment = generateComments(top_post.selftext)
            if comment.startswith('"') and comment.endswith('"'):
                comment = comment[1:-1]
            top_post.reply(comment)
            print("*"*100)
        print(f"Commented on the top post in r/{subreddit_name} with comment: \n {comment}")
        return {"success": True}


    except Exception as e:
        # Detailed error logging
        error_message = f"An error occurred: {e}"
        print(error_message)
        # Optionally, you could log this error to a file or monitoring system here
        return {"error": error_message}
        

    except Exception as e:
        # Detailed error logging
        error_message = f"An error occurred: {e}"
        print(error_message)
        # Optionally, you could log this error to a file or monitoring system here
        return {"error": error_message}
