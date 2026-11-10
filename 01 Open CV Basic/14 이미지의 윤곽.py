# 윤곽선(contour) : 경계선을 연결한 선

import cv2

img= cv2.imread('images/card.png')
cv2.imshow('card img', img)
#-----
#1) 흑백이미지로 단순화. 윤곽을 찾을 때 색상정보는 필요없으니..
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray card img', gray)

#2) 이진화를 위해 오츠알고리즘 사용
ret, otsu= cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('otch img', otsu)

#3) 이진화된 이미지에서 개체의 외곽선 정보 추출
contours, hierachy= cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#contours : 윤곽선 정보, hierachy: 윤곽선 계층 구조
#cv2.RETR_EXTERNAL : 가장 외곽의 윤곽만 추출
# cv2.CHAIN_APPROX_NONE : 윤곽선을 구성하는 근사화 방법지정. 모든 점들을 압축없이. 그대로 저장.

#윤곽선 정보를 기반으로 원본이미지에 윤곽선 그리기
target_img= img.copy() #원본칼라 이미지를 복제

# 윤곽선을 그릴 색상 지정
COLOR= (0,225,0) #녹색
# cv2.drawContours(image=target_img, contours=contours, contourIdx=0, color=COLOR) #윤곽 중 첫 윤곽만 그리기
cv2.drawContours(image=target_img, contours=contours, contourIdx=-1, color=COLOR) # -1 하면 전원 다!
cv2.imshow('contours image', target_img)

#윤곽선을 통해 개체의 위치를 식별하는 사각형 영역 : bounfing box
for contour in contours:
    x, y, width, hight = cv2.boundingRect(contour)
    cv2.rectangle(target_img, (x,y), (x+width,y+hight), COLOR, thickness=2) #사각형의 좌상단좌표, 우하단 좌표

cv2.imshow('bounding box image', target_img)

#윤곽선의 면적을 이용하여 일정 크기 이상만 검출하도록.
target_img2= img.copy()

for contour in contours:
    if cv2.contourArea(contour)>250:
        x, y, width, hight = cv2.boundingRect(contour)
        cv2.rectangle(target_img2, (x,y), (x+width,y+hight), COLOR, thickness=3)

cv2.imshow('bounding box image', target_img2)

#-----
cv2.waitKey(0)
cv2.destroyAllWindows()