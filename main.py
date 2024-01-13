import json
import vector_db
import prompt

# 답변의 기반이 될 자료 불러오기
# Vector DB 구축
vec_db_with_content, idx = vector_db.make_vector_db('knu_library_faq_example.csv')

print("질문을 입력하세요 (입력 없이 Enter 누를시, 종료됨)")

# 무한 루프 방지
cnt = 0

while cnt < 6:
    input_question = input('질문 : ')
    if input_question == "":
        break

    result = prompt.take_input(input_question)
    if result.function_call == None:
        print('>>> 도서관과 관련 없는 질문은 하지 말아 주십시오.')
    else:
        args = json.loads(result.function_call.arguments)
        # 입력 질문 임베딩
        input_question_vec = vector_db.get_embedding(args['q'])

        # Vector Search
        search_result = vector_db.search(input_question_vec,vec_db_with_content,idx)

        # 답변 생성
        response = prompt.make_respense(input_question,search_result['answer'])
        print(">>> ",response)
    cnt+=1