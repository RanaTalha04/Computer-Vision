import cv2

img_color = cv2.imread("data/Presentation.jpg", cv2.IMREAD_COLOR)
img_gray= cv2.imread("data/Presentation.jpg", cv2.IMREAD_GRAYSCALE)
img_unchanged= cv2.imread("data/Presentation.jpg", cv2.IMREAD_UNCHANGED)


cv2.imshow("Colored Image: ", img_color)
cv2.imshow("Gray Image: ", img_gray)
cv2.imshow("Unchanged Image: ", img_unchanged)


img_color_write = cv2.imwrite("data/ppt_img.jpg", cv2.IMREAD_COLOR)
img_gray_write = cv2.imwrite("data/ppt_img_gray.jpg", cv2.IMREAD_GRAYSCALE)
img_unchanged_write = cv2.imwrite("data/ppt_img_unchanged.jpg", cv2.IMREAD_UNCHANGED)

cv2.waitKey(0)

cv2.destroyAllWindows()