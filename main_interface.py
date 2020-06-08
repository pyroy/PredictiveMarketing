import tkinter as tk
import PIL

from feature_dict import *
from map_maker import query
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
        style.theme_create( "blue", parent="alt", settings={"TNotebook": {"configure": {"background":"white","bordercolor":"black"}},"TNotebook.Tab": {"configure": {"padding": [5, 1], "background": "darkblue","foreground":"white"},"map":       {"foreground":[("selected", "black")],"background": [("selected", "white")],"expand": [("selected", [1, 1, 1, 0])] } } } )

        style.theme_use("blue")

        self.canvas = Canvas(self, width=400, height=500)
        self.canvas.place(x = 0, y = 0)

        self.canvas2 = Canvas(self, width=400, height=55,bg="white")
        self.canvas2.place(x = 0, y = 0)
        self.canvas2.create_text(110,30,fill="black",text="LocationPredictor",font=("Impact",20))

        load = PIL.Image.open(path+"\\images\\lpr.png")
        load = load.resize((400,500), PIL.Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(load)
        img = self.canvas.create_image(200, 250, image=self.render,tags="background")

        self.master.title("Location Predictor")
        self.pack(fill=BOTH, expand=True)

        load2 = PIL.Image.open(path+"\\images\\nlr.png")
        load2 = load2.resize((100,50), PIL.Image.ANTIALIAS)
        self.render2 = ImageTk.PhotoImage(load2)
        img2 = self.canvas2.create_image(370, 30, image=self.render2)

        frame = Frame(self)
        frame.place(x=300,y=450)

        def window(self,txt):
            info_window = tk.Toplevel(bg="darkblue")
            info_window.title("Info")
            info_window.geometry("200x200")
            info_window.resizable(False, False)
            label4 = tk.Label(info_window,text=txt,bg="darkblue",fg="white")
            label4.pack()
            info_window.mainloop()

        def window1(self):
            window1 = tk.Toplevel(bg="darkblue")
            window1.title("Custom_waytypes")
            window1.geometry("400x320")
            window1.resizable(False, False)
            Checkbutton(window1, text="motorway", variable=motorway,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=0)
            Checkbutton(window1, text="trunk", variable=trunk,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=0)
            Checkbutton(window1, text="primary", variable=primary,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=0)
            Checkbutton(window1, text="secondary", variable=secondary,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=0)
            Checkbutton(window1, text="tertiary", variable=tertiary,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=50)
            Checkbutton(window1, text="residential", variable=residential,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=50)
            Checkbutton(window1, text="motorway_link", variable=motorway_link,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=50)
            Checkbutton(window1, text="trunk_link", variable=trunk_link,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=50)
            Checkbutton(window1, text="primary_link", variable=primary_link,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=100)
            Checkbutton(window1, text="secondary_link", variable=secondary_link,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=100)
            Checkbutton(window1, text="tertiary_link", variable=tertiary_link,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=100)
            Checkbutton(window1, text="living_street", variable=living_street,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=100)
            Checkbutton(window1, text="service", variable=service,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=150)
            Checkbutton(window1, text="track", variable=track,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=150)
            Checkbutton(window1, text="escape", variable=escape,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=150)
            Checkbutton(window1, text="road", variable=road,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=150)
            Checkbutton(window1, text="pedestrian", variable=pedestrian,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=200)
            Checkbutton(window1, text="footway", variable=footway,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=200)
            Checkbutton(window1, text="bridleway", variable=bridleway,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=200)
            Checkbutton(window1, text="path", variable=pat,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=200)
            Checkbutton(window1, text="sidewalk", variable=sidewalk,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=250)
            Checkbutton(window1, text="cycleway", variable=cycleway,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=250)
            Checkbutton(window1, text="steps", variable=steps,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=250)
            Checkbutton(window1, text="corridor", variable=corridor,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=250)
            Checkbutton(window1, text="unclassified", variable=unclassified,bg="darkblue",fg="white",selectcolor='black').place(x=130,y=290)
            Checkbutton(window1, text="crossing", variable=crossing,bg="darkblue",fg="white",selectcolor='black').place(x=260,y=290)
            window1.mainloop()

        def window2(self):
            window2 = tk.Toplevel(bg="darkblue")
            window2.title("Custom_surfacetypes")
            window2.geometry("450x300")
            window2.resizable(False, False)
            Checkbutton(window2, text="paved", variable=paved,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=0)
            Checkbutton(window2, text="asphalt", variable=asphalt,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=0)
            Checkbutton(window2, text="concrete", variable=concrete,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=0)
            Checkbutton(window2, text="concrete_lanes", variable=concrete_lanes,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=0)
            Checkbutton(window2, text="concrete_plates", variable=concrete_plates,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=50)
            Checkbutton(window2, text="paving_stones", variable=paving_stones,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=50)
            Checkbutton(window2, text="sett", variable=sett,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=50)
            Checkbutton(window2, text="unhewn_cobblestone", variable=unhewn_cobblestone,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=50)
            Checkbutton(window2, text="cobblestone", variable=cobblestone,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=100)
            Checkbutton(window2, text="metal", variable=metal,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=100)
            Checkbutton(window2, text="wood", variable=wood,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=100)
            Checkbutton(window2, text="unpaved", variable=unpaved,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=100)
            Checkbutton(window2, text="compacted", variable=compacted,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=150)
            Checkbutton(window2, text="fine_gravel", variable=fine_gravel,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=150)
            Checkbutton(window2, text="pebblestone", variable=pebblestone,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=150)
            Checkbutton(window2, text="dirt", variable=dirt,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=150)
            Checkbutton(window2, text="earth", variable=earth,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=200)
            Checkbutton(window2, text="grass", variable=grass,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=200)
            Checkbutton(window2, text="grass_paver", variable=grass_paver,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=200)
            Checkbutton(window2, text="ground", variable=ground,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=200)
            Checkbutton(window2, text="mud", variable=mud,bg="darkblue",fg="white",selectcolor='black').place(x=0,y=250)
            Checkbutton(window2, text="sand", variable=sand,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=250)
            Checkbutton(window2, text="woodchips", variable=woodchips,bg="darkblue",fg="white",selectcolor='black').place(x=100,y=250)
            Checkbutton(window2, text="snow", variable=snow,bg="darkblue",fg="white",selectcolor='black').place(x=200,y=250)
            Checkbutton(window2, text="salt", variable=salt,bg="darkblue",fg="white",selectcolor='black').place(x=300,y=250)
            window2.mainloop()

        tabControl = ttk.Notebook(self,height=500,width=400)     
        #frame2 = tk.Frame(self,bg="darkblue")
        #frame2.place(x=0, y=80)
        #tabControl.add(frame2, text='Complexity')

        #bg_label = tk.Label(frame2, image = self.render)
        #bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        #bg_label.image = self.render
        
        #infobutton = tk.Button(frame2,text="info",bitmap="info",command=lambda : window(self,"Complexity : The amount of detail \n displayed on the map(advanced \n detail contains almost all \n usefull data, but  takes longer \n to process, while Basic only \n uses the data necessary \n to be able to work).\n\n Fill in everything before\n running the program."))
        #infobutton.place(x=385,y=394)

        #self.Label1 = tk.Label(frame2,text="Algorithm:",bg="darkblue",fg="white")
        #self.Label1.place(x=0,y=50,height=25)

        #Radiobutton1 = tk.Radiobutton(frame2, text="Basic",value=1,bg="darkblue",fg="white",selectcolor='black')
        #Radiobutton1.place(x=60,y=50)

        #Radiobutton2 = tk.Radiobutton(frame2, text="Average",value=2,bg="darkblue",fg="white",selectcolor='black',tristatevalue=0)
        #Radiobutton2.place(x=115,y=50)

        #Radiobutton3 = tk.Radiobutton(frame2, text="Advanced",value=3,bg="darkblue",fg="white",selectcolor='black',tristatevalue=0)
        #Radiobutton3.place(x=185,y=50)

        #Runbutton = tk.Button(frame2, text="Run",bg="darkblue",fg="white",command=lambda : [check(),query(road_features,"goal_features",sightingdict,"vieuwtime",(entry_lat.get(),entry_lon.get()),combo.get())])
        #Runbutton.place(x=200,y=380,height=25,width=45)

        frame3 = tk.Frame(self,bg="darkblue")
        frame3.place(x=5, y=140)
        tabControl.add(frame3, text='Features')

        bg_label = tk.Label(frame3, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render

        time_label = tk.Label(frame3,text="Time passed:",bg="darkblue",fg="white")
        time_label.place(x=0,y=10)

        time = DoubleVar()
        time_passed = tk.Entry(frame3,textvariable = time)
        time_passed.place(x=73,y=10)

        self.label2 = tk.Label(frame3,text="Transport type:",bg="darkblue",fg="white")
        self.label2.place(x=0,y=50)

        transport_type = ttk.Combobox(frame3,state="readonly", values=["Car", "Bike","On foot","Military"])
        transport_type.place(x=90,y=50)
        transport_type.current(0)

        self.label3 = tk.Label(frame3,text="Terrain Type:",bg="darkblue",fg="white")
        self.label3.place(x=0,y=100)

        custom_waytype = tk.Button(frame3,text = "Custom",bg="darkblue",fg="white",command= lambda: window1(self))
        custom_waytype.place(x=100,y=100)

        motorway = IntVar()
        trunk = IntVar()
        primary = IntVar()
        secondary = IntVar()
        tertiary = IntVar()
        residential= IntVar()
        motorway_link = IntVar()
        trunk_link = IntVar()
        primary_link = IntVar()
        secondary_link = IntVar()
        tertiary_link = IntVar()
        living_street = IntVar()
        service = IntVar()
        track = IntVar()
        escape = IntVar()
        road = IntVar()
        pedestrian = IntVar()
        footway = IntVar()
        steps = IntVar()
        bridleway = IntVar()
        pat = IntVar()
        sidewalk = IntVar()
        cycleway = IntVar()
        corridor = IntVar()
        unclassified= IntVar()
        crossing = IntVar()

        waytype_label = tk.Label(frame3,text="Custom Waytype:",bg="darkblue",fg="white")
        waytype_label.place(x=0,y=100,height = 25)

        custom_surfacetype = tk.Button(frame3,text = "Custom",bg="darkblue",fg="white",command= lambda: window2(self))
        custom_surfacetype.place(x=115,y=150)

        paved = IntVar()
        asphalt = IntVar()
        concrete = IntVar()
        concrete_lanes = IntVar()
        concrete_plates = IntVar()
        paving_stones = IntVar()
        sett = IntVar()
        unhewn_cobblestone = IntVar()
        cobblestone = IntVar()
        metal = IntVar()
        wood = IntVar()
        unpaved = IntVar()
        compacted = IntVar()
        fine_gravel = IntVar()
        gravel = IntVar()
        pebblestone = IntVar()
        dirt = IntVar()
        grass_paver = IntVar()
        sand = IntVar()
        snow = IntVar()
        ice = IntVar()
        earth = IntVar()
        grass = IntVar()
        ground = IntVar()
        mud = IntVar()
        woodchips = IntVar()
        salt = IntVar()

        waytype_checkdict = {"motorway":motorway,"trunk":trunk,"primary":primary,"secondary":secondary,"tertiary":tertiary,"residential":residential,"motorway_link":motorway_link
                                 ,"trunk_link":trunk_link,"primary_link":primary_link,"secondary_link":secondary_link,"tertiary_link":tertiary_link,"living_street":living_street,
                                 "service":service,"track":track,"escape":escape,"road":road,"pedestrian":pedestrian,"footway":footway,"steps":steps,"bridleway":bridleway,"path":pat
                                 ,"sidewalk":sidewalk,"cycleway":cycleway,"corridor":corridor,"unclassified":unclassified,"crossing":crossing}
        surfacetype_checkdict = {"paved":paved,"asphalt":asphalt,"concrete":concrete,"concrete:lanes":concrete_lanes,"concrete:plates":concrete_plates,
                                     "paving_stones":paving_stones,"sett":sett,"unhewn_cobblestone":unhewn_cobblestone,"cobblestone":cobblestone,"metal":metal,"wood":wood,"unpaved":unpaved
                                     ,"compacted":compacted,"fine_gravel":fine_gravel,"gravel":gravel,"pebblestone":pebblestone,"dirt":dirt,"grass_paver":grass_paver,"sand":sand,"snow":snow,
                                     "ice":ice,"earth":earth,"grass":grass,"ground":ground,"mud":mud,"woodchips":woodchips,"salt":salt}


        customvar= IntVar()

        use_custom = Checkbutton(frame3,text="Use custom",variable = customvar,bg="darkblue",fg= "white",selectcolor= "black")
        use_custom.place(x = 300,y= 50)
        
        surface_label = tk.Label(frame3,text="Custom Surfacetype:",bg="darkblue",fg="white")
        surface_label.place(x=0,y=150,height = 25)

        self.next_label = tk.Label(frame3,bg="darkblue",fg="white",text="Area:")
        self.next_label.place(x=0,y=200)

        selectorlist = [{"area": ("greaterthan", 0.00000707)},{"area": ("greaterthan", 0.00001053)},{"area": ("greaterthan", 0.00001203)},
                        {"area": ("greaterthan", 0.00001243)},{"area": ("greaterthan", 0.00002125)},{"area": ("greaterthan", 0.00004781)},
                        {"area": ("greaterthan", 0.00000135)},{"area": ("greaterthan", 0.00005115)},{"area": ("greaterthan", 0.0000005)},
                        {"area": ("greaterthan", 0.00003047)},{"area": ("greaterthan", 0.00001147)},{"area": ("greaterthan", 0.00002132)},{"area": ("greaterthan", 0.00003587)},{"area": ("greaterthan", 0.00002100)}]

        selector = ttk.Combobox(frame3,state="readonly", values=["small car", "medium sized car","large car","large van","small truck","normal truck","bike","military drone","normal drone","bus","humvee","small tank","large tank","rocket system"])        
        selector.place(x=30, y=200)
        selector.current(0)

        infobutton = tk.Button(frame3,text="info",bitmap="info",command=lambda : window(self,"Select features i.e. the vehicle used \n or the type of roads to filter on"))
        infobutton.place(x=385,y=394)

        Runbutton2 = tk.Button(frame3, text="Run",bg="darkblue",fg="white",command=lambda : query(check(),check2(),update1(sightingdict,"frame5"),float(time_passed.get()),(float(entry_lat.get()),float(entry_lon.get())),combo.get()))
        Runbutton2.place(x=200,y=380,height=25,width=45)

        frame4 = tk.Frame(self,bg="darkblue",name="frame4")
        frame4.place(x=5, y=200)
        tabControl.add(frame4, text='Start&Goals')

        goaldict = dict()
        sightingdict = list()

        def new_entry(new_frame,y,listname,d,frame):
            listname.append(0)
            lat = IntVar()
            lon = IntVar()
            new_label = tk.Label(new_frame,bg="darkblue",fg="white",text="Latitude:")
            new_label.place(x=0,y=len(listname)*25+y)
            entry_lat = tk.Entry(new_frame,textvariable = lat,name=str(0-(len(listname))))
            entry_lat.place(x=50,y=len(listname)*25+y)
            new_label = tk.Label(new_frame,bg="darkblue",fg="white",text="Longitude:")
            new_label.place(x=180,y=len(listname)*25+y)
            entry_lon = tk.Entry(new_frame,textvariable = lon,name=str(len(listname)))
            entry_lon.place(x=245,y=len(listname)*25+y)
            d[len(listname)] = [lat.get(),lon.get()]

        def new_entry1(new_frame,y,listname,d,frame):
            listname.append(0)
            lat = DoubleVar()
            lon = DoubleVar()
            time = DoubleVar()
            new_label = tk.Label(new_frame,bg="darkblue",fg="white",text="Latitude:")
            new_label.place(x=0,y=len(listname)*25+y)
            entry_lat = tk.Entry(new_frame,textvariable = lat,name=str(0-(len(listname)*2)))
            entry_lat.place(x=50,y=len(listname)*25+y,width=60)
            new_label = tk.Label(new_frame,bg="darkblue",fg="white",text="Longitude:")
            new_label.place(x=110,y=len(listname)*25+y)
            entry_lon = tk.Entry(new_frame,textvariable = lon,name=str(len(listname)*2))
            entry_lon.place(x=170,y=len(listname)*25+y,width=60)
            new_label = tk.Label(new_frame,bg="darkblue",fg="white",text="Delta Time:")
            new_label.place(x=230,y=len(listname)*25+y)
            entry_time = tk.Entry(new_frame,textvariable = time,name=str(len(listname)*100))
            entry_time.place(x=300,y=len(listname)*25+y,width=60)
            d.append((float(time.get()),(float(lat.get()),float(lon.get()))))
            
        def update(d,frame):
            for i in range(len(d)):
                 d[i+1] = (int(self.nametowidget(str(frame)+"."+str(0-(i+1))).get()),int(self.nametowidget(str(frame)+"."+str(i+1)).get()))
            return d

        def update1(d,frame):
            for i in range(len(d)):
                 d[i] = (float(self.nametowidget(str(frame)+"."+str((i+1)*100)).get()),(float(self.nametowidget(str(frame)+"."+str(0-(i+1)*2)).get()),float(self.nametowidget(str(frame)+"."+str((i+1)*2)).get())))
            return d

        bg_label = tk.Label(frame4, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render

        self.label4 = tk.Label(frame4,bg="darkblue",fg="white",text="Starting Coördinates:")
        self.label4.place(x=0,y=50)

        infobutton = tk.Button(frame4,text="info",bitmap="info",command=lambda : window(self,"Fill in the starting Coördinates \n and the location"))
        infobutton.place(x=385,y=394)

        self.label5 = tk.Label(frame4,bg="darkblue",fg="white",text="Latitude:")
        self.label5.place(x=0,y=80)

        entry_lat = tk.Entry(frame4)
        entry_lat.place(x=50,y=80)

        self.label6 = tk.Label(frame4,bg="darkblue",fg="white",text="Longitude:")
        self.label6.place(x=180,y=80)

        entry_lon = tk.Entry(frame4)
        entry_lon.place(x=245,y=80)

        last_label = tk.Label(frame4,bg="darkblue",fg="white",text="location:")
        last_label.place(x=0,y=20,height = 20)

        combo = ttk.Combobox(frame4,state="readonly", values=["bremm", "heilbronn","oberhausen"])        
        combo.place(x=52, y=20)
        combo.current(0)

        frame4_list=[]
        waylist = list()
        surfacelist = list()
        max_speed = 0

        def check():
            if customvar.get() == True:
                for feature in FEATURES_CUSTOM:
                    if feature == "waytype":
                        for i in FEATURES_CUSTOM[feature]:
                            if waytype_checkdict[i].get() == True:
                                waylist.append(str(i))
                    if feature == "surfacetype":
                        for i in FEATURES_CUSTOM[feature]:
                            if surfacetype_checkdict[i].get() == True:
                                surfacelist.append(str(i))
                    if transport_type.get() == "Car":
                        max_speed = 60
                    if transport_type.get() == "bike":
                        max_speed = 20
                    if transport_type.get() == "On foot":
                        max_speed = 5
                    if transport_type.get() == "Military":
                        max_speed = 50
                    return {"waytype":waylist,"surfacetype":surfacelist,"max_speed":max_speed}
            if transport_type.get() == "Car":
                return FEATURES_AUTO
            elif transport_type.get() == "Bike":
                return FEATURES_FIETS
            elif transport_type.get() == "On foot":
                return FEATURES_VOET
            elif transport_type.get() == "Military":
                return FEATURES_MILITARY
                            
        def check2():
            if selector.get() == "small car":
                return selectorlist[0]
            elif selector.get() == "medium car":
                return selectorlist[1]
            elif selector.get() == "large car":
                return selectorlist[2]
            elif selector.get() == "large van":
                return selectorlist[3]
            elif selector.get() == "small truck":
                return selectorlist[4]
            elif selector.get() == "normal truck":
                return selectorlist[5]
            elif selector.get() == "bike":
                return selectorlist[6]
            elif selector.get() == "military drone":
                return selectorlist[7]
            elif selector.get() == "normal drone":
                return selectorlist[8]
            elif selector.get() == "bus":
                return selectorlist[9]
            elif selector.get() == "humvee":
                return selectorlist[10]
            elif selector.get() == "small tank":
                return selectorlist[11]
            elif selector.get() == "large tank":
                return selectorlist[12]
            elif selector.get() == "rocket system":
                return selectorlist[13]


        Runbutton3 = tk.Button(frame4, text="Run",bg="darkblue",fg="white",command=lambda : query(check(),check2(),update1(sightingdict,"frame5"),float(time_passed.get()),(float(entry_lat.get()),float(entry_lon.get())),combo.get()))
        Runbutton3.place(x=200,y=380,height=25,width=45)

        frame5 = tk.Frame(self,bg="darkblue",name="frame5")
        frame5.place(x=5, y=280)
        tabControl.add(frame5, text='Sightings')

        bg_label = tk.Label(frame5, image = self.render)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = self.render

        infobutton = tk.Button(frame5,text="info",bitmap="info",command=lambda : window(self,"Fill in Coördinates of sightings if \n there are any"))
        infobutton.place(x=385,y=394)

        self.label8 = tk.Label(frame5,bg="darkblue",fg="white",text="Coördinates sightings:")
        self.label8.place(x=0,y=40,height=25)

        frame5_list=[]

        button3 = tk.Button(frame5,text="New Entry",command=lambda : new_entry1(frame5,80,frame5_list,sightingdict,"frame5"))
        button3.place(x=125,y=40)

        Runbutton4 = tk.Button(frame5, text="Run",bg="darkblue",fg="white",command=lambda : query(check(),check2(),update1(sightingdict,"frame5"),float(time_passed.get()),(float(entry_lat.get()),float(entry_lon.get())),combo.get()))
        Runbutton4.place(x=200,y=380,height=25,width=45)

        tabControl.place(x=0,y=59.4)


def main():
    root = Tk()
    root.geometry("400x500")
    root.resizable(False, False)
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
