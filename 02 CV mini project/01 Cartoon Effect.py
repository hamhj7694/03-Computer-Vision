import cv2

# 원본이미지
img=cv2.imread("01 Open CV Basic/images/woman.jpg")
cv2.imshow('원본', img)

#색상 단순화
#평균이동(meanshift)
color= cv2.pyrMeanShiftFiltering(
    img,
    sp=20, #주변 픽셀을 탐색하는 공간 범위
    sr=40, #색상이 비슷하다고 판단하는 범위
)
cv2.imshow('cartoon color img', color)

# 조금 더 만화처럼 보이도록 윤곽선을 그려내기
#1) 흑백으로
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#2) 잔털이나 잡털 등 노이즈 제거하기 위해 블러처리
blur=cv2.GaussianBlur(gray, (9, 9), 0) #9*9 필터 사용
cv2.imshow('blur', blur)
#3) 주요 경계선 검출
adges= cv2.Canny(blur, 80, 160)
cv2.imshow('edges image', adges)
#4) 주요 경계선을 검정색으로 표시(카툰의 선처럼)
cartoon= color.copy()
cartoon[adges>0] = (10,10,10) #어두운 BGR
cv2.imshow('cartoon', cartoon)

# 결과 저장
cv2.imwrite('cartoon.jpg', cartoon)

#-----
cv2.waitKey(0)
cv2.destroyAllWindows()