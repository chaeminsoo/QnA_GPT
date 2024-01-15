# QnA GPT

<p align="center"><img width="150" alt="image" src="https://github.com/chaeminsoo/FAQ_GPT/assets/79351899/9dd08192-b6d2-453b-b342-ce0b68944b6e"></p>


## Overview
입력한 문서(데이터)를 기반으로, LLM이 질문에 대한 답변을 생성합니다.  
문서 내 필요한 정보를 빠르게 찾거나, 질문을 통해 문서에 대한 이해도를 높힐 수 있습니다.  

해당 Repository에서는 "경북대학교 도서관 FAQ"의 일부를 데이터로 사용하여, FAQ 봇을 구현했습니다.  
(※ 데이터가 바뀔 경우, Prompt와 일부 코드를 수정해야 합니다.)

## Features

- Retrieval Augmented Generation (RAG)
    - 답변을 생성하기 전, 사용자의 요청과 관련된 지식을 Vector DB에서 검색
    - 검색한 지식에 기반하여 답변을 생성
    - Halluciation(환각) 감소
- Vector Seach
    - Vector DB에서 사용자의 요청과 관련된 지식을 검색
    - 효율적인 검색을 위해 K-D Tree 구조 사용
- Function Calling
    - 사용자의 요청이 Vector Seach를 필요로 할 경우, Vector Seach에 필요한 argument를 제공
    - 불필요한 Vector Seach 예방

## Architecture

<p align="center"><img width="814" alt="image" src="https://github.com/chaeminsoo/FAQ_GPT/assets/79351899/99cbfa47-c2db-4877-a696-a667a52e6ef5"></p>

## Usage
``` bash
$ pip install -r requirements.txt
```
``` bash
$ python main.py
```
<br>
<p align="center"><img width="619" alt="image" src="https://github.com/chaeminsoo/coding_test/assets/79351899/407e42b2-f784-4110-af5b-b09303c9219b"></p>
<br>

- 입력한 문서(도서관 FAQ)를 기반으로, 질문에 대한 답변을 생성합니다.
- 입력한 문서에서 찾을 수 없는 내용은 추측하지 않습니다.(RAG)
- 필요한 경우에만 Vector Search를 합니다. (Function Calling)

## Details
- Author : [채민수](https://github.com/chaeminsoo)
- 언어 : Python
- LLM : OpenAI GPT
- 작업 기간 : 2024.01.10 ~ 2024.01.13
