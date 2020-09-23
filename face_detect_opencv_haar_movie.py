import cv2

face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
#mouth_cascade = cv2.CascadeClassifier('./data/haarcascade_mcs_mouth.xml')

scaler=0.4
cap =cv2.VideoCapture('./img/5.mp4')

while True:
    ret, img = cap.read()    
    if not ret:
        break
    img_resize = cv2.resize(img, (int(img.shape[1]*scaler), int(img.shape[0]*scaler)))
    img_gray=cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray,1.1,3)
    for x, y, w, h in faces:
        cv2.rectangle(img_resize, (x, y), (x + w, y + h), (255, 0, 0), 2)
        '''
        face = src[y: y + h, x: x + w]
        face_gray = src_gray[y: y + h, x: x + w]
        
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            '''
        
    cv2.imshow('img', img_resize)
    key= cv2.waitKey(30)   
    if key & 0xFF == 27:#esc
        break

cap.release()
cv2.destroyAllWindows()
