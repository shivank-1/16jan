***Reddit Bot with Groq AI Integration***


Demo Video-https://drive.google.com/drive/folders/1pqEjpQX0QmSjpf8lFMBkrZY8ODnKQ5aa?usp=sharing

This project automates posting on Reddit using Groq AI for content generation.

**Setup Instructions**

**Step1. Generate Reddit Credentials**

Visit Reddit's App Preferences

Click Create App or Create Another App.

Fill out the fields:

App Type: Script

Name: Your Bot Name

Redirect URI: http://localhost:8080

Permissions: Choose necessary scopes

Save the app and note down:

client_id

client_secret

**Step2. Generate Groq API Key**

Visit the Groq API Portal

Sign in and generate an API key.

**Step3. Create a .env File**

Create a .env file in the root directory and add the following:

REDDIT_CLIENT_ID="your_reddit_client_id"
REDDIT_CLIENT_SECRET="your_reddit_client_secret"
REDDIT_USER_AGENT="your_reddit_user_agent"
REDDIT_USERNAME="your_username"
REDDIT_PASSWORD="your_password"
GROQ_API_KEY="your_groqapi_key"

**Step4. Create a Virtual Environment**

Create a virtual environment using Conda:

conda create -p venv python==3.10 -y

Activate the environment:

conda activate ./venv

**Step5. Install Requirements**

Install the necessary packages:

pip install -r requirements.txt

**Step6. Run the Bot**

Run the bot using:

python Post_scheduler.py

Troubleshooting

Ensure all environment variables are correctly set.

Verify your Reddit app permissions.

Check the Groq API rate limits.

