from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator



def index(request):
    page = request.GET.get('page',1)
    questions = Question.objects.order_by('-created_at')
    paginator = Paginator(questions, 10) # Paginator 객체 생성, 한 페이지에 10개
    paginated_questions = paginator.get_page(page)

    return render(request, 'board/index.html', {'questions':paginated_questions}) # 템플릿 폴더 안에 앱/파일.html 로 관리

def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'board/detail.html', {'question':question}) 

def create_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id) # 주어진 Id로 조회
    Answer(question=question, #answer의 question은 FK이기 때문에 알아서 question의 id가 들어감
           content = request.POST.get('content')).save()
    return redirect('board:question_detail', question_id=question.id)

def create_question(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        Question(subject=subject, content=content).save()
        return redirect('board:question_list')
    return render(request, 'board/create_question.html')

# 임시로 Question 객체를 100개 생성하는 뷰
def test(request):
    # Question 객체 100개 생성
    for i in range(1,101):
        Question(
            subject=f'질문 {i}', 
            content=f'질문 내용 {i}').save()
    return HttpResponse('100개의 질문이 생성되었습니다.')