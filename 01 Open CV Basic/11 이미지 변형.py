import cv2

img= cv2.imread('images/dog3.jpg')
img= cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
cv2.imshow('원본', img)

#1) 불러온 이미지 흑백으로 변경시키기
img2= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('2', img2)

#2) 이미지 블러처리(흐리게_
#2.1) 필터(커널) 이용 방법
kernel_3 = cv2.GaussianBlur(img, (3,3), 0) # 필터크기, 표준편차(시그마) 값
kernel_5 = cv2.GaussianBlur(img, (5,5), 0) # 필터크기, 표준편차(시그마) 값
kernel_7 = cv2.GaussianBlur(img, (7,7), 0) # 필터크기, 표준편차(시그마) 값
cv2.imshow('kernel_3', kernel_3)
cv2.imshow('kernel_5', kernel_5)
cv2.imshow('kernel_7', kernel_7)

#2.2 표준편차를 이용한 블러처리 -- 시그마
sigma1= cv2.GaussianBlur(img, (0,0), 1) #표준편차 1
sigma5= cv2.GaussianBlur(img, (0,0), 5) #표준편차 5
sigma10= cv2.GaussianBlur(img, (0,0), 10) #표준편차 10
cv2.imshow('sigma1', sigma1)
cv2.imshow('sigma5', sigma5)
cv2.imshow('sigma10', sigma10)

#3) 원근 변경 -- 이미지에 비스듬하게 찍힌 이미지를 원근을 조절하여 똑바로 세우기.[문서 스캐너]
img= cv2.imread('images/newspaper.jpg')
cv2.imshow('newspaper image', img)

#잘라낼 사이즈
width, height= 640, 240

#원본이미지에서 잘라낼 영역의 좌표들 준비
import numpy as np
src= np.array([[511,352],[1008,345],[1122,584],[455,594]], dtype=np.float32)
dst= np.array([[0,0],[width,0],[width,height],[0,height]], dtype=np.float32)

matrix= cv2.getPerspectiveTransform(src,dst)
result= cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow('newpaper transform', result)

#-------
cv2.waitKey(0)
cv2.destroyAllWindows()