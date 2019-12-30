import time
import sys
import cv2
import imutils
def getBrightness(img):
    hue = cv2.CreateImage


def main(debug=False,fromCamera=True):
    print("inmanin")
    im = None
    if fromCamera:
        print("inif")
        capture = cv2.VideoCapture(2)
        while True:
            ret, frame = capture.read()
            cv2.imshow('Original Capture',frame)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('GrayCapture',gray)

            bilateral_filtered_image = cv2.bilateralFilter(frame,5,175,175)
            cv2.imshow("Bilateral", bilateral_filtered_image)

            edge_detected_image = cv2.Canny(bilateral_filtered_image,75,200)
            cv2.imshow("Edge Detection",edge_detected_image)\
            
            contours = cv2.findContours(edge_detected_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            contour_list = []
            for contour in contours:
                print("*********CONTOURS")
                print(len(contours))
                approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
                area = cv2.contourArea(contour)
                if ((len(approx) > 8) & (area > 30) ):
                    contour_list.append(contour)
            cv2.drawContours(frame,contour_list, -1, (255, 0, 0), 2)
            cv2.imshow('Detected Objs', frame)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        capture.release()
        cv2.destroyAllWindows()

        

        print(str(capture))
if __name__ ==  "__main__":
    print("sanity here")
    main(debug=False,fromCamera=True)
