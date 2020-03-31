import cv2

video_src = 'resource\\video480.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier('cascades\\cars.xml')

count = 0

while True:

    ret, img = cap.read()

    if (type(img) == type(None)):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if count == 0:
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

    cv2.imshow('video-car', img)

    if cv2.waitKey(33) == 27:
        break

    count = count + 1
    if count > 4:
        count = 0

cv2.destroyAllWindows()