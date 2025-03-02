import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load images
img1 = cv2.imread("left.jpeg")  # Change path if needed
img2 = cv2.imread("right.jpeg")

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

# Create BFMatcher (Brute-Force Matcher)
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# Match descriptors
matches = bf.match(descriptors1, descriptors2)

# Sort matches by distance (best matches first)
matches = sorted(matches, key=lambda x: x.distance)

# Draw the top 50 matches
img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the matched keypoints
plt.figure(figsize=(15, 8))
plt.imshow(img_matches)
plt.title("Keypoint Matching Between Images")
plt.show()

# -------- Panorama Stitching --------
stitcher = cv2.Stitcher.create()
status, pano = stitcher.stitch([img1, img2])

if status == cv2.STITCHER_OK:
    plt.figure(figsize=(15, 7))
    plt.imshow(cv2.cvtColor(pano, cv2.COLOR_BGR2RGB))
    plt.title("Final Panorama")
    plt.axis("off")
    plt.show()
else:
    print("Error during stitching")
