import vector_db
import prompt

# 답변의 기반이 될 자료 불러오기
# Vector DB 구축
vec_db_with_content, idx = vector_db.make_vector_db('knu_library_faq_example.csv')

input_question = input('무엇이 궁금하세요? : ')

# 입력 질문 임베딩
input_question_vec = vector_db.get_embedding(input_question)

# Vector Search
search_result = vector_db.search(input_question_vec,vec_db_with_content,idx)

# 답변 생성
response = prompt.make_respense(input_question,search_result['answer'])
print(">>> ",response)