from django.urls import path
from . import views

# 네임 스페이스
# 사용할때는 board:question_list 와 같이 사용
app_name = 'board' # board 앱의 Url 네임스페이스 설정

urlpatterns = [
    # ''으로만 쓰여있지만, 사실 config에 정의된 'board/' 이하의 링크임.
    path('', views.index, name='question_list'), # board 앱의 index 뷰를 기본 URL로 설정
    # <a href = '/board/{{ question.id }}'> 로 되어있으니 맨 앞에 바로 question_id 넣기
    path('<int:question_id>/', views.detail, name='question_detail'), # 질문 상세 페이지 URL 
    path('ask/create/<int:question_id>/', 
         views.create_answer, name='create_answer'),
    path('question/create/', views.create_question, name='create_question'),
    # 임시
    path('test/', views.test, name='text')
]