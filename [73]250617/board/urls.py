from django.urls import path
from . import views

urlpatterns = [
    # ''으로만 쓰여있지만, 사실 config에 정의된 'board/' 이하의 링크임.
    path('', views.index), # board 앱의 index 뷰를 기본 URL로 설정
    path('test/abc/', views.test),
]