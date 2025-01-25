import cv2
from util12 import get_limits
from  PIL import Image



# Define the BGR color for yellow
yellow = [0, 255, 255]  # Yellow in BGR ColorSpace

# Open the camera (index 0, adjust if necessary)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

try:
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the image from BGR to HSV color space
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get the lower and upper HSV limits for the color yellow
        lowerLimit, upperLimit = get_limits(color=yellow)

        # Create a mask that identifies areas of the frame within the color range
        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        mask_ = Image.fromarray(mask)

        bbox =mask_.getbbox()

        print(bbox)

        if bbox is not None:
            x1,y1,x2,y2 = bbox 

            cv2.rectangle(frame , (x1,y1),(x2,y2) , (0,255,0), 5 )


        # Display the mask
        cv2.imshow('frame', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break
finally:
    # Release the camera and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

