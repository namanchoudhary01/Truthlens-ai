import cv2
import numpy as np

def predict_image(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return "Error", 0

    img = cv2.resize(img, (128, 128))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Feature 1: variance (texture)
    variance = np.var(gray)

    # Feature 2: edge density
    edges = cv2.Canny(gray, 100, 200)
    edge_density = np.mean(edges)

    # Normalize values
    variance_norm = min(variance / 1000, 1)
    edge_norm = min(edge_density / 100, 1)

    # Combine score
    score = (variance_norm + edge_norm) / 2

    confidence = round(score * 100, 2)

    # Decision threshold
    if score > 0.6:
        return "Fake", confidence
    else:
        return "Real", confidence