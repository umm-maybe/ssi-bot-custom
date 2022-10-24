from praw_ssi_file.reddit import Reddit
import logging

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
for logger_name in ("praw", "prawcore"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

reddit = Reddit(
    client_id="qm_JHMIB1vH10w",
    client_secret="3Wm-4GTB1xxAkGav8YVZJ_X5vdk",
    user_agent="script:%(bot_name)s:v%(bot_version)s (by /u/%(bot_author)s)"
)
print(reddit.read_only)
try:
    #submission = reddit.subreddit("SubSimps").random()
    #print(submission.id)
    #test = reddit.subreddit("SubSimps").new(limit=10)
    #print(test)
    subreddit1 = reddit.subreddit("SubSimps").new(limit=10)
    for submission in reddit.subreddit("SubSimps").new(limit=10):
        try:
            print(submission["data"]["id"])
        except Exception as e: print(e)
except Exception as e: print(e)
