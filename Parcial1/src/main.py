# Autor: Angel de Jesús Maldonado Juárez
# Universidad Autónoma de San Luis Potosí
# Examen Parcial 1 | Visión Computacional
# Fecha de entrega: 26/09/22

import cv2 as cv
import numpy as np

# window name
wname = 'Parcial1'

# Sobel filter parameters
dx_sobel = 1
dy_sobel = 0
ksize_sobel = 1

# Dilate initial parameters
shape_dilate = cv.MORPH_RECT
ksize_dilate = 1

# Erode filter parameters
shape_erode = cv.MORPH_RECT
ksize_erode = 1

# Rotation degrees
deg = 0

# Crop coordinates
point_matrix = np.zeros((2, 2), np.int32)
# Click counter
click_counter = 0
# Function to store coordinates with clicks


def mousePoints(event, x, y, flags, params):
    global click_counter
    # Left button mouse click event opencv
    if event == cv.EVENT_LBUTTONDOWN:
        point_matrix[click_counter] = x, y
        click_counter = click_counter + 1


# load the image
img = cv.imread('../img/examen_b.tif')

# check if image was loaded correctly
if img.size != 0:
    # create new window
    cv.namedWindow(wname)

    # Sobel configuration
    while True:
        # apply Sobel filter
        sobel = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=dx_sobel,
                         dy=dy_sobel, ksize=ksize_sobel)
        # show Sobel parameters
        print('\n########## Sobel parameters ##########')
        print("\ndx={0}, dy={1}, ksize={2}".format(
            dx_sobel, dy_sobel, ksize_sobel))
        print("\n(1 to dx, 2 to dy, 3 to -ksize, 4 to +ksize)")
        print("(x to exit, enter to continue process...)")
        # show image filtered
        cv.imshow(wname, sobel)

        # wait for key press
        k = cv.waitKey(0)
        match k:
            # key '1' - toggle dx_sobel
            case 49:
                dx_sobel = 0 if dx_sobel == 1 and dy_sobel == 1 else 1
            # key '2' - toggle dy_sobel
            case 50:
                dy_sobel = 0 if dy_sobel == 1 and dx_sobel == 1 else 1
            # key '3' - decrease ksize_sobel by 2
            case 51:
                ksize_sobel = ksize_sobel - 2 if ksize_sobel > 1 else ksize_sobel
            # key '4' - increase ksize_sobel by 2
            case 52:
                ksize_sobel = ksize_sobel + 2 if ksize_sobel < 31 else ksize_sobel
            # key 'x' - exit program
            case 120:
                exit()
            # key 'enter' - save step on img and continue process
            case 13:
                cv.imwrite('../img/sobel-res.png', sobel)
                img = cv.imread('../img/sobel-res.png')
                break

    # Dilate configuration
    while True:
        # get dilation kernel given shape and ksize
        kernel = cv.getStructuringElement(
            shape_dilate, (ksize_dilate, ksize_dilate))
        # apply Dilation filter
        dilation = cv.dilate(img, kernel)
        # show Dilation parameters
        print('\n########## Dilation parameters ##########')
        print("\nshape={0}, ksize=({1},{2})".format(
            str(shape_dilate), ksize_dilate, ksize_dilate))
        print("\n(1 to cv.MORPH_RECT, 2 to cv.MORPH_CROSS, 3 to MORPH_ELLIPSE, 4 to -ksize, 5 to +ksize)")
        print("(x to exit, enter to continue process...)")
        # show image filtered
        cv.imshow(wname, dilation)

        # wait for key press
        k = cv.waitKey(0)
        match k:
            # key '1' - change to cv.MORPH_RECT
            case 49:
                shape_dilate = cv.MORPH_RECT
            # key '2' - change to cv.MORPH_CROSS
            case 50:
                shape_dilate = cv.MORPH_CROSS
            # key '3' - change to cv.MORPH_ELLIPSE
            case 51:
                shape_dilate = cv.MORPH_ELLIPSE
            # key '4' - decrease ksize_dilate by 2
            case 52:
                ksize_dilate = ksize_dilate - 1 if ksize_dilate > 1 else ksize_dilate
            case 53:
                ksize_dilate = ksize_dilate + 1
            # key 'x' - exit program
            case 120:
                exit()
            # key 'enter' - save step on img and continue process
            case 13:
                cv.imwrite('../img/dilate-res.png', dilation)
                img = cv.imread('../img/dilate-res.png')
                break

    # crop image with 2 clicks
    tmp = img.copy()
    # set click callback
    cv.setMouseCallback(wname, mousePoints)
    print('\nClick 2 points on image...')
    while True:
        # if user clicked twice
        if (click_counter == 2):
            # first point
            starting_x = point_matrix[0][0]
            starting_y = point_matrix[0][1]

            # second point
            ending_x = point_matrix[1][0]
            ending_y = point_matrix[1][1]
            # Draw rectangle for area of interest
            cv.rectangle(tmp, (starting_x, starting_y),
                         (ending_x, ending_y), (0, 255, 0), 3)

            # show cropping coordinates and bounding box
            cv.imshow(wname, tmp)
            print('\n########## Cropping coordinates ({}) ##########'.format(
                click_counter))
            print("\n({},{}) ({},{})".format(
                point_matrix[0][0], point_matrix[0][1], point_matrix[1][0], point_matrix[1][1]))
            print("(x to exit, enter to continue process, or any to change box)")

            # wait for key press
            k = cv.waitKey(0)
            match k:
                # key 'x' - exit program
                case 120:
                    exit()
                # key 'enter' - save step on img and continue process
                case 13:
                    # crop image and continue process
                    crop = img[starting_y:ending_y, starting_x:ending_x]
                    img = crop
                    # show croped image
                    cv.imshow(wname, crop)
                    break
            # restart if any key was pressed
            print('\nClick 2 points on image...')
            click_counter = 0
            tmp = img.copy()
            point_matrix = np.zeros((2, 2), np.int32)

        # show dots on user clicks
        for x in range(0, 2):
            cv.circle(
                tmp, (point_matrix[x][0], point_matrix[x][1]), 3, (0, 255, 0), cv.FILLED)
        # show dotted image
        cv.imshow(wname, tmp)
        # refresh
        cv.waitKey(1)

    # Erode configuration
    while True:
        # get filter kernel
        kernel = cv.getStructuringElement(
            shape_erode, (ksize_erode, ksize_erode))
        # apply Bilateral filter
        erode = cv.erode(img, kernel)

        print('\n########## Erosion parameters ##########')
        print("\nshape={0}, ksize=({1},{2})".format(
            str(shape_erode), ksize_erode, ksize_erode))
        print("\n(1 to cv.MORPH_RECT, 2 to cv.MORPH_CROSS, 3 to MORPH_ELLIPSE, 4 to -ksize, 5 to +ksize)")
        print("(x to exit, enter to continue process...)")
        # show image filtered
        cv.imshow(wname, erode)

        # wait user new configuration
        k = cv.waitKey(0)
        match k:
            case 49:
                shape_erode = cv.MORPH_RECT
            case 50:
                shape_erode = cv.MORPH_CROSS
            case 51:
                shape_erode = cv.MORPH_ELLIPSE
            case 52:
                ksize_erode = ksize_erode - 2 if ksize_erode > 1 else ksize_erode
            case 53:
                ksize_erode = ksize_erode + 2
            # key 'x' - exit program
            case 120:
                exit()
            # key 'enter' - save step on img and continue process
            case 13:
                cv.imwrite('../img/erode-res.png', erode)
                img = cv.imread('../img/erode-res.png')
                break

    # image rotation
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    while True:
        # show rotated image
        print("\ndegrees={}".format(deg))
        print("\n(1 to -degrees, 2 to +degrees")
        print("(x to exit, enter to finish process and save image...)")

        # wait user new configuration
        k = cv.waitKey(0)
        match k:
            case 49:
                deg = deg - 1
                # generate rotation matrix
                M = cv.getRotationMatrix2D((cX, cY), -1, 1.0)
            case 50:
                deg = deg + 1
                M = cv.getRotationMatrix2D((cX, cY), 1, 1.0)
            # key 'x' - exit program
            case 120:
                exit()
            # key 'enter' - save step on img and continue process
            case 13:
                cv.imwrite('../img/res.png', img)
                cv.destroyAllWindows()
                break

        # apply rotation matrix to image
        img = cv.warpAffine(img, M, (w, h))
        cv.imshow(wname, img)

    print('\nSobel parameters: dx={}, dy={}, ksize={}'.format(
        dx_sobel, dy_sobel, ksize_sobel))
    print("Dilate parameters: shape={}, ksize={}".format(
        str(shape_dilate), ksize_dilate))
    print("Crop coordinates: ({},{}) ({},{})".format(
        point_matrix[0][0], point_matrix[0][1], point_matrix[1][0], point_matrix[1][1]))
    print("Erode parameters: shape={}, ksize={}".format(
        str(shape_erode), ksize_erode))
    print("Rotating angle: {}".format(deg))
else:
    print('error loading image...')
