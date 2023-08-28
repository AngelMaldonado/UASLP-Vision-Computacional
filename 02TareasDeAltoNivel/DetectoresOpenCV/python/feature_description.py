# Source: https://docs.opencv.org/4.x/d5/dde/tutorial_feature_description.html
# 30/10/2022
import numpy as np
import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='Code for Feature Description tutorial.')
parser.add_argument('--input1', help='Path to input image 1.', default='img/angel_1.jpg')
parser.add_argument('--input2', help='Path to input image 2.', default='img/angel_2.jpg')
args = parser.parse_args()

img1 = cv.imread(cv.samples.findFile(args.input1), cv.IMREAD_GRAYSCALE)
img2 = cv.imread(cv.samples.findFile(args.input2), cv.IMREAD_GRAYSCALE)
if img1 is None or img2 is None:
    print('Could not open or find the images!')
    exit(0)

# -- Step 1: Detect the keypoints using SIFT
detector = cv.SIFT_create()
keypoints1, descriptors1 = detector.detectAndCompute(img1, None)
keypoints2, descriptors2 = detector.detectAndCompute(img2, None)

# -- Step 2: Matching descriptor vectors with a brute force matcher
matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_BRUTEFORCE)
matches = matcher.match(descriptors1, descriptors2)

# -- Draw matches
img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
cv.drawMatches(img1, keypoints1, img2, keypoints2, matches, img_matches)

# -- Show detected matches
cv.imshow('Matches', img_matches)

cv.waitKey(0)