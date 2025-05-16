import openai
import os
query = " 2 + 2 x 3 = ? "
client = openai.OpenAI(
    api_key=os.getenv("GPT_API_KEY"),
)

def cot_prompt(query):
  prompt = f""" 다음 문제를 단계별로 풀어주세요. 각 단계를 번호로 굽누하고 최종 답변을 명확하게 제시하세요
  {query}
  1. 문제 분석
  2. 계산
  3. 답변 확인
  """

  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "단계별로 문제를 해결하려는 논리적인 시스템입니다."},
          {"role": "user", "content":prompt},
      ],
      max_tokens = 150,
      temperature=0.7

  )
  return response.choices[0].message.content
result = cot_prompt(query)
print(result)

# 검증
expected_answer = "8"
if expected_answer in result:
  print("검증 성공")
else:
  print("검증 실패")