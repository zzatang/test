import os
import numpy as np
from math import sqrt
from time import time
from queue import Queue
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageChops
from skimage.feature import match_template

__version__ = '0.0.1'

MAX_WIDTH = 640
MAX_HEIGHT = 640
RMS_THRESHOLD = 50

class FindSubset:
    def __init__(self, master):
        self.master = master
        self.master.title('Finding Subset Images')
        self.master.resizable(False, False)

        self.main_frame = ttk.Frame(self.master)
        self.main_frame.pack(padx = 5, pady = 5)

        ttk.Label(self.main_frame, text = 'Search Directory:').grid(row = 0, column = 0, sticky = 'w')
        self.path_entry = ttk.Entry(self.main_frame, width = 54)
        self.path_entry.grid(row = 1, column = 0, sticky = 'e')
        self.path_entry.insert(0, '.\\images')
        self.browse_button = ttk.Button(self.main_frame, text = 'Browse...', command = '')
        self.browse_button.grid(row = 1, column = 1, sticky = 'w')
        self.search_button = ttk(self.main_frame, text = 'Find Subset Images', command = '')
        self.search_button.grid(row = 2, column = 0, columnspan = 2)




def main():
    root = Tk()
    FindSubset(root)
    root.mainloop()

if __name__ == '__main__': main()