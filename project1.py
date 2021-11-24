import tkinter as tk
from tkinter import ttk
from tkinter.constants import TRUE
from typing import Text
class App(tk.Tk):
    def __new__(cls):
        return super().__new__(cls)
    def __init__(self):
        super().__init__()
        self.__title = 'project'
        self.__logo = 'icon.ico'
        self.__height = 240
        self.__width = 480
        self.__marginy = int(self.winfo_screenheight()/2 - self.height/2)
        self.__marginx = int(self.winfo_screenwidth()/2 - self.width/2)
        self.geometry(f'{{width}}x{{height}}+{{marginx}}+{{marginy}}'.format(width = self.width,
                                                                             height = self.height,
                                                                             marginx = self.margin[0],
                                                                             marginy = self.margin[1]))
        self.title = f'{{title}}'.format(title = self.__title)
        self.iconbitmap(f'{{}}'.format(self.__logo))
        # self.resizable(0,0)
        self.attributes('-alpha', 0.8)
        self.attributes('-topmost', True)
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @property
    def margin(self):
        return (self.__marginx, self.__marginy)
if __name__ == '__main__':
    root = App()
    root.columnconfigure(0, weight = 8)
    root.columnconfigure(1, weight = 2)
    frame_left = ttk.Frame(root, height = 200,
                           width = 360,
                           padding = 5,
                           borderwidth=5,
                           relief='sun')
    frame_left.grid(column = 0, row = 0, padx = 5, sticky = tk.NS)
    frame_right = ttk.Frame(root, height = 200,
                            width = 90,
                            padding = 5,
                            borderwidth = 5,
                            relief = 'sun')
    frame_right.grid(column = 1, row = 0, padx = 5, sticky = tk.NE)
    findText = list()
    findText.append(tk.Entry(frame_left, width = 50))
    findText.append(tk.Entry(frame_left, width = 50))
    for widget in findText:
        widget.grid(column = 1,padx = 2, pady = 2, sticky = tk.NS)
    text = list()
    text.append(tk.Label(frame_left, text = 'find'))
    text.append(tk.Label(frame_left, text = 'replace by'))
    text[0].grid(column = 0, row = 0,padx = 2, pady = 2, sticky = tk.W)
    text[1].grid(column = 0, row = 1,padx = 2, pady = 2, sticky = tk.W)
    text.append(tk.Label(frame_left, text = 'replace with'))
    text.append(tk.Label(frame_left, text = 'search'))
    text[2].grid(column = 0, row = 2,padx = 2, pady = 2, sticky = tk.W)
    text[3].grid(column = 0, row = 3,padx = 2, pady = 2, sticky = tk.W)
    frame_left.columnconfigure(0,weight = 100)
    frame_left.columnconfigure(1,weight = 200)
    frame_left.rowconfigure(0,weight = 1)
    frame_left.rowconfigure(1,weight = 1)
    frame_left.rowconfigure(2,weight = 1)
    frame_left.rowconfigure(3,weight = 1)
    for i in range(4):
        btn = ttk.Button(frame_right, text='button').grid(pady = 2, padx = 2,sticky = tk.NS, ipady = 8)
    frame_right.rowconfigure(0,weight = 1)
    frame_right.rowconfigure(1,weight = 1)
    frame_right.rowconfigure(2,weight = 1)
    frame_right.rowconfigure(3,weight = 1)
    root.mainloop()
# Completed project 1 (remote board)