from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv

load_dotenv()
def qa_view(request):
    answer = None
    if request.method == 'POST':
        question = request.POST.get('question') # 폼에서 가져온다
        response = openai.chat.completions.create(
            model = 'gpt-4o',
            messages = [
                {'role':'user', 'content': question}
            ]
        )
        answer = response.choices[0].message.content
    return render(request, 'qa/index.html', {'answer':answer})
