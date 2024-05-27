from fastapi.testclient import TestClient
from main import settings

from main import app

client = TestClient(app)


def test_keywords_textrank():
    input_sentence = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
    algo_type = "TextRank"
    response = client.post(
        f"{settings.API_V1_STR}/algo/keywords",
        json={"input_sentence": input_sentence, "algo_type": algo_type},
    )

    assert 200 <= response.status_code < 300
    result_list = response.json()["data"]["keywords_list"]
    assert len(result_list) != 0


def test_keywords_TFIDF():
    input_sentence = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
    algo_type = "TextRank"

    response = client.post(
        f"{settings.API_V1_STR}/algo/keywords",
        json={"input_sentence": input_sentence, "algo_type": algo_type},
    )

    assert 200 <= response.status_code < 300
    result_list = response.json()["data"]["keywords_list"]
    assert len(result_list) != 0


def test_keywords_nodata():
    input_sentence = "1"
    algo_type = "TextRank"

    response = client.post(
        f"{settings.API_V1_STR}/algo/keywords",
        json={"input_sentence": input_sentence, "algo_type": algo_type},
    )

    assert response.status_code == 404
