print("Do you want to take your photo: ")
a=int(input("press 1 for yes and 2 for no"))
if a==1:
    
    import numpy as np
    import cv2
    cam=cv2.VideoCapture(0)
    print("any 'q' key to capture photo")
    while True:
        return_value,img=cam.read()
        gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow("cam-test",gray)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            cv2.imwrite('image.jpg',img)
            break
    cam.release()
    cv2.destroyAllWindows()
else:
    print("exit")
