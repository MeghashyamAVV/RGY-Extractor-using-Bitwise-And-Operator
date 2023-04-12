import cv2
import numpy as np

img = cv2.imread('img2.jfif')

red_lower = np.array([0, 0, 100])
red_upper = np.array([80, 80, 255])
green_lower = np.array([0, 100, 0])
green_upper = np.array([80, 255, 80])
yellow_lower = np.array([0, 200, 200])
yellow_upper = np.array([80, 255, 255])


red_mask = cv2.inRange(img, red_lower, red_upper)
green_mask = cv2.inRange(img, green_lower, green_upper)
yellow_mask = cv2.inRange(img, yellow_lower, yellow_upper)

red_vegetable = cv2.bitwise_and(img, img, mask=red_mask)
green_vegetable = cv2.bitwise_and(img, img, mask=green_mask)
yellow_vegetable = cv2.bitwise_and(img, img, mask=yellow_mask)

cv2.imshow('Red Vegetable', red_vegetable)
cv2.imshow('Green Vegetable', green_vegetable)
cv2.imshow('Yellow Vegetable', yellow_vegetable)

cv2.waitKey(0)
cv2.destroyAllWindows()