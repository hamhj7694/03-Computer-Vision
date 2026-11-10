# 이미지 이진화 - 모든 픽셀을 1,0으로 변경
# 특정 값을 기준으로 0, 1 분류. 흑백이 명확해서 글씨 같은 것 식별이 용이함.

import cv2
img= cv2.imread('images/sudoku.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('sudoku img', img)

#흑백으로 구분한 임계값
threshold= 127 #255의 절반

#1) 이미지를 이진화 [조명이 균일할 때 방법] - 임계값 기준으로 0,1 을 분류
ret, thresh= cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY) #리턴 값(실제 사용된 임계값, 적용된 이미지)
cv2.imshow('thresh img', thresh)

#2) 이미지의 최적의 임계값을 알아서 적용하는 기법 -- 오츠알고리즘
ret, otsu= cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('otch', otsu)
print('오츠 최적 임계값 :', otsu)

#3) 적응형 이진화 - 가우시안 분표 활용
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# 블록 윈도우[11*11] 단위로 임계값 계산
cv2.imshow('thresh2', thresh2)

#[불균형할 때 방법]

#-----
cv2.waitKey(0)
cv2.destroyAllWindows()