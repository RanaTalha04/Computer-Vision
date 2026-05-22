import cv2
import matplotlib.pyplot as plt
import numpy as np

digit = np.uint8(250)
print(f"Digit: {digit + 10}")
print(f"Digit: {digit - 255}")

# Image READ, SHOW, WRITE and COLORS
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

# Image shape

image = cv2.imread('data/Presentation.jpg', cv2.IMREAD_COLOR)

h, w, c = image.shape

print(f"Height: {h}, Width: {w}, Channels: {c}")
print(f"Total Pixel: {h*w:,}")


# Image Resize
# By width and height

cv2.imshow('Original Image', image)

down_width = 500
down_height = 500

down_points = (down_width, down_height)

resized_image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)

cv2.imshow('Resized Image', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize in Half

half = cv2.resize(image, None ,fx=0.5, fy=0.5)
cv2.imshow("Resize in Half", half)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Image Cropping, Slicing, Indexing

# Single Pixel

pixel = image[0, 0]
print(pixel)

# One Channel 

blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, :, 2]

print(f"Blue: {blue}")
print(f"Green: {green}")
print(f"Red: {red}")

# Cropping
print(resized_image.shape)
cropped_image = image[100:400, 100: 500]

cv2.imshow("Cropped Image", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Use this in jupyter notebbok or Colab or Kaggle or any other notebook

fig, axes = plt.subplots(2, 4, figsize=(14, 6))
axes[0,0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)); axes[0,0].set_title('Original')
axes[0,1].imshow(blue, cmap='Blues');   axes[0,1].set_title('Blue channel')
axes[0,2].imshow(green, cmap='Greens');  axes[0,2].set_title('Green channel')
axes[0,3].imshow(red, cmap='Reds');    axes[0,3].set_title('Red channel')
# axes[1,0].imshow(gray, cmap='gray'); axes[1,0].set_title('Grayscale')
axes[1,1].imshow(cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)); axes[1,1].set_title('Flipped')
axes[1,2].imshow(cv2.cvtColor(image[h//4:3*h//4, w//4:3*w//4], cv2.COLOR_BGR2RGB)); axes[1,2].set_title('Center crop')
axes[1,3].imshow(cv2.cvtColor(255 - image, cv2.COLOR_BGR2RGB)); axes[1,3].set_title('Inverted')
for ax in axes.flat: ax.axis('off')
plt.tight_layout()
plt.show()