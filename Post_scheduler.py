import praw
import groq
import schedule
import time
import logging
from datetime import datetime, timedelta
import os
from groq import Groq
from dotenv import load_dotenv

from reddit import *
from Content_Generator import *



# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_scheduled_post():
    """Create and submit a scheduled post."""
    try:
        subject = "Artificial Intelligence"  # You can modify this or make it dynamic
        content = generate_ai_content(subject)
        if content:
            post_url = submit_post(
                subreddit_name="test",
                title=subject,
                content=content,
                post_type='text'
            )
            logger.info(f"Scheduled post created successfully: {post_url}")
        else:
            logger.error("Failed to generate content")
    except Exception as e:
        logger.error(f"Error in scheduled post creation: {e}")

def schedule_post_in_five_minutes():
    """Schedule a post to be created in 5 minutes from now."""
    # Get current time
    current_time = datetime.now()
    # Calculate posting time (5 minutes from now)
    posting_time = current_time + timedelta(minutes=5)
    # Format time for scheduler
    schedule_time = posting_time.strftime("%H:%M")
    
    logger.info(f"Scheduling post for {schedule_time}")
    schedule.every().day.at(schedule_time).do(create_scheduled_post)
    
    # Run until the post is made
    while True:
        schedule.run_pending()
        time.sleep(1)
        # Check if we've passed the scheduled time
        if datetime.now() > posting_time + timedelta(minutes=1):
            break

if __name__ == "__main__":
    logger.info("Starting scheduler for post in 5 minutes...")
    schedule_post_in_five_minutes()
    logger.info("Post has been scheduled and executed. Program ending.")