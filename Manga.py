import cv2
import numpy as np


#画像読み込み
img = cv2.imread("Ramb.jpg")
screen = cv2.imread("Screen.png")

#グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
th1 = 60
th2 = 120

# スクリーントーン画像を入力画像と同じ大きさにリサイズする
screen = cv2.resize(screen,(gray.shape[1],gray.shape[0]))

#輪郭検出し、色反転することで輪郭線を黒にする
med = np.median(img)
sigma = 0.33
min_val = int(max(0,(1.0 - sigma) * med))
max_val = int(max(255,(1.0 - sigma) * med))
    
edge = 255 - cv2.Canny(gray, min_val, max_val)

#三値化
gray[gray <= th1] = 0
gray[gray >= th2] = 255
gray[ np.where((gray > th1) & (gray < th2)) ] = screen[ np.where((gray > th1)&(gray < th2)) ]

#三値画像と輪郭画像を合成
manga_im = cv2.bitwise_and(gray, edge)
    
#結果を出力
cv2.imwrite("output.jpg", manga_im)
cv2.imshow("img",img)  
cv2.imshow("manga",manga_im)
cv2.waitKey(0)
cv2.destroyAllWindows()