import urllib.request
import cv2
import face_recognition
import os
import numpy as np


# step 1 load ảnh từ kho ảnh nhận dạng


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

#step encoding
def Mahoa(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #BGR được chuyển đổi sang RGB
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnow = Mahoa(images)
print("ma hoa thanh cong")
print(len(encodeListKnow))

#khởi dộng webcam
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.43.235/cam-lo.jpg')
#url = "http://192.168.2.41/320x240.jpg"

while True:
    #response = urllib.request.urlopen(url)
    #img_array = np.array(bytearray(response.read()), dtype=np.uint8)
    #frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)


    ret, frame= cap.read()
    framS = cv2.resize(frame,(0,0),None,fx=0.5,fy=0.5)
    framS = cv2.cvtColor(framS, cv2.COLOR_BGR2RGB)

    # xác định vị trí khuôn mặt trên cam và encode hình ảnh trên cam
    facecurFrame = face_recognition.face_locations(framS) # lấy từng khuôn mặt và vị trí khuôn mặt hiện tại
    encodecurFrame = face_recognition.face_encodings(framS)

    for encodeFace, faceLoc in zip(encodecurFrame,facecurFrame): # lấy từng khuôn mặt và vị trí khuôn mặt hiện tại theo cặp
        matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis) #đẩy về index của faceDis nhỏ nhất


        if faceDis[matchIndex] <0.50 :
            name = classNames[matchIndex].upper()
            print("Đúng")
        else:
            name = "Unknown"
            print("Sai")

        #print tên lên frame
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
        cv2.rectangle(frame,(x1,y1), (x2,y2),(0,255,0),2)
        #cv2.rectangle(frame, (x1, y1 - 35), (x2, y1), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, name, (x1 + 6, y1 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        # cv2.putText(frame,name,(x2,y2),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        if name == "Unknown":
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('.', frame)
    if cv2.waitKey(1) == ord("q"):  # độ trễ 1/1000s , nếu bấm q sẽ thoát
        break
cap.release()  # giải phóng camera
cv2.destroyAllWindows()  # thoát tất cả các cửa sổ

