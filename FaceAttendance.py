# Importing Libraries
import cv2
import os


def path_exists(path):
    direct = os.path.dirname(path)
    if not os.path.exists(direct):
        os.makedirs(direct)


face_id = input("Enter you ID Number:")

# Capturing Video

video_cam = cv2.VideoCapture(0)

# Object Detection
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Initializing sample face image

count = 0

path_exists("Dataset")


# Looping

while True:
    # Capture video frame
    _, image_frame = video_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes

    faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Loops for each face
    for (x,y,w,h) in faces:

        # Cropping image frame into a rectangle
        cv2.rectangle(image_frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

        # Increment sample face image
        count+=1

        # Saving dataset in folder
        cv2.imwrite("Dataset" + str(face_id) +"." + str(count)+ ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame with rectangle
        cv2.imshow("frame", image_frame)

    # To stop taing video press s
    if cv2.waitKey(100) & 0xFF == ord("s"):
        break

    # If image number reaches 100, stop video
    elif count>=30:
        print("Successfully Captured")
        break

# Stop video
video_cam.release()

# Close all windows
cv2.destroyAllWindows()
