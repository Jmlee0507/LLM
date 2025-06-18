# Django 프로젝트 시작 가이드

## 1. 초기 설정

```bash
# 프로젝트 클론
git clone https://github.com/sknetworks20250226/django.git
cd django

# Django 설치
pip install django
```

(가상환경은 필요 시 생성)

---

## 2. DB 초기화 및 서버 실행

```bash
python manage.py migrate             # 기본 테이블 생성
django-admin createsuperuser        # 관리자 계정 생성
python manage.py runserver          # 서버 실행
```

- 관리자 페이지 접속: [localhost:8000/admin](http://localhost:8000/admin)  
- 로그인 후 테스트용 Question 데이터 생성

---

## 3. 모델 변경 시

```bash
python manage.py makemigrations     # 변경 사항 감지
python manage.py migrate            # DB에 적용
```

- 모델 생성/수정 시 꼭 위 명령어로 반영

---
