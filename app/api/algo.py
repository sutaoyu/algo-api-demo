from typing import Any, List
from typing import Union
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, validator
from enum import Enum
import jieba
import jieba.posseg
import jieba.analyse

from app.api.base import ResponseModel, MultiResponseModel


router = APIRouter()


class TextInputBase(BaseModel):
    input_sentence: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="需要处理的原始文本",
        example="我爱北京天安门💳 0 👤"
    )
    @validator('input_sentence')
    def validate_input(cls, v):
        if not v.strip():
            raise ValueError("输入文本不能为空或仅包含空白字符")
        return v


class KeyworkdsAlgoType(str, Enum):
    TF_IDF = "TF-IDF"
    Text_Rank = "TextRank"


# 集成自TextInputBase
class KeywordsInputBase(TextInputBase):
    algo_type: KeyworkdsAlgoType


class KeywordsOutputBase(KeywordsInputBase):
    keywords_list: list


def get_keywords(sentence, algo_type):
    keywords = []
    if algo_type == "TF-IDF":
        for keyword, _ in jieba.analyse.extract_tags(sentence, withWeight=True):
            keywords.append(keyword)
    elif algo_type == "TextRank":
        for keyword, _ in jieba.analyse.textrank(sentence, withWeight=True):
            keywords.append(keyword)
    return keywords


@router.post("/keywords", response_model=ResponseModel[KeywordsOutputBase])
def fetch_keywords(
    *,
    input: KeywordsInputBase,
) -> Any:
    """
    单个句子的关键词提取
    """
    try:
        keywords = get_keywords(input.input_sentence, input.algo_type)
        if not keywords:
            raise HTTPException(
                status_code=404, detail=f"keywords of {input.input_sentence} not found"
            )
        result = {
            "keywords_list": keywords,
            "input_sentence": input.input_sentence,
            "algo_type": input.algo_type,
        }
        return ResponseModel(code=200, msg="ok", data=result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"文本处理过程中发生错误: {str(e)}"
        )    
