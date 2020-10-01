from tkinter import *




# class Config_static:



class Config_dynamic:
    def __init__(self,root,config_name,default,row):
        self.default = default
        self.config_name = Label(root,text=f"{config_name}:")
        self.lab = Label(root,text=self.default)
        self.entry = Entry(root)
        self.entry.insert(END,self.default)
        self.button = Button(root,text="Update",command=self.update_configs)
        self.config_name.grid(row=row,column = 0)
        self.lab.grid(row=row,column = 1)
        self.entry.grid(row=row,column = 2)
        self.button.grid(row=row,column = 3)

    def update_configs(self):
        # v = entry.get()
        self.lab.config(text=self.entry.get())
