#!/usr/bin/env python3

from tools import *
from segmentation import *

color_map = np.array([[0,0,0],[0,0,0], [0,0,0], [255,255,255]])

def perspective(image):
    height,width,_=image.shape
    up = 280
    upstrech = 100
    stretch = 220

    tl = [0, up]
    tr = [width, up]
    br = [0, height]
    bl = [width, height]

    corner_points_array = np.float32([tl, tr, br, bl])

    # Create an array with the parameters (the dimensions) required to build the matrix
    imgtl = [0, 1]
    imgtr = [width, 0]
    imgbr = [0+stretch, height-upstrech]
    imgbl = [width-stretch, height-upstrech]


    img_params = np.float32([imgtl, imgtr, imgbr, imgbl])

    # Compute and return the transformation matrix
    matrix = cv2.getPerspectiveTransform(corner_points_array, img_params)
    img_transformed = cv2.warpPerspective(image, matrix, (width, height-upstrech))
    return img_transformed



def callback(image):
    mask , contour_points, road = get_segmentation_image(image,color_map)
    cv2.imshow("asd",perspective(image))
    cv2.waitKey(1)
    mask = cv2.resize(mask,(640,480))

    cv2.imshow("qsd",perspective(mask))


imagesubscribe("/axis_videocap/image_raw",callback)

rospy.init_node('base', anonymous=True)
try:
  rospy.spin()
except KeyboardInterrupt:
  print("Shutting down")

