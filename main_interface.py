import tkinter as tk
import PIL
import pandas
import requests
import subprocess

from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Button,Radiobutton, Style, Label
from dataset_interface import get_suggested_keywords
from exchange_rate import EUR_to_USD
from textpdf import PDF
from fpdf import FPDF

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

        def get_result_for_advice(outcome,check):
            L = str()
            SEA = outcome[0]
            SEO = outcome[1]
            if len(SEA) > 0 and len(SEO) > 0:
                L +=('SEA & SEO\n')
                L +=('Met behulp van de gegevens die u heeft ingevuld is berekend dat u met betaald adverteren winst kan maken met voor uw product relevante keywords.\n')
                L +=('Hierom raden wij aan om geld te besteden aan betaald adverteren op google. De keywords die wij aanraden voor SEA zijn als volgt:\n\n')
                for i in range(3):
                    if i < len(SEA):
                        L +=(str(SEA[i])+'\n')
                L +=('\n')
                L +=('Deze keywords hebben wij geselecteerd op basis van de winst per product en het zoekvolume van het keyword.\n')
                L +=('Organisch verkeer naar de website krijgen door middel van SEO lijkt ons ook haalbaar. Dit is omdat de competitie voor de relevante zoektermen laag genoeg is. De aangeraden keywords zijn als volgt:\n\n')
                L +=('         SEO\n')
                for i in range(3):
                    if i < len(SEO):
                        L +=(str(SEO[i])+'\n')
                L +=('\n')
            elif len(SEA) > 0:
                L +=('SEA\n')
                L +=('Met behulp van de gegevens die u heeft ingevuld is berekend dat u met betaald adverteren winst kan maken met voor uw product relevante keywords.\n')
                L +=('Hierom raden wij aan om geld te besteden aan betaald adverteren op google. De keywords die wij aanraden voor SEA zijn als volgt:\n\n')
                for i in range(3):
                    if i < len(SEA):
                        L +=(str(SEA[i])+'\n')
                if check == True:
                    L +=('\n')
                    L +=('Deze keywords hebben wij geselecteerd op basis van de winst per product en het zoekvolume van het keyword.\n')
                    L +=('Organisch verkeer naar de website krijgen door middel van SEO lijkt ons niet haalbaar. Dit is omdat de competitie voor de relevante zoektermen te hoog is.')
            elif len(SEO) > 0:
                L +=('SEO\n')
                L +=('Met behulp van de gegevens die u heeft ingevuld is berekend dat u met betaald adverteren geen winst kan maken met voor uw product relevante keywords.\n')
                L +=('Hierom raden wij aan geen geld te besteden aan betaald adverteren op google.')
                L +=('Organisch verkeer naar de website krijgen door middel van SEO lijkt ons wel haalbaar. Dit is omdat de competitie voor de relevante zoektermen laag genoeg is.')
                L +=('De keywords die wij aanraden zijn gekozen op basis van de winst per product en het zoekvolume van het keyword.\n')
                L +=('De aangeraden keywords voor SEO zijn als volgt:\n\n')
                for i in range(3):
                    if i < len(SEO):
                        L +=(str(SEO[i])+'\n')
                L +=('\n')
            else:
                L +=('Adverteren op Google niet haalbaar\n')
                L +=('Met behulp van de gegevens die u heeft ingevuld is berekend dat u met betaald adverteren geen winst kan maken met voor uw product relevante keywords.\n')
                L +=('Hierom raden wij aan geen geld te besteden aan betaald adverteren op google.')
                if check == True:
                    L +=('Organisch verkeer naar de website krijgen door middel van SEO lijkt ons ook niet haalbaar. Dit is omdat de competitie voor de relevante zoektermen te hoog is.')
            return L
        
        def display_template(keywords,prod_val,conv,check):
            prod_val = EUR_to_USD(prod_val)
            suggestions = get_suggested_keywords(keyword=keywords,avg_product_value=prod_val,conv=conv,check_seo=bool(check))
            L = get_result_for_advice(suggestions)
            pdf = PDF()
            pdf.set_title('Social Brothers Advice Report')
            pdf.set_author('SB')
            pdf.print_chapter(1, 'Uitkomsten', L)
            pdf.output('Advice.pdf', 'F')
            subprocess.Popen(['Advice.pdf'],shell=True)


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

        product_name_box = tk.Text(frame2, height=1, width=20)
        product_name_box.place(x=180,y=20)

        product_label = tk.Label(frame2,text="Average profit per sale: (€)",bg="lightgray",fg="black")
        product_label.place(x=10,y=50,height=18)

        product_value = DoubleVar()
        product_box = tk.Entry(frame2,textvariable = product_value)
        product_box.place(x=180,y=50,width=165)

        conversion_label = tk.Label(frame2,text="Conversion to lead ratio:",bg="lightgray",fg="black")
        conversion_label.place(x=10,y=80,height=18)

        conversion_lead_value = DoubleVar()
        conversion_box = tk.Entry(frame2,textvariable = conversion_lead_value)
        conversion_box.place(x=180,y=80,width=165)

        conversion_label = tk.Label(frame2,text="Lead to sale ratio:",bg="lightgray",fg="black")
        conversion_label.place(x=10,y=110,height=18)

        conversion_sale_value = DoubleVar()
        conversion_box = tk.Entry(frame2,textvariable = conversion_sale_value)
        conversion_box.place(x=180,y=110,width=165)

        check = IntVar()
        SEO_check = tk.Checkbutton(frame2, text="Enable SEO advice",bg="lightgray", variable=check)
        SEO_check.place(x=10,y=140,height=18)

        infobutton = tk.Button(frame2,text="info",bg='lightgray',bitmap="info",
                               command=lambda :window(self,"Here you find a short explanation\n on how to input the entry fields. \n\n Product name: keyword which\n best describes the product i.e. \n stofzuiger or koelkast\n\n Average profit per sale: input in euros. \n\n Conversion to lead ratio: input in decimals. \n\n Conversion to sale ratio: input in decimals."))
        infobutton.place(x=385,y=194)

        Runbutton1 = tk.Button(frame2, text="Get Advice",bg="lightgray",fg="black",
                               command=lambda : display_template(keywords=product_name_box.get(1.0, tk.END+"-1c"),
                                                                 conv=(conversion_lead_value.get()*conversion_sale_value.get()),
                                                                 prod_val=product_value.get(),
                                                                 check=check.get()))
        Runbutton1.place(x=143,y=170,height=33,width=120)

        frame3 = tk.Frame(self,bg="lightgray",name="frame3")
        frame3.place(x=5, y=200)
        tabControl.add(frame3, text='B2C')

        bg_label = tk.Label(frame3, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render

        product_name = tk.Label(frame3,text="Product name:",bg="lightgray",fg="black")
        product_name.place(x=10,y=20,height=18)

        product_name_box1 = tk.Text(frame3,height=1,width=20)
        product_name_box1.place(x=180,y=20)

        product_label = tk.Label(frame3,text="Average profit per sale: (€)",bg="lightgray",fg="black")
        product_label.place(x=10,y=50,height=18)

        product_value1 = DoubleVar()
        product_box = tk.Entry(frame3,textvariable = product_value1)
        product_box.place(x=180,y=50,width=165)

        conversion_label = tk.Label(frame3,text="Conversion to sale ratio:",bg="lightgray",fg="black")
        conversion_label.place(x=10,y=80,height=18)

        conversion_value1 = DoubleVar()
        conversion_box = tk.Entry(frame3,textvariable = conversion_value1)
        conversion_box.place(x=180,y=80,width=165)

        check1 = IntVar()
        SEO_check = tk.Checkbutton(frame3, text="Enable SEO advice",bg="lightgray", variable=check1)
        SEO_check.place(x=10,y=110,height=18)

        infobutton = tk.Button(frame3,text="info",bg='lightgray',bitmap="info",
                               command=lambda :window(self,"Here you find a short explanation\n on how to input the entry fields. \n\n Product keywords: keywords which\n best describe the product separated. \n by a comma. \n\n Average profit per sale: input in euros. \n\n Conversion to sale ratio: input in decimals."))
        infobutton.place(x=385,y=194)

        Runbutton2 = tk.Button(frame3, text="Get Advice",bg="lightgray",fg="black",
                               command=lambda : display_template(keywords=product_name_box1.get(1.0, tk.END+"-1c"),
                                                                 conv=conversion_value1.get(),
                                                                 prod_val=product_value1.get(),
                                                                 check=check1.get()))
        Runbutton2.place(x=143,y=170,height=33,width=120)

        frame4 = tk.Frame(self,bg="lightgray",name="frame4")
        frame4.place(x=5, y=200)
        tabControl.add(frame4, text='Webshop')

        bg_label = tk.Label(frame4, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render

        product_name = tk.Label(frame4,text="Product name:",bg="lightgray",fg="black")
        product_name.place(x=10,y=20,height=18)

        product_name_box2 = tk.Text(frame4,height=1,width=20)
        product_name_box2.place(x=180,y=20)

        product_label = tk.Label(frame4,text="Average profit per sale: (€)",bg="lightgray",fg="black")
        product_label.place(x=10,y=50,height=18)

        product_value2 = DoubleVar()
        product_box = tk.Entry(frame4,textvariable = product_value2)
        product_box.place(x=180,y=50,width=165)

        conversion_label = tk.Label(frame4,text="Conversion to sale ratio:",bg="lightgray",fg="black")
        conversion_label.place(x=10,y=80,height=18)

        conversion_value2 = DoubleVar()
        conversion_box = tk.Entry(frame4,textvariable = conversion_value2)
        conversion_box.place(x=180,y=80,width=165)

        check2 = IntVar()
        SEO_check = tk.Checkbutton(frame4, text="Enable SEO advice",bg="lightgray", variable=check2)
        SEO_check.place(x=10,y=110,height=18)

        infobutton = tk.Button(frame4,text="info",bg='lightgray',bitmap="info",
                               command=lambda :window(self,"Here you find a short explanation\n on how to input the entry fields. \n\n Product name: keyword which\n best describes the product i.e. \n stofzuiger or koelkast\n\n Average profit per sale: input in Euros. \n\n conversion to sale ratio: input in decimals."))
        infobutton.place(x=385,y=194)

        Runbutton3 = tk.Button(frame4, text="Get Advice",bg="lightgray",fg="black",
                               command=lambda : display_template(keywords=product_name_box2.get(1.0, tk.END+"-1c"),
                                                                 conv=conversion_value2.get(),
                                                                 prod_val=product_value2.get(),
                                                                 check=check2.get()))
        Runbutton3.place(x=143,y=170,height=33,width=120)

        tabControl.place(x=0,y=59.4)

def main():
    root = Tk()
    root.geometry("400x300")
    root.resizable(False, False)
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
