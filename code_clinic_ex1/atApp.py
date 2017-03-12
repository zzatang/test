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
        self._createGUI()
        self.database = lpoDB.lpoDB()

    
    def _createGUI(self):

        # create style
        bgcolor = '#CCCCFF'
        self.master.configure(background = bgcolor)
        self.master.title("AT Testing")
        self.master.resizable(False, False)
        self.style = ttk.Style()
        self.style.configure("TFrame", background = bgcolor)
        self.style.configure("TButton", background = bgcolor)
        self.style.configure("TLabel", background = bgcolor)
        self.style.configure("Status.TLabel", background = bgcolor, font = ("Arial Black", 10))
        self.style.configure("Result.TLabel", background = bgcolor, font = ("Arial Black", 10))

        # create and display header
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack(side = TOP)
        self.logo = PhotoImage(file = "lpo_logo.gif")
        ttk.Label(self.frame_header, image = self.logo).pack()

        # create and display input 
        self.frame_input = ttk.Frame(self.master)
        self.frame_input.pack(side = TOP)
        
        ttk.Label(self.frame_input, text = "Start Date:").grid(row = 0, column = 1, columnspan = 3, sticky = "sw")

        
        
        



def main():
    root = Tk()
    app = atApp(root)
    root.mainloop()

if __name__ == "__main__": main()