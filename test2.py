from praw_file.reddit import Reddit

reddit = Reddit(
    client_id="flcEUCJ5JkVDxh8w0oVLaw",
    client_secret="a6ZQWE1otbrkcf_qPmPmHyuWsDW9vg",
    user_agent="script:%(bot_name)s:v%(bot_version)s (by /u/%(bot_author)s)"
)
print(reddit.read_only)
try:
    for submission in reddit.subreddit("SubSimGPT2Interactive").new(limit=4):
        try:
            print(submission.id)
        except Exception as e: print(e)
except Exception as e: print(e)
