from pathlib import Path
from shutil import ExecError
import tkinter as tk

import numpy as np
import cv2

from gui_app import App
import hsv

class Ctrl:
    def __init__(self, app:App):
        self.app = app

        self.bgr_img = None
        self.hsv_img = None
        self.rgb_img = None
        self.h_mask = None
        self.s_mask = None
        self.v_mask = None

        self.app.frame1.scale.set_callback(self.mask_hsv)

    
    def load_img(self, path:str):
        _path = Path(path)
        assert _path.exists()
        bgr_img = cv2.imread(path)

        bgr_img_hsize, bgr_img_wsize = bgr_img.shape[:2]
        ratio = 640 / bgr_img_wsize
        img_wsize = 640
        img_hsize = int(bgr_img_hsize * ratio)
        bgr_img = cv2.resize(bgr_img, (img_wsize, img_hsize))

        self.bgr_img = bgr_img
        self.hsv_img = hsv.cvt_bgr2hsv(self.bgr_img)
        self.rgb_img = cv2.cvtColor(self.bgr_img, cv2.COLOR_BGR2RGB)
        self.h_mask = np.ones(self.bgr_img.shape, dtype="uint8")
        self.s_mask = np.ones(self.bgr_img.shape, dtype="uint8")
        self.v_mask = np.ones(self.bgr_img.shape, dtype="uint8")

        self.app.frame1.canvas.set_image(self.rgb_img)


    def mask_hsv(
            self, 
            hsv_text:str, 
            value1:int, 
            value2:int):
        if hsv_text == "h":
            self.h_mask = hsv.make_hew_mask(self.hsv_img, value1, value2)
        elif hsv_text == "s":
            self.s_mask = hsv.make_saturation_mask(self.hsv_img, value1, value2)
        elif hsv_text == "v":
            self.v_mask = hsv.make_brightness_mask(self.hsv_img, value1, value2)
        else:
            raise Exception

        out_img = self.rgb_img * self.h_mask * self.s_mask * self.v_mask
        self.app.frame1.canvas.set_image(out_img)


    def begin(self):
        self.app.mainloop()