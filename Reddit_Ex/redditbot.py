import praw
import re
import time

# Set up the Reddit API client
reddit = praw.Reddit(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", user_agent="YOUR_USER_AGENT")

# Set up the word that the bot will respond to
trigger_word = "hello"

# Set up the response message
response_message = "Hello there! How are you doing?"

# Set up the subreddit that the bot will operate in
subreddit = reddit.subreddit("test")

# Set up the comment stream to listen for new comments
for comment in subreddit.stream.comments():
    # Check if the comment contains the trigger word
    if trigger_word in comment.body:
        # If the trigger word is found, reply to the comment with the response message
        comment.reply(response_message)
        
    # Pause the script for the recommended amount of time after each request
    time.sleep(reddit.auth.limits["comment"]["remaining"])
