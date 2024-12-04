
# OPENAI Threads
from dotenv import load_dotenv
from openai import OpenAI
from utils import logger
import os

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
OPENAI_ASSISTANT_NAME=os.getenv("OPENAI_ASSISTANT_NAME")
OPENAI_ASSISTANT_INSTRUCTIONS=os.getenv("OPENAI_ASSISTANT_INSTRUCTIONS")
OPENAI_ASSISTANT_MODEL=os.getenv("OPENAI_ASSISTANT_MODEL")

client=OpenAI(api_key=OPENAI_API_KEY)

my_assistant = None
my_thread = None

def load_assistant():
    # Find by name else create new
    global my_assistant
    my_assistants = client.beta.assistants.list(order="desc", limit="20")
    for assistant in my_assistants.data:
        if assistant.name == OPENAI_ASSISTANT_NAME:
            my_assistant = assistant
            break
    # Found?
    if my_assistant:
        my_assistant = client.beta.assistants.update(
            my_assistant.id,
            instructions=OPENAI_ASSISTANT_INSTRUCTIONS,
            model=OPENAI_ASSISTANT_MODEL
        )
        print(f"Assistant ${OPENAI_ASSISTANT_NAME} has been found at id: {my_assistant.id}, edit at: https://platform.openai.com/playground/assistants?assistant={my_assistant.id}")
    # Not found?
    else:
        my_assistant = client.beta.assistants.create(
            instructions=OPENAI_ASSISTANT_INSTRUCTIONS,
            name=OPENAI_ASSISTANT_NAME,
            model=OPENAI_ASSISTANT_MODEL,
        )
        print(f"Assistant ${OPENAI_ASSISTANT_NAME} was created at id: {my_assistant.id}, edit at: https://platform.openai.com/playground/assistants?assistant={my_assistant.id}")

def load_thread():
    # Create new thread on every run
    global my_thread
    my_thread = client.beta.threads.create()
    print(f"Current thread id: {my_thread.id}, edit at: https://platform.openai.com/playground/assistants?thread={my_thread.id}")

def initialize():
    load_assistant()
    load_thread()

def reply(text):

    client.beta.threads.messages.create(
        thread_id=my_thread.id,
        role="user",
        content=text,
    )

    run = client.beta.threads.runs.create(
        thread_id=my_thread.id,
        assistant_id=my_assistant.id
    )

    while not run.status == "completed":
        print("Waiting for answer...")
        run = client.beta.threads.runs.retrieve(
            thread_id=my_thread.id,
            run_id=run.id
        )

    messages = client.beta.threads.messages.list(my_thread.id, order='desc', limit=1)
    return messages.data[0].content[0].text.value


initialize()