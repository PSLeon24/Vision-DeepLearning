import cv2

img = cv2.imread('star.jpeg', cv2.IMREAD_COLOR)
cv2.imshow('Image processing', img)

cv2.waitKey(0)
cv2.destroyAllWindows()