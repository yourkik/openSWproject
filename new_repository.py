import os

def make_repository():
    if os.path.isdir("Crop_image")==False: #같은 이름의 폴더가 이미 있으면 작동하지 않게함(같은 이름의 폴더 존재시 에러발생)
        os.makedirs("Crop_image") #폴더 생성
        os.chdir("Crop_image") #해당 폴더로 이동