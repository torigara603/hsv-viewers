import tkinter as tk

import numpy as np
from PIL import Image, ImageTk

class MyCanvas(tk.Canvas):
    def __init__(self, master=None, wsize:int=640, hsize:int=480):
        super().__init__(master, width=wsize, height=hsize)
    
    def set_image(self, rgb_img:np.ndarray):
        self.rgb_img = rgb_img
        window_wsize = self.winfo_width()
        window_hsize = self.winfo_height()
        self._tkimg = ImageTk.PhotoImage(Image.fromarray(rgb_img))
        self.create_image(
            (window_wsize // 2, window_hsize // 2), 
            image=self._tkimg)

    def get_image(self) -> np.ndarray:
        return self.rgb_img
