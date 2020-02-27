import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.ones((200,200,3), np.uint8)
output = np.ones((600,600,3), np.uint8)
ft = cv2.FONT_HERSHEY_SIMPLEX

def nothing(x):
    pass

def main():

    window_name='Colors'
    cv2.namedWindow(window_name)
    cv2.createTrackbar('B',window_name,1,255,nothing)
    cv2.createTrackbar('G',window_name,1,255,nothing)
    cv2.createTrackbar('R',window_name,1,255,nothing)
    while(1):
        b = (cv2.getTrackbarPos('B',window_name))
        g = (cv2.getTrackbarPos('G',window_name))
        r = (cv2.getTrackbarPos('R',window_name))
        color = [b,g,r]
        
        x=0
        y=0
        x1=199
        y1=199
        cv2.rectangle(img, (x,y), (x1,y1), color, -1)
        
        bgr = np.copy(img)
        h = bgr[1, 1, 0]
        s = bgr[1, 1, 1]
        v = bgr[1, 1, 2]
        if h>100: a=0
        if s>100: b=0
        if v>100: c=0
        if h<100: a=255
        if s<100: b=255
        if v<100: c=255
        cv2.putText(bgr, 'BGR', (5,20), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(bgr, str(h), (5,40), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(bgr, str(s), (5,60), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(bgr, str(v), (5,80), ft, 0.7, (int(a),int(b),int(c)), 1)
        #cv2.imshow('BGR', bgr)
        output[0:200, 0:200] = bgr 
        
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h = rgb[1, 1, 0]
        s = rgb[1, 1, 1]
        v = rgb[1, 1, 2]
        if h>100: a=0
        if s>100: b=0
        if v>100: c=0
        if h<100: a=255
        if s<100: b=255
        if v<100: c=255
        cv2.putText(rgb, 'RGB', (5,20), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(rgb, str(h), (5,40), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(rgb, str(s), (5,60), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(rgb, str(v), (5,80), ft, 0.7, (int(a),int(b),int(c)), 1)
        #cv2.imshow('RGB', rgb)
        output[0:200, 200:400] = rgb 

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h = hsv[1, 1, 0]
        s = hsv[1, 1, 1]
        v = hsv[1, 1, 2]
        if h>100: a=0
        if s>100: b=0
        if v>100: c=0
        if h<100: a=255
        if s<100: b=255
        if v<100: c=255
        cv2.putText(hsv, 'HSV', (5,20), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(hsv, str(h), (5,40), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(hsv, str(s), (5,60), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(hsv, str(v), (5,80), ft, 0.7, (int(a),int(b),int(c)), 1)
        #cv2.imshow('HSV', hsv)
        output[0:200, 400:600] = hsv 
        
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        h = lab[1, 1, 0]
        s = lab[1, 1, 1]
        v = lab[1, 1, 2]
        if h>100: a=0
        if s>100: b=0
        if v>100: c=0
        if h<100: a=255
        if s<100: b=255
        if v<100: c=255
        cv2.putText(lab, 'LAB', (5,20), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(lab, str(h), (5,40), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(lab, str(s), (5,60), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(lab, str(v), (5,80), ft, 0.7, (int(a),int(b),int(c)), 1)
        #cv2.imshow('LAB', lab)
        output[200:400, 0:200] = lab 
        
        yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        h = yuv[1, 1, 0]
        s = yuv[1, 1, 1]
        v = yuv[1, 1, 2]
        if h>100: a=0
        if s>100: b=0
        if v>100: c=0
        if h<100: a=255
        if s<100: b=255
        if v<100: c=255
        cv2.putText(yuv, 'YUV', (5,20), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(yuv, str(h), (5,40), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(yuv, str(s), (5,60), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(yuv, str(v), (5,80), ft, 0.7, (int(a),int(b),int(c)), 1)
        #cv2.imshow('YUV', yuv)
        output[200:400, 200:400] = yuv 
        
        hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
        h = hls[1, 1, 0]
        s = hls[1, 1, 1]
        v = hls[1, 1, 2]
        if h>100: a=0
        if s>100: b=0
        if v>100: c=0
        if h<100: a=255
        if s<100: b=255
        if v<100: c=255
        cv2.putText(hls, 'HLS', (5,20), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(hls, str(h), (5,40), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(hls, str(s), (5,60), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(hls, str(v), (5,80), ft, 0.7, (int(a),int(b),int(c)), 1)
        #cv2.imshow('HLS', hls)
        output[200:400, 400:600] = hls 
        
        YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        h = YCrCb[1, 1, 0]
        s = YCrCb[1, 1, 1]
        v = YCrCb[1, 1, 2]
        if h>100: a=0
        if s>100: b=0
        if v>100: c=0
        if h<100: a=255
        if s<100: b=255
        if v<100: c=255
        cv2.putText(YCrCb, 'YCrCb', (5,20), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(YCrCb, str(h), (5,40), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(YCrCb, str(s), (5,60), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(YCrCb, str(v), (5,80), ft, 0.7, (int(a),int(b),int(c)), 1)
        #cv2.imshow('YCrCb', YCrCb)
        output[400:600, 0:200] = YCrCb 
        
        luv = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
        h = luv[1, 1, 0]
        s = luv[1, 1, 1]
        v = luv[1, 1, 2]
        if h>100: a=0
        if s>100: b=0
        if v>100: c=0
        if h<100: a=255
        if s<100: b=255
        if v<100: c=255
        cv2.putText(luv, 'LUV', (5,20), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(luv, str(h), (5,40), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(luv, str(s), (5,60), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(luv, str(v), (5,80), ft, 0.7, (int(a),int(b),int(c)), 1)
        #cv2.imshow('LUV', luv)
        output[400:600, 200:400] = luv 
        
        xyz = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
        h = xyz[1, 1, 0]
        s = xyz[1, 1, 1]
        v = xyz[1, 1, 2]
        if h>100: a=0
        if s>100: b=0
        if v>100: c=0
        if h<100: a=255
        if s<100: b=255
        if v<100: c=255
        cv2.putText(xyz, 'XYZ', (5,20), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(xyz, str(h), (5,40), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(xyz, str(s), (5,60), ft, 0.7, (int(a),int(b),int(c)), 1)
        cv2.putText(xyz, str(v), (5,80), ft, 0.7, (int(a),int(b),int(c)), 1)
        #cv2.imshow('XYZ', xyz)
        output[400:600, 400:600] = xyz 
        cv2.imshow('ESC for exit, p for plot', output)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:         # wait for ESC key to exit
            break
        elif k == ord('p'):
            titles = ['BGR', 'RGB', 'HSV', 'LAB', 'YUV', 'HLS','YCrCb','LUV','XYZ']
            images = [bgr, rgb, hsv, lab, yuv, hls, YCrCb, luv, xyz]
            for i in range(9):
                plt.subplot(3, 3, i+1) 
                plt.imshow(images[i])
                plt.title(titles[i])
                plt.xticks([]), plt.yticks([])
            plt.show()

    cv2.destroyAllWindows()

#Run Main
if __name__ == "__main__" :
    main()