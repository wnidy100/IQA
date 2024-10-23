import cv2
import copy
import numpy as np


# 0 <= th < 1
# The smaller the 'th', the noiser the image
def get_noisy_img(origin_img, th=0.7):
    img = copy.copy(origin_img)
    h, w, c = img.shape

    for k in range(c):
        rand_mat1 = np.random.rand(h, w)
        rand_mat2 = np.random.rand(h, w)

        for i, low in enumerate(rand_mat1):
            for j, val in enumerate(low):
                if val >= th:
                    img[i][j][k] *= rand_mat2[i][j]
    return img


origin_img = cv2.imread("highq.jpg")
origin_mse_score = np.square(np.subtract(origin_img, origin_img)).mean()

noisy_img = get_noisy_img(origin_img)
noisy_mse_score = np.square(np.subtract(origin_img, noisy_img)).mean()

blurred_img = cv2.GaussianBlur(origin_img, (0, 0), 5)
blurred_mse_score = np.square(np.subtract(origin_img, blurred_img)).mean()

print("MSE with original:", origin_mse_score)
print("MSE with blurred:", blurred_mse_score)
print("MSE with noisy:", noisy_mse_score)