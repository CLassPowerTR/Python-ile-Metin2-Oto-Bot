import customtkinter
import tkinter as tk
import threading
import time
from Phebia2_Bot import otoMetinMenu
from Phebia2_Bot import otoMetinMenuAlternatif
from Phebia2_Bot import otoGirisMenu



class Window(customtkinter.CTk):
    def __init__(self,hwnd,hwnd1,titleName, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hwnd = hwnd
        self.hwnd1 = hwnd1
        self.geometry("360x420")
        self.resizable(width = False, height = False)
        version = customtkinter.CTkLabel(self, text="CLassPowerTR | METİN_BOTU_Version v0.2.0",width=15,height=8,corner_radius=8)
        version.pack(side= tk.BOTTOM)
        self.title(titleName)
        self.menu = customtkinter.CTkTabview(self)
        self.protocol("WM_DELETE_WINDOW", self.pencereyiKapat)
        self.menu.pack(side= tk.TOP,expand=True, fill="both")
        self.otoGiris = self.menu.add("Oto Giriş")
        self.otoMetin = self.menu.add("Oto Metin")
        self.otoTus = self.menu.add("Oto Tuş")
        self.labelWidth=12
        self.labelHeight=12
        self.labelCornerRadius=8
        self.entryWidth=60
        self.entryHeight=20
        self.entryCornerRadius=8
        self.checkboxHeight=20
        self.checkboxWidth=20
        self.checkboxCornerRadius=6
        self.optionMenuWidth=100
        self.optionMenuHeight=20
        self.optionMenuCornerRadius=8
        ################################### OTO GİRİŞ ###########################################
        self.after(1, otoGirisMenu.AllView(self,self.hwnd,self.hwnd1))
        ################################### OTO METİN ###########################################
        self.after(1, otoMetinMenu.AllView(self,self.hwnd,self.hwnd1))
        ################################### OTO TUŞ ###########################################
        otoTusBasla = tk.IntVar(self)
        otoTusBasla.set(0)
        otoTusDurum = customtkinter.CTkLabel(self.otoTus, text="Deaktif",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        otoTusDurum.grid(row=1,column=3)
        otoTusEntryValue = tk.StringVar(self)
        otoTusEntryValue.set("F4")
        otoTusEntry = customtkinter.CTkEntry(self.otoTus,textvariable=otoTusEntryValue,width=self.entryWidth,height=self.entryHeight,corner_radius=self.entryCornerRadius,text_color="#bababa").grid(row=1,column=0)
        otoTusButton = customtkinter.CTkCheckBox(self.otoTus,text="Oto Tuşu Başlat",variable=otoTusBasla, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",width=1,height=1,checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=1,column=2)

        otoTusBasla1 = tk.IntVar(self)
        otoTusBasla1.set(0)
        otoTusDurum1 = customtkinter.CTkLabel(self.otoTus, text="Deaktif",corner_radius=8,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        otoTusDurum1.grid(row=2,column=3)
        otoTusEntryValue1 = tk.StringVar(self)
        otoTusEntryValue1.set("space")
        otoTusEntry1 = customtkinter.CTkEntry(self.otoTus,textvariable=otoTusEntryValue1,width=self.entryWidth,height=self.entryHeight,corner_radius=self.entryCornerRadius,text_color="#bababa").grid(row=2,column=0)
        otoTusButton1 = customtkinter.CTkCheckBox(self.otoTus,text="Oto Tuşu Başlat",variable=otoTusBasla1, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",width=1,height=1,checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=2,column=2)

        tusHizValue = tk.StringVar(self)
        tusHizValue.set("Hızlı")
        tusHizValue1 = tk.StringVar(self)
        tusHizValue1.set("Hızlı")
        tusHizi = ["Çok Yavaş",
        "Yavaş",
        "Orta",
        "Hızlı",
        "Çok Hızlı",
        ]

        otoTusLabel4 = customtkinter.CTkLabel(self.otoTus,text="TUŞ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        otoTusLabel4.grid(row=0,column=0)
        otoTusLabel5 = customtkinter.CTkLabel(self.otoTus,text="HIZ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        otoTusLabel5.grid(row=0,column=1)

        otoTusButton4 = customtkinter.CTkOptionMenu(self.otoTus, values=tusHizi,width=self.optionMenuWidth,height=self.optionMenuHeight, variable=tusHizValue1, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666").grid(row=2,column=1)
        otoTusButton2 = customtkinter.CTkOptionMenu(self.otoTus, values=tusHizi,width=self.optionMenuWidth,height=self.optionMenuHeight, variable=tusHizValue, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666").grid(row=1,column=1)

        otoTusBasla2 = tk.IntVar(self)
        otoTusBasla2.set(0)
        otoTusButton3 = customtkinter.CTkCheckBox(self.otoTus,text="Dönerek Vur",variable=otoTusBasla2, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",width=4,height=4,checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=3 ,column=2)
        otoTusLabel3 = customtkinter.CTkLabel(self.otoTus,text="Deaktif",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        otoTusLabel3.grid(row=3,column=3)
    
    def pencereyiKapat(self):
        g=0
        self.quit()



def startBotWindow(hwnd,hwnd1,titleName):
    app = Window(hwnd,hwnd1,titleName)
    app.after(0, app.mainloop())
    