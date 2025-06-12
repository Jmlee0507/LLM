# 요청 / 응답 모델 정의
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    # ORM 객체를 직렬화할 수 있도록 ==> DB에서 가져온 객체를 
    class Config:
        from_attributes = True

#상품 등록 데이터객체
class ProductCreate(BaseModel):
    name: str
    price: int

class ProductOut(BaseModel):
    name: str
    price: int
    class Config: # 객체로 리턴할 때
        from_attributes = True

class CartItem(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderRequest(BaseModel):
    user_id: int

class OrderOut(BaseModel):
    id: int
    user_id: int    
    product_id: int
    quantity: int
    class Config:   # 객체로 리턴할때
        from_attributes = True     