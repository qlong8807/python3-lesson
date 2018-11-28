#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'简单的GUI窗口'

__author__ = 'Jans'

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text='Name:')
        self.helloLabel.pack()#pack()把widget加入到父容器，pack()是简单布局，还有grid()布局
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.sayHelloButton = Button(self,text='sayHello',command=self.hello)
        self.sayHelloButton.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'World!'
        messagebox.showinfo('这是一个提示框','Hello %s' % name)

app = Application()
#设置窗口标题
app.master.title('Title1')
#主消息循环
app.mainloop()