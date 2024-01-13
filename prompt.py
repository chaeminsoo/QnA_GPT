import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

openAIclient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def make_respense(q, info, temperature=0, max_tokens=1024):
    prompt = f"""
    You are a librarian.

    Answer the following question based only on the information given.

    If the given information is not enough to answer the question, just say you do not have enough information, Do not say anything else.

    Question : {q}

    Given information : {info}
    """

    respense = openAIclient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role" : "system",
                "content" : "Create your respense in Korean."
            },
            {
                "role" : "user",
                "content" : prompt
            }
        ],
        temperature = temperature,
        max_tokens = max_tokens
    )

    return respense.choices[0].message.content


def take_input(user_input):
    functions = [
        {
            "name":"make_respense",
            "description":"Generates responses to questions related to the library.",
            "parameters":{
                "type":"object",
                "properties":{
                    "q" : {
                        "type": "string",
                        "description": "The question that asked."
                    }
                },
                "required":["q"]
            }
        }
    ]

    result = openAIclient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role" : "user",
                "content" : user_input
            }
        ],
        functions=functions,
        function_call='auto',
        temperature = 0,
        max_tokens = 1024
    )

    return result.choices[0].message



