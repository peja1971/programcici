import cv2
import numpy as np

def nothing(x):
    pass
img = np.zeros([250,250,3], np.uint8)
def main():

    window_name='bgr'
    cv2.namedWindow(window_name)
    cv2.createTrackbar('h',window_name,1,180,nothing)
    cv2.createTrackbar('s',window_name,1,255,nothing)
    cv2.createTrackbar('v',window_name,1,255,nothing)
    while(1):
        h = int(cv2.getTrackbarPos('h',window_name))
        s = int(cv2.getTrackbarPos('s',window_name))
        v = int(cv2.getTrackbarPos('v',window_name))
        
        img[0:250,0:250] = [h,s,v]

        bgr = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        
        cv2.imshow('hsv', img)
        cv2.imshow('bgr', bgr)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
    cv2.destroyAllWindows()


#Run Main
if __name__ == "__main__" :
    main()