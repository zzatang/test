from tkinter import *
from tkinter import ttk, messagebox
from statistics import mean, median
from datetime import date
import lpoDB

__version__ = '0.0.1'

class atApp:
    "This is the top level module"
    
    def __init__ (self, master):
        self.master = master
        self.database = lpoDB.lpoDB()

    
    def _createGUI(self):
        bgcolor = '#CCCCFF'
        self.master.configure(background = bgcolor)
        




def main():
    root = Tk()
    app = atApp(root)
    root.mainloop()

if __name__ == "__main__": main()