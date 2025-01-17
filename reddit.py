import praw
import groq
import schedule
import time
import logging
from datetime import datetime, timedelta
import os
from groq import Groq
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_reddit_instance():
    """Create and return a Reddit instance using PRAW."""
    try:
        reddit = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent=os.getenv('REDDIT_USER_AGENT'),
            username=os.getenv('REDDIT_USERNAME'),
            password=os.getenv('REDDIT_PASSWORD')
        )
        return reddit
    except Exception as e:
        logger.error(f"Error creating Reddit instance: {e}")
        raise

def submit_post(subreddit_name, title, content, post_type='text'):
    """Submit a post to a specified subreddit."""
    reddit = create_reddit_instance()
    try:
        subreddit = reddit.subreddit(subreddit_name)
        if not subreddit.user_is_subscriber:
            logger.warning(f"Warning: You are not subscribed to r/{subreddit_name}")
        
        if post_type == 'text':
            submission = subreddit.submit(title=title, selftext=content)
        elif post_type == 'link':
            submission = subreddit.submit(title=title, url=content)
        else:
            raise ValueError("Invalid post_type. Use 'text' or 'link'")
        
        logger.info(f"Post successfully submitted to r/{subreddit_name}")
        return submission.url
    except Exception as e:
        logger.error(f"Error submitting post: {e}")
        return None