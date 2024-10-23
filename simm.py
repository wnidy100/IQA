import cv2
import copy
import numpy as np
from skimage.metrics import structural_similarity as ssim


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
origin_ssim_score = ssim(origin_img, origin_img, channel_axis=2, data_range=origin_img.max()-origin_img.min())

blurred_img = cv2.GaussianBlur(origin_img, (0, 0), 5)
blurred_ssim_score = ssim(origin_img, blurred_img, channel_axis=2, data_range=origin_img.max()-origin_img.min())

noisy_img = get_noisy_img(origin_img)
noisy_ssim_score = ssim(origin_img, noisy_img, channel_axis=2, data_range=origin_img.max()-origin_img.min())

# cv2.imshow("blurred", blurred_img)
# cv2.imshow("noisy", noisy_img)
# cv2.waitKey(0)

print("SSIM with original:", origin_ssim_score)
print("SSIM with blurred:", blurred_ssim_score)
print("SSIM with noisy:", noisy_ssim_score)