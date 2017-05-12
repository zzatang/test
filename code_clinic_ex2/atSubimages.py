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
        self.browse_button = ttk.Button(self.main_frame, text = 'Browse...', command = self.browse_callback)
        self.browse_button.grid(row = 1, column = 1, sticky = 'w')
        self.search_button = ttk(self.main_frame, text = 'Find Subset Images', command = self.search_callback)
        self.search_button.grid(row = 2, column = 0, columnspan = 2)

        self.result_table = ttk.Treeview(self.main_frame, column = ('subset'))
        self.result_table.heading('#0', text = 'Original Image')
        self.result_table.column('#0', width = 200)
        self.result_table.heading('subset', text = 'Subset Image')
        self.result_table.column('subset', width = 200)

        self.status_frame = ttk.Frame(self.master)
        self.status_frame.pack(fill = BOTH, expand = True)

        self.status_var = StringVar()
        self.status_label = ttk.Label(self.status_frame, textvariable = self.status_var)

        self.progress_var = DoubleVar()
        self.progressbar = ttk.Progressbar(self.status_frame, mode = 'determinate', variable = self.progress_var)
    
    def browse_callback(self):
        path = filedialog.askdirectory(initialdir = self.path_entry.get())
        self.path_entry.delete('0', END)
        self.path_entry.insert('0', path)

    def search_callback(self):
        self.start_time = time()

        try:
            self.path = self.path_entry.get()
            images = list(entry for entry in os.listdir(self.path) if entry.endswith('.jpg'))
        except:
            messagebox.showerror(title = 'Invalid Directory', message = 'Invalid Search Directory:\n' + self.path)
            return

        if len(images) < 2:
            messagebox.showerror(title = 'Not Enough Images', message = 'Need at least 2 images to analyse.')
            return

        self.queue = Queue()
        for i in images:
            for j in images:
                if i != j:
                    self.queue.put((i, j))
         
        self.result_table.grid_forget()
        self.result_table.delete(*self.result_table.get_children())
        
        self.status_var.set('Beginning...')
        self.status_label.pack(side = BOTTOM, fill = BOTH, expand = True)
        self.progressbar.config(value = 0.0, maximum = self.queue.qsize())
        self.progressbar.pack(side = BOTTOM, fill = BOTH, expand = True)
        self.browse_button.state(['disabled'])
        self.search_button.state(['disabled'])

    def process_queue(self):
        pair = self.queue.get()
        orig_img = Image.open(os.path.join(self.path, pair[0]))
        temp_img = Image.open(os.path.join(self.path, pair[1]))
            
       

def main():
    root = Tk()
    FindSubset(root)
    root.mainloop()

if __name__ == '__main__': main()