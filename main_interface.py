import tkinter as tk
import PIL
import pandas

from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Button,Radiobutton, Style, Label
from dataset_interface import get_suggested_keywords

import os
path = os.path.dirname(os.path.abspath(__file__)) + "\\"

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        style = ttk.Style()
        style.theme_create( "SB", parent="alt", settings={"TNotebook": {"configure": {"background":"darkred","bordercolor":"black"}},"TNotebook.Tab": {"configure": {"padding": [5, 1], "background": "gray","foreground":"black"},"map":       {"foreground":[("selected", "black")],"background": [("selected", "lightgray")],"expand": [("selected", [1, 1, 1, 0])] } } } )
        style.theme_use("SB")

        self.canvas = Canvas(self, width=400, height=500)
        self.canvas.place(x = 0, y = 0)

        self.canvas2 = Canvas(self, width=400, height=55,bg="white")
        self.canvas2.place(x = 0, y = 0)
        self.canvas2.create_text(120,30,fill="gray",text="Predictive Advertisement Tool",font=("Impact",14))

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

        def display_template(prod,prod_val,conv):
            suggestions = get_suggested_keywords(avg_product_value=prod_val,conv=conv)
            

        def window(self,txt):
            info_window = tk.Toplevel(bg="lightgray")
            info_window.title("Info")
            info_window.geometry("250x200")
            info_window.resizable(False, False)
            label4 = tk.Label(info_window,text=txt,anchor = "e",justify = 'left',bg="lightgray",fg="black")
            label4.pack()
            info_window.mainloop()

        tabControl = ttk.Notebook(self,height=500,width=400)     

        frame2 = tk.Frame(self,bg="gray")
        frame2.place(x=5, y=140)
        tabControl.add(frame2, text='B2B')

        bg_label = tk.Label(frame2, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render
        
        product_name = tk.Label(frame2,text="Product name:",bg="lightgray",fg="black")
        product_name.place(x=10,y=20,height=18)

        product_name_value = str()
        product_name_box = tk.Entry(frame2,textvariable = product_name_value)
        product_name_box.place(x=102,y=20)

        product_label = tk.Label(frame2,text="Average profit per sale: ($)",bg="lightgray",fg="black")
        product_label.place(x=10,y=60,height=18)

        product_value = DoubleVar()
        product_box = tk.Entry(frame2,textvariable = product_value)
        product_box.place(x=166,y=60)

        conversion_label = tk.Label(frame2,text="Conversion to lead ratio:",bg="lightgray",fg="black")
        conversion_label.place(x=10,y=100,height=18)

        conversion_lead_value = DoubleVar()
        conversion_box = tk.Entry(frame2,textvariable = conversion_lead_value)
        conversion_box.place(x=158,y=100)

        conversion_label = tk.Label(frame2,text="Lead to sale ratio:",bg="lightgray",fg="black")
        conversion_label.place(x=10,y=140,height=18)

        conversion_sale_value = DoubleVar()
        conversion_box = tk.Entry(frame2,textvariable = conversion_sale_value)
        conversion_box.place(x=115,y=140)

        infobutton = tk.Button(frame2,text="info",bg='lightblue',bitmap="info",command=lambda :window(self,"Here you find a short explenation\n on how to input the entry fields. \n\n Product name: name of the product \n\n Average product value: input in euros \n\n Conversion to lead ratio: input in decimals \n\n conversion to sale ratio: input in decimals"))
        infobutton.place(x=385,y=394)

        Runbutton1 = tk.Button(frame2, text="Get Advice",bg="lightgray",fg="black",command=lambda : get_suggested_keywords(conv=(conversion_lead_value.get()*conversion_sale_value.get()), avg_product_value=product_value.get()))
        Runbutton1.place(x=143,y=170,height=33,width=120)

        frame3 = tk.Frame(self,bg="lightgray",name="frame3")
        frame3.place(x=5, y=200)
        tabControl.add(frame3, text='B2C')

        bg_label = tk.Label(frame3, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render

        product_name = tk.Label(frame3,text="Product name:",bg="lightgray",fg="black")
        product_name.place(x=10,y=20,height=18)

        product_name_value1 = str()
        product_name_box = tk.Entry(frame3,textvariable = product_name_value1)
        product_name_box.place(x=102,y=20)

        product_label = tk.Label(frame3,text="Average profit per sale: ($)",bg="lightgray",fg="black")
        product_label.place(x=10,y=60,height=18)

        product_value1 = DoubleVar()
        product_box = tk.Entry(frame3,textvariable = product_value1)
        product_box.place(x=166,y=60)

        conversion_label = tk.Label(frame3,text="Conversion to sale ratio:",bg="lightgray",fg="black")
        conversion_label.place(x=10,y=100,height=18)

        conversion_value1 = DoubleVar()
        conversion_box = tk.Entry(frame3,textvariable = conversion_value1)
        conversion_box.place(x=158,y=100)

        infobutton = tk.Button(frame3,text="info",bg='lightblue',bitmap="info",command=lambda :window(self,"Here you find a short explenation\n on how to input the entry fields. \n\n Product name: name of the product \n\n Average product value: input in euros \n\n Conversion to sale ratio: input in decimals"))
        infobutton.place(x=385,y=394)

        Runbutton2 = tk.Button(frame3, text="Get Advice",bg="lightgray",fg="black",command=lambda : get_suggested_keywords(conv=(conversion_lead_value.get()*conversion_sale_value.get()), avg_product_value=product_value.get()))
        Runbutton2.place(x=143,y=170,height=33,width=120)

        frame4 = tk.Frame(self,bg="lightgray",name="frame4")
        frame4.place(x=5, y=200)
        tabControl.add(frame4, text='Websop')

        bg_label = tk.Label(frame4, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render

        product_name = tk.Label(frame4,text="Product name:",bg="lightgray",fg="black")
        product_name.place(x=10,y=20,height=18)

        product_name_value2 = str()
        product_name_box = tk.Entry(frame4,textvariable = product_name_value2)
        product_name_box.place(x=102,y=20)

        product_label = tk.Label(frame4,text="Average profit per sale: ($)",bg="lightgray",fg="black")
        product_label.place(x=10,y=60,height=18)

        product_value2 = DoubleVar()
        product_box = tk.Entry(frame4,textvariable = product_value2)
        product_box.place(x=166,y=60)

        conversion_label = tk.Label(frame4,text="Conversion to sale ratio:",bg="lightgray",fg="black")
        conversion_label.place(x=10,y=100,height=18)

        conversion_value2 = DoubleVar()
        conversion_box = tk.Entry(frame4,textvariable = conversion_value2)
        conversion_box.place(x=158,y=100)

        infobutton = tk.Button(frame4,text="info",bg='lightblue',bitmap="info",command=lambda :window(self,"Here you find a short explenation\n on how to input the entry fields. \n\n Product name: name of the product \n\n Average product value: input in euros \n\n conversion to sale ratio: input in decimals"))
        infobutton.place(x=385,y=394)

        Runbutton3 = tk.Button(frame4, text="Get Advice",bg="lightgray",fg="black",command=lambda : get_suggested_keywords(conv=(conversion_lead_value.get()*conversion_sale_value.get()), avg_product_value=product_value.get()))
        Runbutton3.place(x=143,y=170,height=33,width=120)

        tabControl.place(x=0,y=59.4)

        #self.label2 = tk.Label(frame3,text="Business type:",bg="darkorange",fg="black")
        #self.label2.place(x=0,y=20,height=18)

        #business_type = ttk.Combobox(frame3,state="readonly", values=["B2B", "B2C","Webshop"])
        #business_type.place(x=80,y=20)
        #business_type.current(0)

def main():
    root = Tk()
    root.geometry("400x300")
    root.resizable(False, False)
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
