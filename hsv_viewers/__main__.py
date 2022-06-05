from typing import Dict, Any
from argparse import ArgumentParser
import tkinter as tk

from gui_app import MainFrame, App
from ctrl_gui import Ctrl

def parse_args() -> Dict[str, Any]:
    parser = ArgumentParser()
    parser.add_argument(
        "-i", "--img", type=str, 
        default="../data/ichigo_0001.jpg")

    args = vars(parser.parse_args())
    return args

def main():
    args = parse_args()

    img_path = args['img']

    app = App()
    ctrl = Ctrl(app)
    ctrl.load_img(img_path)

    ctrl.begin()

if __name__ == "__main__":
    main()