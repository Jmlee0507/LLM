# start
```
가상환경 생ㅓ
git clone https://github.com/sknetworks20250226/django.git
pip install django
python manage.py migrate
django-admin createsuperuser  --> id/pw 설정
python manage.py runserver
localhost:8000/admin --> 테스트용 question 데이터 생성
```


# Migration
```
model이 새로 생성되거나 변경된 경우 DB를 갱신해야 하는데,
makemigration -> migration 해서 반영을 한다

처음에 DB만 생성했기 때문에 migration 해야 기본 테이블들이 만들어진다
```