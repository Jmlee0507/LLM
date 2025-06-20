# 🐳 Docker 시작하기 (Flask 예제)

## 1️⃣ 사전 준비
1. Docker Desktop 설치
2. 시스템 재부팅
3. VSCode에서 작업 폴더 생성 및 터미널 사용

### ✅ Docker 설치 확인
```bash
docker --version
```

---

## 2️⃣ Flask 앱 구성

### 📄 `app.py`
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 📄 `requirements.txt`
```txt
flask==3.1.1
```

---

## 3️⃣ Dockerfile 작성

### 📄 `Dockerfile`
```Dockerfile
# 베이스 이미지 설정
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY app.py .

# 컨테이너 시작 시 실행할 명령어
CMD ["python", "app.py"]
```

---

## 4️⃣ Docker 명령어

### 🏗 이미지 빌드
```bash
docker build -t myapp:latest .
```

### 🚀 컨테이너 실행
```bash
docker run -d -p 5000:5000 myapp
```

### 🌐 브라우저에서 확인
```
http://localhost:5000
또는
http://127.0.0.1:5000
```

---

## 5️⃣ 추가 명령어

### 🔍 실행 중인 컨테이너 확인
```bash
docker ps
```

### ⛔️ 컨테이너 중지
```bash
docker stop <CONTAINER ID>
```

### 🐳 Docker Desktop을 이용해 시각적으로 컨테이너 및 이미지 확인 가능
