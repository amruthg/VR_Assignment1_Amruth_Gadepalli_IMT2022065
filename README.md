# VR Assignment: Coin Detection & Panorama Stitching

## Author

**Amruth Gadepalli**\
**IMT2022065**


## **1. Overview**

This repository contains two Python scripts:

- Part-A: Detects and counts coins in an image.
- Part-B: Matches keypoints between two images and stitches them into a panorama.

Both scripts use OpenCV for image processing and visualization.

---

## **2. How to Run the Code**

Ensure you have **Python 3.x** installed. Then, install OpenCV using:

```sh
pip install opencv-python numpy matplotlib
```

Run the scripts in a terminal:

```sh
python counting_coins.py
python panorama.py
```

The outputs will be displayed sequentially.

---

## **3. Methods Used**

### **Counting Coins (**``**)**

- The image is **loaded and resized** to ensure consistent processing.
- **Gaussian Blur** is applied to remove noise.
- The image is converted to **grayscale** and **thresholded** for better segmentation.
- **Contours** are detected and sorted based on area.
- The largest contour (background) is ignored, and the remaining contours represent coins.
- The final coin count is displayed, and contours are drawn on the image.

### **Panorama Stitching (**``**)**

- Images are **converted to grayscale** for feature extraction.
- **SIFT (Scale-Invariant Feature Transform)** is used to detect keypoints and compute descriptors.
- **Brute-Force Matcher (BFMatcher)** is used to match keypoints between images.
- The **best 50 matches** are drawn to visualize alignment.
- **OpenCV's Stitcher API** attempts to merge the images into a seamless panorama.

---

## **4. Results and Observations**

### **Coin Detection**

- **Detected Coin Count**: **5**
- The algorithm successfully identifies and separates coins from the background.
- Using a high Gaussian blur helps remove noise, ensuring more accurate contour detection.
- Small artifacts in the image do not interfere with the coin count due to area-based filtering.

### **Panorama Stitching**

- **Feature matching using SIFT** successfully aligns corresponding keypoints between images.
- If images have significant overlap, OpenCV's **Stitcher API** produces a seamless panorama.
- The stitching process may fail if:
  - There is insufficient overlap between images.
  - The images lack distinct keypoints.

---

## **5. Dependencies**

Ensure you have the following Python libraries installed:

```sh
pip install opencv-python numpy matplotlib
```

---

## **6. Visual Outputs**

The outputs of the scripts include:

- **Coin Detection Output**: Image with detected coins outlined and the total count displayed.
- **Feature Matching Output**: Image showing keypoint matches between input images.
- **Final Panorama Output**: Stitched image (if successful).

These visualizations appear sequentially when the scripts are executed.

---

## **7. Notes**

- The images (`coins3.jpeg`, `left.jpeg`, `right.jpeg`) should be placed in the same directory as the scripts.
- The scripts do not require any additional user input after execution.
- If the panorama stitching fails, try using images with **more overlapping regions**.

---

## **8. Contact**

For any issues or improvements, feel free to contribute or raise an issue.



