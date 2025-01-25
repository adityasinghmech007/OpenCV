import numpy as np
import cv2

def get_limits(color):
    # Ensure the input color is a list with three integer values
    if not isinstance(color, list) or len(color) != 3:
        raise ValueError("Color must be a list of three integers representing BGR values.")
    
    # Convert the list to a NumPy array and reshape it to (1, 1, 3)
    c = np.array(color, dtype=np.uint8).reshape(1, 1, 3)
    
    # Convert the BGR color to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    # Define the lower and upper HSV limits
    lowerLimit = np.array([hsvC[0][0][0] - 10, 100, 100], dtype=np.uint8)
    upperLimit = np.array([hsvC[0][0][0] + 10, 255, 255], dtype=np.uint8)
    
    return lowerLimit, upperLimit
