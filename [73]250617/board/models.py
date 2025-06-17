from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200) # 질문 제목
    content = models.TextField() # 질문 내용
    created_at = models.DateTimeField(auto_now_add = True) # 생성 시간
    updated_at = models.DateTimeField(auto_now = True) # 수정 시간

    def __str__(self):
        return self.subject # 객체를 문자열로 표현할 때 제목을 반환

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #답변 제목
    content = models.TextField() # 답변 내용
    created_at = models.DateTimeField(auto_now_add = True) # 생성 시간
    updated_at = models.DateTimeField(auto_now = True) # 수정 시간  