from fastapi import APIRouter
from app.api import algo


api_router = APIRouter()

# 在下面新增router便于接口调用
api_router.include_router(algo.router, prefix="/algo", tags=["algo"])
