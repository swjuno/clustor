import os
import sys
import requests
import json


def naver_face_detect(file):
    client_id = "dV27NKE5bKj969JZ39wp"
    client_secret = "pJXUIqD3Ti"
    url = "https://openapi.naver.com/v1/vision/face"
    # url = "https://openapi.naver.com/v1/vision/celebrity" // 유명인 얼굴인식
    files = {'image': open(file, 'rb')}
    headers = {'dV27NKE5bKj969JZ39wp': client_id, 'pJXUIqD3Ti': client_secret}
    response = requests.post(url, files=files, headers=headers)
    rescode = response.status_code
    if (rescode == 200):
        # print(response.text)
        data = json.loads(response.text)
        return data
    else:
        # print("Error Code:" + rescode)
        return None
