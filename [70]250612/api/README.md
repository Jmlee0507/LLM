

# API 명세서

| 기능           | 메서드 | 엔드포인트             | 설명                        |
| -------------- | ------ | ---------------------- | --------------------------- |
| 회원가입폼     | GET    | `/api/register`        | 회원가입 페이지 제공        |
| 회원가입       | POST   | `/api/register`        | 사용자 정보 DB 저장         |
| 로그인         | POST   | `/api/login`           | 사용자 인증 및 세션 관리    |
| 상품목록조회   | GET    | `/api/products`        | 전체 상품 조회              |
| 상품등록       | POST   | `/api/products`        | 관리자용 상품 등록          |
| 장바구니 담기  | POST   | `/api/cart`            | 사용자별 장바구니 추가      |
| 장바구니 조회  | GET    | `/api/cart?user_id=1`  | 특정 사용자의 장바구니 조회 |
| 주문 요청      | POST   | `/api/order`           | 장바구니 상품 주문 처리     |
| 주문 목록 조회 | GET    | `/api/order?user_id=1` | 사용자 주문 내역 조회       |


# FAST API 설치
```
pip install fastapi uvicorn sqlalchemy
```

# 실행 코드
```
uvicorn main:app --reload
```

# 통신 및 응답 규약

| 항목       | 내용 |
|------------|------|
| **통신 방식** | 모든 요청/응답은 JSON 포맷 사용 |
| **인증 방식** | 쿠키, 세션 미사용. 로그인 시 반환된 `user_id`를 클라이언트 (JavaScript 변수 등) 에 저장하여 이후 인증에 활용 |
| **성공 응답 포맷** | `{ "success": true, "data": ... }` |
| **에러 응답 포맷** | `{ "success": false, "error": "에러 메시지" }` |
| **에러 처리 방식** | 모든 에러는 위 통일된 에러 응답 포맷 사용 |

# Fast API로 구현한 API와 HTML을 연결하려면
```
main.py가 실행 중인 폴더의 하위에 templates 폴더를 만들고 html파일을 저장한다
```