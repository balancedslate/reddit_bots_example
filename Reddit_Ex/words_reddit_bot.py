import praw

# Replace "client_id", "client_secret", and "user_agent" with your own values
reddit = praw.Reddit(client_id="client_id", client_secret="client_secret", user_agent="user_agent")

# Choose a subreddit to search
subreddit = reddit.subreddit("learnprogramming")

# Set the word you want to count
word_to_count = "python"

# Initialize a counter
count = 0

# Search the subreddit for posts containing the word
for submission in subreddit.search(word_to_count):
    # Count the number of times the word appears in the title of the post
    count += submission.title.lower().count(word_to_count)

# Print the final count
print(f"The word '{word_to_count}' appears {count} times in r/learnprogramming")
