import cv2

#1. 이미지
img= cv2.imread('images/dog3.jpg')
cv2.imshow('o img', img)

#이미지의 크기 고정
#1) 고정 크기 지정
img2= cv2.resize(img, (300, 500)) 
cv2.imshow('r img', img2)

#2) 비율 크기 지정
img3=cv2.resize(img, None, fx=1.3, fy=1.5, interpolation=cv2.INTER_LINEAR) #두번째 파라미터인 크기인자를 None, 보간법 LINEAR : 이웃 2*2(4개)픽셀의 평균 픽샐로 빈 픽셀 채움
cv2.imshow('resize img2', img3)

img4=cv2.resize(img, None, fx=1.3, fy=1.5, interpolation=cv2.INTER_CUBIC) #두번째 파라미터인 크기인자를 None, 보간법 LINEAR : 이웃 4*4(16개)픽셀의 평균 픽샐로 빈 픽셀 채움
cv2.imshow('resize img2', img4)

img5=cv2.resize(img, None, fx=1.3, fy=1.5, interpolation=cv2.INTER_AREA) #크기 줄일 때
cv2.imshow('resize img2', img5)

#2. 동영상
cap= cv2.VideoCapture('videos/dog.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 프레임 크기 조정
    frame_resize= cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    if cv2.waitKey(1) == ord('1'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()