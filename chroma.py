import cv2 as cv
import numpy as np

def chroma(video_path, bg):
    capture = cv.VideoCapture(video_path)
    bg = cv.cvtColor(bg, cv.COLOR_BGR2BGRA)
    h, w, c = bg.shape
    out = cv.VideoWriter("saves/vid.mp4",-1, 20.0, (w, h))
    i=0
    while True:
        isTrue, im = capture.read()
        if isTrue==True:
            bg_copy=np.copy(bg)
            bgr_img = np.copy(cv.resize(im, (w, h)))
            im = cv.resize(cv.cvtColor(im, cv.COLOR_BGR2BGRA), (w, h))
            hsv_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)
            green = np.where((hsv_img[:,:,0]<=80) & (hsv_img[:,:,0]>=40) & (hsv_img[:,:,1]>90) & (hsv_img[:,:,2]>90))
            im[green]=(0,0,0,0)
            alpha = im[:, :, 3]/255.0
            for c in range(0,3):
                bg_copy[0:h, 0:w, c]=(im[:,:,c]*(alpha)+((1.0-alpha)*bg[0:h, 0:w, c]))
            out.write(bg_copy)
            print(f"{i} frames completed")
            i+=1
        else:
            print("Completed")
            break

    capture.release()
    out.release()
    # cv.destroyAllWindows()

if __name__ == '__main__':
    chroma("vids/rr.mp4", cv.imread("imgs/mars.jpg"))