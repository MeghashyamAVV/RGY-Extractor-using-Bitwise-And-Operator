# RGY-Extractor-using-Bitwise-And-Operator



This code uses OpenCV library to extract the red, green, and yellow components of an image using color masks and bitwise AND operator. The code reads an image file and sets up color ranges for the red, green, and yellow colors. Then, using the cv2.inRange function, it creates binary masks for each of these colors. The bitwise AND operator is then applied to the original image and the respective color masks, resulting in three separate images containing only the red, green, and yellow components.

The resulting images are then displayed using cv2.imshow function. By using color masks and bitwise AND operator, this code effectively segments the image into its color components, making it easier to identify and analyze specific parts of the image. This technique can be useful in a variety of applications, such as object detection, image segmentation, and computer vision.
