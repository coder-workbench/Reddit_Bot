# Reddit AI Bot

This Python-based Reddit bot integrates with the Reddit API, Groq AI API, and other custom modules to generate engaging content and interact with Reddit users. It allows users to schedule posts, comment on posts, and decide the time for posting. The bot also has logging features and error handling to ensure smooth operation.

## Features

- **AI-Generated Content**: Uses Groq AI API to generate engaging Reddit posts and comments.
- **Scheduled Posting**: Allows users to specify a time to post content.
- **Commenting on Posts**: Users can choose whether to comment on Reddit posts, and specify the subreddit.
- **Logging**: Tracks bot activity and errors in log files.
- **Error Handling**: Handles errors gracefully with logging and debugging information.

## Libraries and Modules

The bot requires the following libraries:

- `praw` - Python Reddit API Wrapper.
- `groq` - Groq AI API for generating content.
- `schedule` - Python library for scheduling tasks.
- `logging` - For logging actions and errors.
- `dotenv` - For loading environment variables.
- `os` - To interact with the operating system.
- `datetime` - For handling timestamps and scheduling.

Custom Modules:
- `ContentGeneration.py` - Contains functions for generating posts and comments.
- `Reddit.py` - Contains functions for interacting with Reddit's API (e.g., posting, commenting).

## Prerequisites

Make sure you have the following:

- Python 3.x
- `praw` (Reddit API wrapper)
- `groq` (For AI content generation)
- `schedule` (For scheduling tasks)
- `dotenv` (To load environment variables)
- `.env` file with API keys and credentials (details below)
  
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/coder-workbench/Reddit_Bot.git
    ```

2. Install the required dependencies:

    ```bash
   pip install praw groq schedule python-dotenv
    ```

3. Set up your `.env` file for API credentials:

    Create a `.env` file in the root of the project with the following variables:

    ```plaintext
   GROQ_API_KEY= [your secret key]
   Reddit_API-KEY = [your reddit secret]
    Client_ID = [reddit client id]
    rdt_username = [reddit username]
    rdt_password = [your password]
    ```

## Usage

1. Run the bot script:

    ```bash
    python Main.py
    ```

2. The bot will prompt you for the following information:

    - **Time to post**: Specify the time to post (e.g., 'HH:MM`).
    - **Comment on posts**: Whether to comment on posts (`Y` or `N`).
    - **Subreddit for commenting** (if applicable): Specify a subreddit to comment on.

    For **testing purposes**, the bot will default to posting in the **`testingground4bots`** subreddit. This is a hardcoded value, so it’s recommended to use this subreddit for testing. If you want to **auto-generate** the subreddit name, you can uncomment the appropriate line in the script to allow the bot to auto-select a subreddit.

3. The bot will generate content, schedule posts, and comment on posts as necessary.

## Hardcoded Subreddit (Testing)

For testing, the bot posts in the **`testingground4bots`** subreddit. You can find the line in the script where the subreddit is set:

# Hardcoded for testing
subreddit_name = 'testingground4bots'
## Known Issues

Bugs known in the current implementation of the bot:
Groq AI Data Format:
   The Groq AI API occasionally returns data in an unusual format (e.g., as a string or list) even though a dictionary format was requested. This could lead to code crashes when accessing expected dictionary keys.
   
