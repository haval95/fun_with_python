import cv2
import glob

images = glob.glob("*.jpg")

for img in images:
    img1 = cv2.imread(img,0)
    rs = cv2.resize(img1,(100,100))
    cv2.imshow("hey",rs)
    cv2.waitKey(40)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+img, rs)