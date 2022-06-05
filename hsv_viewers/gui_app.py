import tkinter as tk
import cv2
from PIL import Image, ImageTk

from gui_canvas import MyCanvas
from gui_hsv_bar import HSVScaleFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.frame1 = MainFrame(self)
        self.frame1.pack()
        self.set_position()

    
    def set_position(self):
        self.update()
        frame_width = self.winfo_width()
        frame_height = self.winfo_height()
        geometry = f"{frame_width}x{frame_height}"
        geometry += f"+{50}+{50}"
        self.geometry(f"{geometry}")


class MainFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.canvas = MyCanvas(self)
        self.canvas.grid(column=0, row=0)
        self.canvas.update()

        self.scale = HSVScaleFrame(self)
        self.scale.grid(column=1, row=0)


if __name__ == "__main__":
    root = tk.Tk()

    frame1 = MainFrame(master=root)
    frame1.pack()

    root.mainloop()