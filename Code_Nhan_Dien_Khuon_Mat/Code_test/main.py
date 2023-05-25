
import cv2
import face_recognition

#1 chúng ta sẽ phải chuyển hình ảnh sang BGR (Blue,green,Red) vì
#thư viện hiểu như vậy
"""
OpenCV đọc hình ảnh ở định dạng BGR (thay vì RGB) vì khi OpenCV lần đầu tiên được phát triển,
định dạng màu BGR đã phổ biến trong các nhà sản xuất máy ảnh và nhà cung cấp phần mềm hình ảnh.
Kênh màu đỏ được coi là một trong những kênh màu kém quan trọng nhất, 
vì vậy nó được liệt kê cuối cùng và nhiều ảnh bitmap sử dụng định dạng BGR để lưu trữ hình ảnh. 
Tuy nhiên, hiện nay tiêu chuẩn đã thay đổi và hầu hết các phần mềm hình ảnh và máy ảnh 
sử dụng định dạng RGB, đó là lý do tại sao trong các chương trình, ban đầu bạn nên chuyển 
đổi hình ảnh BGR sang RGB trước khi phân tích hoặc thao tác với bất kỳ hình ảnh nào.
"""
# step 1 :
imgElon = face_recognition.load_image_file("pic/elon musk.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgCheck = face_recognition.load_image_file("pic/elon check.jpg")
imgCheck = cv2.cvtColor(imgCheck, cv2.COLOR_BGR2RGB)

# Xác đinh vị trí khuôn mặt cần nhận dạng
faceloc = face_recognition.face_locations(imgElon)[0]
print(faceloc) #(y1,x2,y2,x1)
encodeElon = face_recognition.face_encodings(imgElon)[0] # mã hóa ảnh
cv2.rectangle(imgElon, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 255), 2)

faceCheck = face_recognition.face_locations(imgCheck)[0]
encodeCheck = face_recognition.face_encodings(imgCheck)[0] # mã hóa ảnh
cv2.rectangle(imgCheck, (faceCheck[3], faceCheck[0]), (faceCheck[1], faceCheck[2]), (255, 0, 255), 2)

# nó sẽ so sánh hình ảnh mã hóa với các điểm trên khuôn mặt xem có khớp o
results = face_recognition.compare_faces([encodeElon],encodeCheck)
print(results) # Kết quả True

# tuy nhiên khi có nhiều hình ảnh thì chúng ta cần phải biết
# khoảng cách (sai số) giữa các bức ảnh là bao nhiêu?
faceDis = face_recognition.face_distance([encodeElon],encodeCheck)
print(results,faceDis)
#
cv2.putText(imgCheck, f"{results}{(1-(round(faceDis[0],2)))*100}{'%'}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cap = cv2.VideoCapture(0)

cv2.imshow("Elon", imgElon)  # view thử ảnh để kiểm tra
cv2.imshow("ElonCheck", imgCheck) # view thử ảnh
cv2.waitKey()
cv2.destroyAllWindows()  # thoát tất cả các cửa sổ