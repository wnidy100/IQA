import cv2
import math
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


def get_psnr_score(img1, img2):
    mse = np.square(np.subtract(img1, img2)).mean() # MSE

    if mse == 0:
        return 100

    PIXEL_MAX = 255.0
    psnr_score = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

    return psnr_score


origin_img = cv2.imread("highq.jpg")
origin_psnr_score = get_psnr_score(origin_img, origin_img)

noisy_img = get_noisy_img(origin_img)
noisy_psnr_score = get_psnr_score(origin_img, noisy_img)

blurred_img = cv2.GaussianBlur(origin_img, (0, 0), 5)
blurred_psnr_score = get_psnr_score(origin_img, blurred_img)

print("MSE with original:", origin_psnr_score)
print("MSE with blurred:", noisy_psnr_score)
print("MSE with noisy:", blurred_psnr_score)