import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\Abdul Qawi\Desktop\WhatsApp Image 2023-11-26 at 13.11.41_10a02fee.jpg"
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform edge detection using Canny
edges = cv2.Canny(gray, 30, 150)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area to find potential faces
min_area = 500
potential_faces = []
for contour in contours:
    if cv2.contourArea(contour) > min_area:
        x, y, w, h = cv2.boundingRect(contour)
        potential_faces.append((x, y, x+w, y+h))

# Draw rectangles around potential faces
for (x1, y1, x2, y2) in potential_faces:
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the result
cv2.imshow('Potential Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
