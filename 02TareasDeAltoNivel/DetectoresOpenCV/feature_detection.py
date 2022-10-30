import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(
    description='Code for Feature Detection tutorial.')
parser.add_argument('--input', help='Path to input image.',
                    default='img/corners.jpg')
args = parser.parse_args()

src = cv.imread(cv.samples.findFile(args.input), cv.IMREAD_GRAYSCALE)
if src is None:
    print('Could not open or find the image: ', args.input)
    exit(0)

# -- Step 1: Detect the keypoints using SIFT
detector = cv.SIFT_create()
keypoints = detector.detect(src)


# -- Draw keypoints
img_keypoints = np.empty((src.shape[0], src.shape[1], 3), dtype=np.uint8)
cv.drawKeypoints(src, keypoints, img_keypoints)

# -- Show detected (drawn) keypoints
cv.imshow('SIFT Keypoints', img_keypoints)

cv.waitKey(0)
