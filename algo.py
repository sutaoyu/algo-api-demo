from typing import Any, List
from typing import Union
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from base import ResponseModel, MultiResponseModel
from enum import Enum

import jieba
import jieba.posseg
import jieba.analyse

router = APIRouter()


class KeyworkdsAlgoType(str, Enum):
    TF_IDF = "TF-IDF"
    Text_Rank = "TextRank"


class KeywordsInputBase(BaseModel):
    input_sentence: str
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
