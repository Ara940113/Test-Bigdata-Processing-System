from collection import *

datas=[]
for i in range(1,21):
    naver_data = naver_craw(i+1)
    datas.append(naver_data)

mongo_save(mongo, datas, "greendb", "naverss")  # List안에 dict을 넣어야 함


