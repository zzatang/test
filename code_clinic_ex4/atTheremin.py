from tkinter import *
from tkinter import ttk

__version__ = '0.0.1'

class atTheremin():
    def __init__(self, master):
        self.prev = None
        master.attributes('-fullscreen', True)
        self.canvas = Canvas(master, background = 'black')
        self.canvas.pack(fill = BOTH, expand = True)
        self.canvas.create_text(self.canvas.winfo_width()//2, self.canvas.winfo_height(), anchor ='s',
                                text = "Press 'Esc' to Quit", font = ('Helvetica', 32, 'bold'), fill = 'white')

        master.bind('<Motion>', self.mouse_move)
        master.bind('<BottonPress>', self.move_down)
        master.bind('<BottonRelease>', self.mouse_up)
        master.bind('Escape', lambda e: master.destroy())
               

    def mouse_move(self, event):
        R = int(255 * event.x/self.canvas.winfo_width() * (self.canvas.winfo_height() - (event.y + 1)) / self.canvas.winfo_height())
        B = int(255 * event.x/self.canvas.winfo_width() * (event.y + 1) / self.canvas.winfo_height())
        self.canvas.config( background = '#{:02x}50{:02x}'.format(R, B))


    def mouse_down(self, event):
        pass

    def mouse_up(self, event):
        pass


def main():
    root = Tk()
    gui = atTheremin(root)
    root.mainloop()

if __name__ == '__main__': main()