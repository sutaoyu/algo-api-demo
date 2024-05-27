from pydantic.generics import GenericModel
from typing import Any, Generic, List, Optional, TypeVar, Dict
from pydantic import BaseModel, ValidationError, validator
from datetime import datetime
from enum import Enum, IntEnum

T = TypeVar("T")


class ResponseModel(GenericModel, Generic[T]):
    code: int
    data: T
    msg: str


class MultiResponseModel(GenericModel, Generic[T]):
    data_list: List[T]
    pages: int
    total: int
