import urllib.request
import cv2
import face_recognition
import os
import numpy as np
import requests
import time
from PIL import ImageGrab
import random
import string


#step encoding
def Mahoa(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #BGR được chuyển đổi sang RGB
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def check_time(name):
    timeout = 3  # Thời gian timeout (s)
    start_time = time.time()
    url3 = "https://b8ee-116-105-23-40.ngrok-free.app/door_on"

    while True:
        if name == "Unknown":
            elapsed_time = time.time() - start_time
            if elapsed_time >= timeout:
                response = requests.get(url3)
                print("Unknown")
                break
        else:
            start_time = time.time()

        # Thực hiện các công việc khác trong vòng lặp nếu cần
        time.sleep(0.1)


def face_recognition_1():
    path = "pic2"
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        print(cl)
        curImg = cv2.imread(f"{path}/{cl}")
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
        # splitext sẽ tách path ra thành 2 phần, phần trước đuôi mở rộng và phần mở rộng
    print(len(images))
    print(classNames)



    encodeListKnow = Mahoa(images)
    print("ma hoa thanh cong")
    print(len(encodeListKnow))

    #khởi dộng webcam
    cap = cv2.VideoCapture(0)

    unknown_count = 0  # Biến đếm số lần `name` là "Unknown" liên tiếp
    threshold = 8  # Ngưỡng số lần liên tiếp để in ra "alo"

    while True:
        ret, frame= cap.read()
        framS = cv2.resize(frame,(0,0),None,fx=0.5,fy=0.5)
        framS = cv2.cvtColor(framS, cv2.COLOR_BGR2RGB)

        # xác định vị trí khuôn mặt trên cam và encode hình ảnh trên cam
        facecurFrame = face_recognition.face_locations(framS) # lấy từng khuôn mặt và vị trí khuôn mặt hiện tại
        encodecurFrame = face_recognition.face_encodings(framS)

        for encodeFace, faceLoc in zip(encodecurFrame,facecurFrame): # lấy từng khuôn mặt và vị trí khuôn mặt hiện tại theo cặp
            matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
            matchIndex = np.argmin(faceDis) #đẩy về index của faceDis nhỏ nhất


            if faceDis[matchIndex] <0.50 :
                name = classNames[matchIndex].upper()
            else:
                name = "Unknown"
            print(name)

            if name == "Unknown":
                unknown_count += 1
            else:
                unknown_count = 0

            url3 = "https://b8ee-116-105-23-40.ngrok-free.app/get_notifi"
            url4 = "https://b8ee-116-105-23-40.ngrok-free.app/get_not_notifi"
            if unknown_count >= threshold:
                response = requests.get(url3)
                unknown_count = 0
                time.sleep(3)
                response = requests.get(url4)

            #print tên lên frame
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
            cv2.rectangle(frame,(x1,y1), (x2,y2),(0,255,0),2)
            cv2.putText(frame,name,(x2,y2),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            if name == "Unknown":
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)




        cv2.imshow('Ga Lai Lap Trinh', frame)
        if (cv2.waitKey(1) == ord("q")): # độ trễ 1/1000s , nếu bấm q sẽ thoát
            break
        time.sleep(0.1)
    cap.release()  # giải phóng camera
    cv2.destroyAllWindows()  # thoát tất cả các cửa sổ

if (__name__ == "__main__"):

    print(face_recognition_1())
