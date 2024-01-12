import os
import csv
from openai import OpenAI

openAIclient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text, model='text-embedding-ada-002'):
    response = openAIclient.embeddings.create(input=text, model=model)
    # response = (data, model, object, usage=(토큰 몇개 썼는지))
    # data = [Embedding(embedding=[벡터값], index=0, object='embedding')]
    
    vector = response.data[0].embedding
    return vector


def load(file_path):
    vec_db = []
    with open(file_path, 'r', encoding='utf-8') as f:
        csv_f = csv.reader(f)
        next(csv_f) # header row 생락

        for row in csv_f:
            # id, question, answer
            text = 'Question: ' + row[1] + "\nAnswer: " + row[2] + '\n'
            vector = get_embedding(text)
            doc = {
                    'id' : row[0],
                    'vector' : vector,
                    'question' : row[1] ,
                    'answer' : row[2]
            }
            vec_db.append(doc)
    
    return vec_db