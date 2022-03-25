from fastapi import FastAPI
from typing import Optional

# 개발 서버 실행: uvicorn 명령어 사용
app = FastAPI()


# FastAPI 인스턴스 -> http method 별 데코레이터 제공
@app.get("/")
async def root():
    # 반환값: dict, list, str 등 가능
    return {"message": "Hello World"}


# 경로 매개변수: {}로 사용 가능 -> 데코레이터 대상 함수에 파라미터로 제공 + 타입 어노테이션으로 타입 체크도 가능
# express.js와 마찬가지로 경로 동작은 순서대로 평가 -> 순서 중요
@app.get("/hello/{number}")
async def say_hello(name: int):
    return {"message": f"Hello {name}"}


# 기본 경로 매개변수: 경로 저장 X -> :path로 해당 매개변수에 경로 형태 값이 올 수 있음을 명시 필요
@app.get("/path/{file_path:path}")
async def say_file_path(file_path: str):
    return {"message": f"file_path: {file_path}"}


# 쿼리 매개변수: 데코레이터 대상 함수의 파라미터로 제공
# optional 매개변수: optional 타입 어노테이션 (None을 기본값으로 지정 시 IDE에서 타입 에러 발생 방지), 기본값 (생략 시 대체값 & Fast API가 optional value임을 인지)
# 모두 지정 필요
@app.get("/query")
async def say_query(name: str, age: Optional[int] = None):
    return {"message": f"name: {name}, age: {age}"}
