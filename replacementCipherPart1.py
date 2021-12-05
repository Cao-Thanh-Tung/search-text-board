import tkinter as tk
from tkinter import Entry, Frame, Label, ttk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter - replacement ciphergraphy')
        self.geometry('500x150')
        self.frame = Frame(self)
        self.__input = Entry(self, width = 300)
        self.__input.bind('<Return>', lambda e: self.creater())
        self.__input.pack(fill = 'x',padx=5,ipadx=2,ipady=5)
        self.input = ''
        self.__output = Label(self, text = 'result')
        self.__output.pack()
        self.frame.pack()
        self.keybox = tuple('hello')
    def creater(self):
        if self.input != '':
            for i in self.keybox:
                i[1].destroy()
                i[2].destroy()
        self.input = self.__input.get()
        self.__output['text'] = self.input
        key = set(self.input)
        self.keybox = tuple([i,tk.Entry(self.frame, width = 5),tk.Label(self.frame,text=i)] for i in key)
        for i in self.keybox:
            tmp = []
            c = 0
            for k in self.input:
                if i[0] == k:
                    tmp.append(c)
                c += 1
            i.append(tmp)
        c = 0
        h = 0
        for e in self.keybox:
            if e[2]['text'] == ' ':
                e[2]['text'] = 'space'
            e[2].grid(column = 2*c, row = h, padx = 5)
            e[1].bind('<Return>',lambda ev,e = e: self.analize(e))
            e[1].grid(column = 2*c +1, row = h, padx = 5)
            c += 1
            if c == 7:
                c = 0
                h +=1
    def analize(self,e):
        tmp = list(self.input)
        for i in e[3]:
            tmp[i] = e[1].get()
        self.input = ''.join(tmp)
        self.__output['text'] = self.input
if __name__ == "__main__":
    app = App()
    app.mainloop()