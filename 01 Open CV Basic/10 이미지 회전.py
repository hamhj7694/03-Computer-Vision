import cv2

img= cv2.imread('images/dog3.jpg')
cv2.imshow('원본', img)

img2=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #시계방향 90도
cv2.imshow('rotat_90', img2)

img3=cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) #반시계방향 90도
cv2.imshow('rotat_90', img3)

img4=cv2.rotate(img, cv2.ROTATE_180) #180도
cv2.imshow('rotat_90', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()