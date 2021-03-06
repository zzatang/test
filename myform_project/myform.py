﻿from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bwDB import bwDB
from atDB import atDB

class Feedback:

    intRecord = 0
    strRecord = 'Number of record: '

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

        self.logo = PhotoImage(file = 'tour_logo.gif')
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
        self.frame_result = ttk.Frame(self.frame_right)
        self.frame_result.grid(row = 1, column = 0, columnspan = 3 )
       
        self.label_record = ttk.Label(self.frame_result, text = ''.join([self.strRecord, str(self.intRecord)]))
        self.label_record.grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        self.frame_listbox = ttk.Frame(self.frame_result)
        self.frame_listbox.grid(row = 1, column =0)
        scrollbar = Scrollbar(self.frame_listbox, orient = 'vertical')
        
        self.treeview_result = ttk.Treeview(self.frame_listbox)
        self.treeview_result['columns'] = ('Name', 'Email')
        self.treeview_result.heading('#0', text = 'id')
        self.treeview_result.heading('Name', text = 'Name')
        self.treeview_result.heading('Email', text = 'Email')
        self.treeview_result.column('#0', width = 30)
        self.treeview_result.column('Name', width = 150)
        self.treeview_result.column('Email', width = 150)
        scrollbar.config(command = self.treeview_result.yview)
        scrollbar.pack(side = 'right', fill='y')
        self.treeview_result.pack()
             
        ttk.Label(self.frame_result, text = 'Comments').grid(row = 2, column = 0,padx = 5, sticky = 'sw')

        self.frame_comments = ttk.Frame(self.frame_result)
        self.frame_comments.grid(row = 3, column = 0)
        scrollbar2 = Scrollbar(self.frame_comments, orient = 'vertical')
        self.text_show_comments = Text(self.frame_comments, width = 38, height = 10, state = 'disabled', wrap = WORD, yscrollcommand = scrollbar2.set)
        scrollbar2.config(command = self.text_show_comments.yview)
        scrollbar2.pack(side = 'right', fill='y')
        self.text_show_comments.pack()

        ttk.Button(self.frame_right, text = 'Refresh', command = self.refresh_list).grid(row = 2, column = 0, padx = 5, pady = 5)
        ttk.Button(self.frame_right, text = 'Delete All', command = self.delete_all_list).grid(row = 2, column = 1, padx = 5, pady = 5)
        self.button_delete_selected = ttk.Button(self.frame_right, text = 'Delete Selected', command = self.delete_selected, state = DISABLED)
        self.button_delete_selected.grid(row = 2, column = 2, padx = 5, pady = 5)

        self.__fn = ':memory:'
        self.__t = 'test'
 
        self.db = atDB(filename = self.__fn, table = self.__t)
        self.db.sql_do('DROP TABLE IF EXISTS {}'.format(self.__t))
        self.db.sql_do('CREATE TABLE {} (id INTEGER PRIMARY KEY, name TEXT, email TEXT, comments TEXT)'.format(self.__t))

    def submit(self):
        record = dict( name = self.entry_name.get(), email = self.entry_email.get(), comments = self.text_comments.get(1.0, 'end'))
        if record['name'] and record['email'] and record['comments'] != '\n':
            self.db.insert(record)
            #print('Name: {}'.format(self.entry_name.get()))
            #print('Email: {}'.format(self.entry_email.get()))
            #print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
            #self.refresh_list()
            self.clear()
            messagebox.showinfo(title = 'Explore NSW Feedback', message = 'Comments Submitted')
        else:
            messagebox.showerror(title = 'Explore NSW Feedback', message = 'All fields need to be filled in')

    def refresh_list(self):
        self.treeview_result.delete(*self.treeview_result.get_children())
        self.text_show_comments.config(state = 'normal')
        self.text_show_comments.delete(1.0, 'end')
        self.text_show_comments.config(state = 'disabled')
        for r in self.db.getrecs():
             self.treeview_result.insert('', 'end', text = str(r['id']), values = (r['name'], r['email']))
        self.treeview_result.bind('<<TreeviewSelect>>', self.on_select)
        self.intRecord = self.db.countrecs()
        self.label_record['text'] = ''.join([self.strRecord, str(self.intRecord)])
        self.button_delete_selected.config(state = 'disabled')

        
    def on_select(self, evt):
        curItem = self.treeview_result.focus()
        selectedItem = self.treeview_result.item(curItem)
        self.__row_id = int(selectedItem['text'])
        sql = 'SELECT comments FROM {} WHERE id = ?'.format(self.__t)
        comment = self.db.sql_query_value(sql, [self.__row_id])
        self.text_show_comments.config(state = 'normal')
        self.text_show_comments.delete(1.0, 'end')
        self.text_show_comments.insert(INSERT, comment)
        self.text_show_comments.config(state = 'disabled')
        self.button_delete_selected.config(state = 'normal')
        
        

    def delete_all_list(self):
        if messagebox.askokcancel("Verify", "Ok to delete all records?"):
            self.db.sql_do('DELETE FROM {}'.format(self.__t))
            self.db.sql_do('VACUUM')
            self.refresh_list()


    def delete_selected(self):
        if messagebox.askokcancel("Verify", "Ok to delete the selected record?"):
            self.db.delete(self.__row_id)
            self.refresh_list()
            self.button_delete_selected.config(state = 'disabled')
     

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')
     
    
                                                             
def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    #print('Done')
    

if __name__ == '__main__': main()
