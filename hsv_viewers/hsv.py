import cv2
import numpy as np

def imshow(img:np.ndarray, name:str="img"):
    cv2.imshow(name, img)
    key = cv2.waitKey(0)
    print(key)
    cv2.destroyAllWindows()


def cvt_bgr2hsv(bgr_img:np.ndarray) -> np.ndarray:
    hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
    return hsv_img

def make_range_mask(
        hsv_mat_ch3:np.ndarray, 
        thresh1:int, 
        thresh2:int, 
        ch:int) -> np.ndarray:
    assert 0 <= ch <= 2
    h_mat_ch1 = hsv_mat_ch3[:, :, ch:ch+1]
    mat_shape = h_mat_ch1.shape
    if thresh1 == thresh2:
        mask_ch1 = np.zeros(mat_shape, dtype="uint8")
    elif thresh1 < thresh2:
        mask_ch1 = np.where(
            np.logical_and(
                thresh1 <= h_mat_ch1, 
                h_mat_ch1 <= thresh2), 
            1, 0).astype("uint8")
    else:
        mask_ch1 = np.where(
            np.logical_or(
                h_mat_ch1 >= thresh1, 
                h_mat_ch1 <= thresh2),
            1, 0).astype("uint8")

    mask_ch3 = np.repeat(mask_ch1, repeats=3, axis=-1)

    return mask_ch3


def make_hew_mask(
        hsv_mat_ch3:np.ndarray, 
        thresh1:int, 
        thresh2:int) -> np.ndarray:
    return make_range_mask(hsv_mat_ch3, thresh1, thresh2, 0)


def make_saturation_mask(
        hsv_mat_ch3:np.ndarray,
        thresh1:int,
        thresh2:int) -> np.ndarray:
    return make_range_mask(hsv_mat_ch3, thresh1, thresh2, 1)


def make_brightness_mask(
        hsv_mat_ch3:np.ndarray, 
        thresh1:int, 
        thresh2:int) -> np.ndarray:
    return make_range_mask(hsv_mat_ch3, thresh1, thresh2, 2)


if __name__ == "__main__":


    src_img_path = "../data/cat_0001.jpg"
    src_img = cv2.imread(src_img_path)

    hsv_img = cvt_bgr2hsv(src_img)
    v_mask = make_brightness_mask(hsv_img, 30, 60)

    assert src_img.shape == v_mask.shape
    out_img = src_img * v_mask

    imshow(out_img)