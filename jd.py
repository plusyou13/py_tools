#!/usr/bin/python3
# coding:utf-8
from urllib import request
from urllib.error import HTTPError
import json
import re
import pandas as pd
HEADER = {
    "Accept": "*/*"
}

# 评论接口
URL = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={productId}&score={score}&sortType=5&page={page}&pageSize=10&isShadowSku=0&rid=0&fold=1"
# 字符编码
DECODE = "GBK"


def fetch_json(productId: str, page: str = 1, score: str = 0) -> dict:
    """
    page:第page页
    score：按分数查询
    """
    url = URL.format(
        productId=str(productId),
        page=str(page),
        score=str(score),
    )
    req = request.Request(url, headers=HEADER)
    rep = request.urlopen(req).read().decode(DECODE, errors="ignore")
    dict_ = re.findall(r"\{.*\}", rep)[0]
    return json.loads(dict_)


if __name__ == "__main__":
    # 以https://item.jd.com/100009177400.html的商品页为例
    for k in range(10):
        comment_dict = fetch_json(productId="100009177400", page=k, score=0)
        #pd.DataFrame(comment_dict).to_csv('jd_comment.csv')
        # with open('jd_comment.json','w')as f:
        #         f.write(comment_dict)
        for i in comment_dict["comments"]:
            with open('jd_comment.json','w')as f:
                f.write(i["content"])
                
            print(i["content"])
        pass