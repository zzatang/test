from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bwDB import bwDB

class Feedback:
    def __init__(self, master):
        master.title('Explore NSW Feedback')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_left = ttk.Frame(master)
        self.frame_left.pack(side = LEFT)
        
        self.frame_header = ttk.Frame(self.frame_left)
        self.frame_header.pack()

        self.logo = PhotoImage(file = 'X:\\Lynda Training Courses\\Python\\4_Python_GUI_Development_With_Tkinter\\myform\\tour_logo.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Thanks for Exploring', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("We're glad you chose Explore NSW for your recent adventure.   "
                          "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(self.frame_left)
        self.frame_content.pack()
        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column =0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Aria', 10))

        self.entry_name.grid(row = 1, column = 0)
        self.entry_email.grid(row = 1, column = 1)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2)

        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')


        self.frame_right = ttk.Frame(master)
        self.frame_right.pack(side = LEFT)
        ttk.Label(self.frame_right, text = 'Databse Content').grid(row = 0, column = 0, columnspan = 3, sticky = 'w')
        self.frame_result = ttk.Frame(self.frame_right)
        self.frame_result.grid(row = 1, column = 1, columnspan = 3 )
       
        self.frame_listbox = ttk.Frame(self.frame_result)
        self.frame_listbox.pack()
        scrollbar = Scrollbar(self.frame_listbox, orient = 'vertical')
        self.listbox_result = Listbox(self.frame_listbox, width = 50, height = 10, yscrollcommand=scrollbar.set)
        scrollbar.config(command = self.listbox_result.yview)
        scrollbar.pack(side = 'right', fill='y')
        self.listbox_result.pack()

        ttk.Label(self.frame_result, text = 'Comments').pack()

        self.frame_comments = ttk.Frame(self.frame_result)
        self.frame_comments.pack()
        scrollbar2 = Scrollbar(self.frame_comments, orient = 'vertical')
        self.text_show_comments = Text(self.frame_comments, width = 38, height = 10, state = 'disabled', wrap = WORD, yscrollcommand = scrollbar2.set)
        scrollbar2.config(command = self.text_show_comments.yview)
        scrollbar2.pack(side = 'right', fill='y')
        self.text_show_comments.pack()

        ttk.Button(self.frame_right, text = 'Refresh', command = self.refresh_list).grid(row = 2, column = 0)
        ttk.Button(self.frame_right, text = 'Delete All', command = self.delete_all_list).grid(row = 2, column = 1)
        self.button_delete_selected = ttk.Button(self.frame_right, text = 'Delete Selected', command = self.delete_selected, state = DISABLED)
        self.button_delete_selected.grid(row = 2, column = 2)


        self.__fn = ':memory:'
        self.__t = 'test'
        

        self.db = bwDB(filename = self.__fn, table = self.__t)
        self.db.sql_do('DROP TABLE IF EXISTS {}'.format(self.__t))
        self.db.sql_do('CREATE TABLE {} (id INTEGER PRIMARY KEY, name TEXT, email TEXT, comments TEXT)'.format(self.__t))


    def submit(self):
        record = dict( name = self.entry_name.get(), email = self.entry_email.get(), comments = self.text_comments.get(1.0, 'end'))
        self.db.insert(record)
        #print('Name: {}'.format(self.entry_name.get()))
        #print('Email: {}'.format(self.entry_email.get()))
        #print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        #self.refresh_list()
        self.clear()
        messagebox.showinfo(title = 'Explore NSW Feedback', message = 'Comments Submitted')

    def refresh_list(self):
        self.listbox_result.delete(0, 'end')
        self.text_show_comments.delete(1.0, 'end')
        for r in self.db.getrecs():
            record = '--'.join([str(r['id']),r['name'], r['email']])
            self.listbox_result.insert('end', record)
        self.listbox_result.bind('<<ListboxSelect>>', self.on_select)

        
    def on_select(self, evt):
        widget = evt.widget
        if widget.size() > 0:
            index = int(widget.curselection()[0])
            value = widget.get(index)
            self.__row_id = int(value.split('--')[0])
            sql = 'SELECT comments FROM {} WHERE id = ?'.format(self.__t)
            comment = self.db.sql_query_value(sql, [self.__row_id])
            self.text_show_comments.config(state = 'normal')
            self.text_show_comments.delete(1.0, 'end')
            self.text_show_comments.insert(INSERT, comment)
            self.text_show_comments.config(state = 'disabled')
            self.button_delete_selected.config(state = 'normal')
        
        

    def delete_all_list(self):
        self.db.sql_do('DELETE FROM {}'.format(self.__t))
        self.db.sql_do('VACUUM')
        self.listbox_result.delete(0, 'end')
        self.text_show_comments.config(state = 'normal')
        self.text_show_comments.delete(1.0, 'end')
        self.text_show_comments.config(state = 'disabled')

    def delete_selected(self):
        self.db.delete(self.__row_id)
        self.refresh_list()
     

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')
     
    
                                                             
def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    print('Done')
    

if __name__ == '__main__': main()
