import os
from openai import OpenAI

openAIclient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text, model='text-embedding-ada-002'):
    response = openAIclient.embeddings.create(input=text, model=model)
    # response = (data, model, object, usage=(토큰 몇개 썼는지))
    # data = [Embedding(embedding=[벡터값], index=0, object='embedding')]
    
    vector = response.data[0].embedding
    return vector