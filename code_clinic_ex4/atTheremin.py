from tkinter import *
from tkinter import ttk

__version__ = '0.0.1'

class atTheremin():
    def __init__(self, master):
        self.prev = None
        master.attributes('-fullscreen', True)
        self.canvas = Canvas(master, background = 'black')
        self.canvas.pack(fill = BOTH, expand = True)
        self.canvas.create_text(master.winfo_screenwidth()//2, master.winfo_screenheight() , anchor ='s',
                                text = "Press 'Esc' to Quit", font = ('Helvetica', 32, 'bold'), fill = 'white')

        master.bind('<Motion>', self.mouse_move)
        master.bind('<ButtonPress>', self.mouse_down)
        master.bind('<ButtonRelease>', self.mouse_up)
        master.bind('<Escape>', lambda e: master.destroy())
               

    def mouse_move(self, event):
        R = int(255 * event.x/self.canvas.winfo_width() * (self.canvas.winfo_height() - (event.y + 1)) / self.canvas.winfo_height())
        B = int(255 * event.x/self.canvas.winfo_width() * (event.y + 1) / self.canvas.winfo_height())
        self.canvas.config( background = '#{:02x}50{:02x}'.format(R, B))

        if self.prev:
            self.canvas.create_line(self.prev.x, self.prev.y, event.x, event.y, width = 10, fill = '#{:02x}88{:02x}'.format(R, B))
            self.prev = event

    def mouse_down(self, event):
        self.prev = event

    def mouse_up(self, event):
        self.prev = None


def main():
    root = Tk()
    gui = atTheremin(root)
    root.mainloop()

if __name__ == '__main__': main()