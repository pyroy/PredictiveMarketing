import tkinter as tk
import PIL

from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Button,Radiobutton, Style, Label

import os
path = os.path.dirname(os.path.abspath(__file__)) + "\\"

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        style = ttk.Style()
        style.theme_create( "Orange", parent="alt", settings={"TNotebook": {"configure": {"background":"white","bordercolor":"black"}},"TNotebook.Tab": {"configure": {"padding": [5, 1], "background": "darkorange","foreground":"black"},"map":       {"foreground":[("selected", "black")],"background": [("selected", "white")],"expand": [("selected", [1, 1, 1, 0])] } } } )

        style.theme_use("Orange")

        self.canvas = Canvas(self, width=400, height=500)
        self.canvas.place(x = 0, y = 0)

        self.canvas2 = Canvas(self, width=400, height=55,bg="white")
        self.canvas2.place(x = 0, y = 0)
        self.canvas2.create_text(120,30,fill="darkorange",text="Predictive advertisement tool",font=("Impact",14))

        load = PIL.Image.open(path+"\\images\\background.jpg")
        load = load.resize((400,500), PIL.Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = self.canvas.create_image(200, 250, image=self.render,tags="background")

        self.master.title('PAT')
        self.pack(fill=BOTH, expand=True)

        load2 = PIL.Image.open(path+"\\images\\social_brothers.png")
        load2 = load2.resize((150,100), PIL.Image.ANTIALIAS)
        self.render2 = ImageTk.PhotoImage(load2)
        img2 = self.canvas2.create_image(320, 30, image=self.render2)

        frame = Frame(self)
        frame.place(x=300,y=450)

        def window(self,txt):
            info_window = tk.Toplevel(bg="darkorange")
            info_window.title("Info")
            info_window.geometry("200x200")
            info_window.resizable(False, False)
            label4 = tk.Label(info_window,text=txt,bg="darkorange",fg="black")
            label4.pack()
            info_window.mainloop()

        tabControl = ttk.Notebook(self,height=500,width=400)     

        frame3 = tk.Frame(self,bg="darkorange")
        frame3.place(x=5, y=140)
        tabControl.add(frame3, text='Features')

        bg_label = tk.Label(frame3, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render

        product_label = tk.Label(frame3,text="Average product Value:",bg="darkorange",fg="black")
        product_label.place(x=0,y=60,height=18)

        product_value = DoubleVar()
        product_box = tk.Entry(frame3,textvariable = product_value)
        product_box.place(x=128,y=60)

        conversion_label = tk.Label(frame3,text="Conversion ratio:",bg="darkorange",fg="black")
        conversion_label.place(x=0,y=100,height=18)

        conversion_value = DoubleVar()
        conversion_box = tk.Entry(frame3,textvariable = conversion_value)
        conversion_box.place(x=96,y=100)

        self.label2 = tk.Label(frame3,text="Business type:",bg="darkorange",fg="black")
        self.label2.place(x=0,y=20,height=18)

        business_type = ttk.Combobox(frame3,state="readonly", values=["B2B", "B2C","Webshop"])
        business_type.place(x=80,y=20)
        business_type.current(0)

        infobutton = tk.Button(frame3,text="info",bg='darkorange',bitmap="info",command=lambda : window(self,"Select features i.e. Business type \n"))
        infobutton.place(x=385,y=394)

        Runbutton2 = tk.Button(frame3, text="Run",bg="darkorange",fg="black",command=lambda : test_func())
        Runbutton2.place(x=200,y=380,height=25,width=45)

        frame4 = tk.Frame(self,bg="darkorange",name="frame4")
        frame4.place(x=5, y=200)
        tabControl.add(frame4, text='Other_tab')

        bg_label = tk.Label(frame4, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render

        tabControl.place(x=0,y=59.4)


def main():
    root = Tk()
    root.geometry("400x500")
    root.resizable(False, False)
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
