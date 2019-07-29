# 安裝 py-opencv
import cv2

print(cv2.__version__)
# 人臉偵測器
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')

# 設定攝像鏡頭
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # 捕捉 frame-by-frame
    ret, frame = cap.read()  # ret : 讀到的 frame 是正確的話會回傳 true

    # 將 frame 顯示
    cv2.imshow('Video', frame)

    # 按下 q 離開迴圈 (「1」表示停 1ms 來偵測是否使用者有按下q。若設定為「0」就表示持續等待至使用者按下按鍵為止)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源與關閉視窗
cap.release()
cv2.destroyAllWindows()
