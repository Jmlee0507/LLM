# R&R(Role and Responsibility) - 업무분장을 위한 역할분담 문서
# 도서관리 API + Swagger UI로 문서 자동화 및 테스트 환경구성
# GET / books : 조회
# POST / book : 등록
# 옵져벼 패턴을 적용 -> 새 도서 추가, RA시스템 검색 모듈에 알림

# python trend는 데이터 타입 검사를 강하게 하는 추세... -> pydantic
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List, Dict
import uvicorn # Swagger UI를 지원하는 서버

# pydantic 모델 정의
class Book(BaseModel):
    id : int
    title : str

class BookCreate(BaseModel):
    title : str

# 샘플 데이터
books = [
    Book(id=1, title = "llm study"),
    Book(id=2, title = "python study"),
]

# 옵저버 패턴 구현
class Subject:
    def __init__(self) -> None:
        self._observer = []
    def add_observer(self,obs):
        self._observer.append(obs)
    def notify(self,message):
        for obs in self._observer:
            obs.update(message)

class Observer: # 추상화(다양한 옵저버 대상 클래스들을 커버)
    def update(self, message):
        raise NotImplementedError

# 옵저버 ... RAG 시스템의 검색메소드
class SearchModule(Observer): #RAG
    def update(self,message):
        print(f'RAG 검색모듈: {message}, 인덱스 업데이트')

# BookManager (Subject 상속)
class BookManager(Subject):
    # 책 추가
    def add_book(self, book: BookCreate):
        new_id = max(b.id for b in books) + 1
        new_books = Book(id = new_id, title = book.title)
        books.append(new_books)
        self.notify(f'새로운 도서 추가 : {new_books.title}')

# API엔드 포인트
book_manager = BookManager()
search_module = SearchModule()
book_manager.add_observer(search_module)

app = FastAPI()
@app.get("/",tags=['Swagger UI'])
def intro():
    return RedirectResponse(url="/docs")
# 호출
@app.get("/books", response_model = List[Book], tags = ['Books'])
def get_books():
    return books

@app.post('/book', response_model = Book, tags=['Books'])
def create_book(book:BookCreate):
    return book_manager.add_book(book)

# 실행은 터미널에서 uvicorn 파이썬파일명:app --reload 
