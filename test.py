from pbfaw.reddit import Reddit
import logging
from  pbfaw.models.util import stream_generator
from pbfaw.models import MoreComments


handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
for logger_name in ("praw", "prawcore"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

reddit = Reddit(
    username="Wezerl",
    password="VGhSrdM8o0XqXw",
    client_id="qm_JHMIB1vH10w",
    client_secret="3Wm-4GTB1xxAkGav8YVZJ_X5vdk",
    user_agent="useragent"
)
print(reddit.read_only)
try:
    #submission = reddit.subreddit("SubSimps").random()
    #print(submission.id)
    #test = reddit.subreddit("SubSimps").new(limit=10)
    #print(test)
    #inbox_stream = stream_generator(reddit.inbox.messages, pause_after=-1, skip_existing=True)
    while True:
        for unread in reddit.inbox.unread():
            print(unread)

    subreddit1 = reddit.subreddit("SubSimps").new(limit=10)
    for submission in reddit.subreddit("SubSimps").new(limit=100):
        try:
            print(submission.fullname)
            submission.comments.replace_more(limit=None)
            comment_queue = submission.comments[:]  # Seed with top-level
            while comment_queue:
                comment = comment_queue.pop(0)
                print(comment.fullname + ":" + comment.body)
        except Exception as e: print(e)
except Exception as e: print(e)
