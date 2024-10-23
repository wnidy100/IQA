import cv2
import copy
import numpy as np
from skimage.metrics import structural_similarity as ssim


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
ssim_none = ssim(origin_img, origin_img, channel_axis=2, data_range=origin_img.max()-origin_img.min())

blurred_img = cv2.GaussianBlur(origin_img, (0, 0), 1)
ssim_blurred = ssim(origin_img, blurred_img, channel_axis=2, data_range=origin_img.max()-origin_img.min())

noisy_img = get_noisy_img(origin_img, 0.999)
ssim_noisy = ssim(origin_img, noisy_img, channel_axis=2, data_range=origin_img.max()-origin_img.min())

# cv2.imshow("blurred", blurred_img)
# cv2.imshow("noisy", noisy_img)
# cv2.waitKey(0)

print(ssim_none, ssim_blurred, ssim_noisy)