import cv2

## Reading images

# img = cv2.imread("resources/lena.png")
# print(img.shape)
# cv2.imshow("Output", img)
# cv2.waitKey(0)

## reading videos

# cap = cv2.VideoCapture("resources/elon.mp4")

# while True:
#     success, img = cap.read()
#     print(img.shape)
#     cv2.imshow("Output", img)

    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break 


## reading webcam



# to open  WebCam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

while True:
    success, img = cap.read()
    
    if not success or img is None:
        print("Failed to grab frame")
        continue 
    
    print(img.shape)
    cv2.imshow("WebCam", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break