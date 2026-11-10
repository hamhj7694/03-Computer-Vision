import cv2
img= cv2.imread('images/dog3.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#파일로 저장
result= cv2.imwrite('saved/img.jpg',img)
print('저장결과:', result)

#---
img2= cv2.imread('image/cat.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('saved/img2.png', img2)

#2. 동영상 저장
cap= cv2.VideoCapture('videos/dog_sd.mp4')
#동영상을 저장하려면 코덱이 필요함
fourcc= cv2.VideoWriter_fourcc(*'MP4V')
#four character code : 4글자 문자로 된 코덱 구분자

# 예) DIVX, XVID, MP4V, H264, NJPG
# .avi 예전에는 --> DIVX (예전거라서 요즘 플레이어들은 기본 설치 안 됨)
# .mp4 --> 웹, 데스크탑, 앱 모두 구동 가능한 코덱. 요즘 가장 대중적

# 원본과 같은 크기, 속도로 저장
width = cap.get(cv2.CAP_RPOP_FRAME_WIDTH)
height = cap.get(cv2.CAP_RPOP_FRAME_HEIGHT)
fps= cap.get(cv2.CAP_PROP_FPS) * 3
# 동영상의 너비는 정수만 가능
width=round(width)
height=round(height)

# 비디오 저장 객체 생성(저장할 곳의 파일명, 재생속도, 크기)
out = cv2.VideoWriter(filename='saved/output.mp4', fourcc=fourcc, fps=fps, frameSize=(width, height))

# 프레임 단위로 원봉세서 동영상을 가져와서 새로운 동영상으로 만들기
while cap.isOpened():
    ret, frame =cap.read() #한 프레임 읽기
    if not ret:
        break

    #한장 저장
    out.write(frame)
    cv2.imshow('dog video', frame) #장면확인하고 싶어서..
    if cv2.waitKey(33)==ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()