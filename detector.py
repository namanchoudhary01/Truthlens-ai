import cv2
import numpy as np

def detect_deepfake(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        return "Error", 0

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    score = np.mean(edges)

    confidence = round((score / 255) * 100, 2)

    if score > 50:
        return "Fake", confidence
    else:
        return "Real", confidence