import customtkinter
import tkinter as tk
import threading
import time
from RikaMt2_Bot import otoMetinMenu
from RikaMt2_Bot import otoMetinMenuAlternatif
from RikaMt2_Bot import otoGirisMenu
from RikaMt2_Bot import otoTusMenu


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
        self.after(1, otoTusMenu.AllView(self,self.hwnd,self.hwnd1))
    
    def pencereyiKapat(self):
        g=0
        self.quit()



def startBotWindow(hwnd,hwnd1,titleName):
    app = Window(hwnd,hwnd1,titleName)
    app.after(0, app.mainloop())
    