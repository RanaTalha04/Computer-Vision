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

## Image Resize

image = cv2.imread('data/Presentation.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Original Image', image)

down_width = 500
down_height = 500

down_points = (down_width, down_height)

resized_image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Resized Image', resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()


## Image Cropping

print(resized_image.shape)
cropped_image = image[100:400, 100: 500]

cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
