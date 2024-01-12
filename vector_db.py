import os
import csv
import numpy as np
from scipy.spatial import cKDTree
from openai import OpenAI

openAIclient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text, model='text-embedding-ada-002'):
    response = openAIclient.embeddings.create(input=text, model=model)
    # response = (data, model, object, usage=(토큰 몇개 썼는지))
    # data = [Embedding(embedding=[벡터값], index=0, object='embedding')]
    
    vector = response.data[0].embedding
    return vector


def make_vector_db(file_path):
    vec_db_with_content = []
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
            vec_db_with_content.append(doc)
            vec_db.append(vector)
    
    index = cKDTree(vec_db)
    
    return vec_db_with_content, index


def cosine_similarity(v1,v2):
    v1_norm = np.sqrt(np.sum(np.square(v1)))
    v2_norm = np.sqrt(np.sum(np.square(v2)))
    return np.dot(v1,v2)/(v1_norm*v2_norm)


def search(input_vec, db_with_content, idx):
    
    result = db_with_content[idx.query(input_vec)[1]]
    score = cosine_similarity(input_vec, result['vector'])

    final_result = {'id':result['id'], 'score':score, 'question':result['question'], 'answer':result['answer']}
    
    return final_result