# 匯入所需程式庫
import cv2
from opencv_faceid import Config

# 載入 Config.HAAR_FACES 指定的層疊分類器
haar_faces = cv2.CascadeClassifier(Config.HAAR_FACES)

if __name__ == '__main__':
    # 取得攝像鏡頭位置
    cap = cv2.VideoCapture(0)

    # 設定攝像鏡頭捕捉區域
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


    # 開始循環偵測
    while True:
        # 捕捉 frame-by-frame
        ret, frame = cap.read()  # ret : 讀到的 frame 是正確的話會回傳 true

        # 將圖片灰階化
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # 按下 q 離開迴圈 (「1」表示停 1ms 來偵測是否使用者有按下q。若設定為「0」就表示持續等待至使用者按下按鍵為止)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # 開始辨識程序...begin

        # 1.判斷是否為單一人臉的圖片


        # 2.判斷 result 有無回傳值


        # 3.取得欲裁切的資料


        # 4.進行裁切放人臉圖片


        # 5.進行比對檢驗評估


        # 6.列印評估資訊


        # 7.判斷評估值 <= Config.POSITIVE_THRESHOLD


        # 結束辨識程序...end

        # 將 frame 顯示
        cv2.imshow('Recognition', frame)

    # 釋放資源
    cap.release()

    # 關閉所有視窗
    cv2.destroyAllWindows()
