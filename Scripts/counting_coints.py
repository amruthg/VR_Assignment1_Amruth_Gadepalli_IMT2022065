import cv2
import numpy as np

# Load the image
img = cv2.imread("coins3.jpeg")

# Ensure the image was loaded correctly
if img is None:
    print("Error: Could not read image. Check the file path.")
    exit()

# Resize the image to a fixed size for consistency in processing
# 800x800 is chosen to ensure uniformity in contour detection across different images
img = cv2.resize(img, (800, 800))

# Create a copy of the original image to draw contours later without modifying the original
img_copy = img.copy()

# Apply Gaussian blur to reduce noise and smoothen the image
# A larger kernel size (7x7) is used to eliminate minor details, so only significant edges remain
# The high sigma value (100) ensures the blurring is strong, reducing unnecessary contours
img = cv2.GaussianBlur(img, (7,7), 100)

# Convert the image to grayscale since contour detection works better in single-channel images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image (black & white)
# Pixels with intensity > 120 are set to white (255), others to black (0)
# This helps in distinguishing the coins from the background
ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

# Find contours in the thresholded image
# cv2.RETR_TREE retrieves all contours and creates a hierarchy, useful if there are nested objects
# cv2.CHAIN_APPROX_NONE stores all contour points without compression, which is useful for accurate shape analysis
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Dictionary to store area of each detected contour
area = {}
for i in range(len(contours)):
    cnt = contours[i]
    ar = cv2.contourArea(cnt)  # Calculate area of the contour
    area[i] = ar  # Store area with contour index

# Sort contours by area in descending order
# This helps in filtering out smaller unwanted contours (e.g., noise, holes)
srt = sorted(area.items(), key=lambda x: x[1], reverse=True)

# Convert sorted results into a NumPy array for easy indexing
results = np.array(srt).astype("int")

# Print sorted contour areas for debugging and analysis
# print(results)

# Count the number of detected contours excluding the largest one (usually the background)
num = np.argwhere(results[:, 1]).shape[0]

# Draw contours on the original image, ignoring the largest one (which is likely the entire background)
for i in range(1, num):  # Start from 1 to skip the background
    img_copy = cv2.drawContours(img_copy, contours, results[i, 0], (255, 0, 0), 3) 
    # Draw each detected coin with a blue outline (BGR: (255, 0, 0)) and thickness 3

# Print the final count of detected coins (excluding the largest contour)
print("Number of coins is", num - 1)

# Display the final image with contours drawn
cv2.imshow("final", img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()


