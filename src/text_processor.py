
# OPENAI Threads
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
OPENAI_THREAD_ID=os.getenv("OPENAI_THREAD_ID")
OPENAI_ASSISTANT_ID=os.getenv("OPENAI_ASSISTANT_ID")
client=OpenAI(api_key=OPENAI_API_KEY)

def reply(text):

    client.beta.threads.messages.create(
        thread_id=OPENAI_THREAD_ID,
        role="user",
        content=text,
    )

    run = client.beta.threads.runs.create(
        thread_id=OPENAI_THREAD_ID,
        assistant_id=OPENAI_ASSISTANT_ID
    )

    while not run.status == "completed":
        print("Waiting for answer...")
        run = client.beta.threads.runs.retrieve(
            thread_id=OPENAI_THREAD_ID,
            run_id=run.id
        )

    messages = client.beta.threads.messages.list(OPENAI_THREAD_ID, order='desc', limit=1)
    return messages.data[0].content[0].text.value