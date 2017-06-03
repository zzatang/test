import os
import shutil
import subprocess
from tkinter import *
from tkinter import ttk, filedialog, messagebox

class atCaptionsort():
    def __init__(self, master):
        self.master = master
        self.master.title('Sort Images')
        self.master.resizable(False, False)
        
        self.main_frame = ttk.Frame(self.master)
        self.main_frame.pack(padx = 5, pady = 5)

        ttk.Label(self.main_frame, text = 'Source Directory:').grid(row = 0, column = 0, sticky = 'w')
        self.src_entry = ttk.Entry(self.main_frame, width = 54)
        self.src_entry.grid(row = 1, column = 0, sticky = 'e')
        self.src_entry.insert(0, '.\\images')
        ttk.Button(self.main_frame, text = 'Browse...', command = self.browse_src_callback).grid(row = 1, column = 1, sticky = 'w')

        ttk.Label(self.main_frame, text = 'Destination Directory:').grid(row = 2, column = 0, sticky = 'w')
        self.dest_entry = ttk.Entry(self.main_frame, width = 54)
        self.dest_entry.grid(row = 3, column = 0, sticky = 'e')
        self.dest_entry.insert(0, '.\\sorted')
        ttk.Button(self.main_frame, text = 'Browse...', command = self.browse_dest_callback).grid(row = 3, column = 1, sticky = 'w')

        self.copy_var = IntVar()
        self.copy_var.set(1)
        ttk.Checkbutton(self.main_frame, text = 'Copy Files', variable = self.copy_var).grid(row = 4, column = 0, columnspan = 2)
        ttk.Button(self.main_frame, text = 'Sort Images', command = self.sort_callback).grid(row = 5, column = 0, columnspan = 2)

    def browse_src_callback(self):
        pass

    def browse_dest_callback(self):
        pass

    def sort_callback(self):
        pass



def main():
    root = Tk()
    gui = atCaptionsort(root)
    root.mainloop()

if __name__ == '__main__': main()