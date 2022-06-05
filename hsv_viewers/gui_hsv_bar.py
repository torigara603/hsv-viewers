from typing import Tuple, Callable

import tkinter as tk

def basic():
    app = tk.Tk()
    scale = tk.Scale(master=app)
    scale.configure(orient="horizontal")
    scale.configure(from_=0, to=100)
    scale.pack()

    app.mainloop()


class MyScale(tk.Scale):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(orient="horizontal")
        self.configure(length=100)
        self.configure(from_=0, to=100)
        self.configure(command=self.move)
        self.intval = tk.IntVar()
        self.configure(variable=self.intval)
        self.configure(tickinterval=100)


    def move(self, str_value:str):
        var1 = int(str_value)
        var2 = self.intval.get()
        print(var1, var2)


class RangeScaleFrame(tk.LabelFrame):
    def __init__(
            self, 
            master=None, 
            text:str="", 
            from_to1:Tuple[int, int]=(0, 100), 
            from_to2:Tuple[int, int]=(0, 100)):
        super().__init__(master)
        self.configure(text=text)

        self.scale1 = MyScale(self)
        self.scale1.configure(from_=from_to1[0])
        self.scale1.configure(to=from_to1[1])
        self.scale1.configure(tickinterval=from_to1[1])
        self.scale1.intval.set(from_to1[0])
        self.scale1.pack()

        self.scale2 = MyScale(self)
        self.scale2.configure(from_=from_to2[0])
        self.scale2.configure(to=from_to2[1])
        self.scale2.configure(tickinterval=from_to2[1])
        self.scale2.intval.set(from_to2[1])
        self.scale2.pack()

        self.scale1.configure(command=self.move)
        self.scale2.configure(command=self.move)

        self.callback = None


    def set_callback(self, func:Callable):
        self.callback = func


    def move(self, *args):
        value1 = self.scale1.intval.get()
        value2 = self.scale2.intval.get()
        if self.callback is not None:
            self.callback(value1, value2)
        else:
            print("None Callback")
            print(f"value1:{value1}, value2:{value2}")


class HSVScaleFrame(tk.LabelFrame):
    def __init__(self, master=None, text="HSV_option"):
        super().__init__(master)
        self.configure(text=text)

        h_from_to = (0, 179)
        s_from_to = (0, 255)
        v_from_to = (0, 255)

        self.h_scale = RangeScaleFrame(
            self, 
            text="hew", 
            from_to1=h_from_to, 
            from_to2=h_from_to)
        self.h_scale.set_callback(self.h_scale_move)
        self.h_scale.pack()
        
        self.s_scale = RangeScaleFrame(
            self, 
            text="satiration", 
            from_to1=s_from_to, 
            from_to2=s_from_to)
        self.s_scale.set_callback(self.s_scale_move)
        self.s_scale.pack()

        self.v_scale = RangeScaleFrame(
            self, 
            text="brightness", 
            from_to1=v_from_to, 
            from_to2=v_from_to)
        self.v_scale.set_callback(self.v_scale_move)
        self.v_scale.pack()

        self.callback = None


    def set_callback(self, func:Callable):
        self.callback = func


    def h_scale_move(self, value1:int, value2:int):
        if self.callback is not None:
            self.callback("h", value1, value2)
        else:
            print("None Callback")
            print(f"{self.__class__}, value1:{value1}, value2:{value2}")


    def s_scale_move(self, value1:int, value2:int):
        if self.callback is not None:
            self.callback("s", value1, value2)
        else:
            print("None Callback")
            print(f"{self.__class__}, value1:{value1}, value2:{value2}")


    def v_scale_move(self, value1:int, value2:int):
        if self.callback is not None:
            self.callback("v", value1, value2)
        else:
            print("None Callback")
            print(f"{self.__class__}, value1:{value1}, value2:{value2}")


if __name__ == "__main__":
    def func1(text, value1, value2):
        print(text, value1, value2)

    app = tk.Tk()
    frame1 = HSVScaleFrame(app , "HSV_Scroll")
    frame1.grid(column=0, row=0)
    frame1.set_callback(func1)
    app.mainloop()