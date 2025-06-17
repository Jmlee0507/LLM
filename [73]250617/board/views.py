from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer



def index(request):
    questions = Question.objects.order_by('-created_at') # 질문을 생성시간 기준 내림차순 정렬
    return render(request, 'board/index.html', {'questions':questions}) # 템플릿 폴더 안에 앱/파일.html 로 관리

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'board/detail.html', {'question':question}) 
