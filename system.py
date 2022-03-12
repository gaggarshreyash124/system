import cv2

def takesnapshot():
    videocaptureobject=cv2.VideoCapture(0)
    result = True
    while(result):
        ret,Frame = videocaptureobject.read()
        cv2.imwrite("image.png",Frame)
        result= False
    videocaptureobject.release()
    cv2.destroyAllWindows()

takesnapshot()