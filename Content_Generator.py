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

def generate_ai_content(subject):
    """Generate AI content using Groq."""
    try:
        load_dotenv()
        groqkey = os.getenv('GROQ_API_KEY')
        client = Groq(api_key=groqkey)
        
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a creative writer with a knack for storytelling and writing engaging article. "
                        "Generate thought-provoking Reddit post that inspire conversations and curiosity."
                        "You can write about new advancements in {subject}."
                },
                {
                    "role": "user",
                    "content": f"Write a captivating Reddit post about {subject}but dont use the word title in the begining  "
                        "Share an intriguing fact or personal anecdote starting with its really cool, and ask the audience an open-ended question."
                }
            ],
            temperature=0.8,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error generating AI content: {e}")
        return None