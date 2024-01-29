import customtkinter
import tkinter as tk
import pyautogui
import threading
import time
from RikaMt2_Bot import Win32
#from Win32 import PyBotOpenCV
#from Win32 import PyBotWin32
import win32gui
import keyboard
import math
import operator
from RikaMt2_Bot import botWindow
#from Win32 import botWindow
   
def get_window_size():
    rect = win32gui.GetWindowRect(hwnd1)
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    return (width, height)
   
def find_closest(coords, x, y):
    closest = None
    closest_distance = float('inf')
    for coord in coords:
        distance = math.sqrt((x - coord[0])**2 + (y - coord[1])**2)
        if distance < closest_distance:
            closest = coord
            closest_distance = distance
    return closest

def metinAvla(metin):
    closest_coord = find_closest(metin,middle[0]/2,middle[1]/2)
    bilgi.configure(text=f"Metin {closest_coord[0]},{closest_coord[1]}'de Bulundu")
    if closest_coord[0] < 200 and closest_coord[1] <200:
        pyBotWin32.click_pg(closest_coord[0],closest_coord[1],left,top) #closest_coord[0]+20
    elif closest_coord[0] > 750 and closest_coord[1] <200:
        pyBotWin32.click_pg(closest_coord[0],closest_coord[1],left,top)
    elif closest_coord[0] < 200:
        pyBotWin32.click_pg(closest_coord[0],closest_coord[1],left,top) #closest_coord[0]+20
    elif closest_coord[0] > 750:
        pyBotWin32.click_pg(closest_coord[0],closest_coord[1],left,top)
    elif closest_coord[1] < 200:
        pyBotWin32.click_pg(closest_coord[0],closest_coord[1],left,top) #closest_coord[0]+10
    else:
        pyBotWin32.click_pg(closest_coord[0],closest_coord[1],left,top) #closest_coord[0]+10
    bilgi.configure(text="Metin Kesildi")
    
def metinKesPasif():
    middle = get_window_size()
    try:
        if l.get() == 1:
            bilgi.configure(text="Metin Botu Başladı")
            while l.get() == 1:
                try:
                    bilgi.configure(text="Metin Aranıyor")
                    metin = pyautogui.locateAllOnScreen(secilenMetin,region=(0,67,1020,600),confidence=0.6)
                    if metin != None:
                        bilgi.configure(text="Metin Bulundu")
                        metinAvla(metin)
                        time.sleep(coolDown)
                    elif metin == None:
                        metin = pyBotOpenCV.AllLocateOnScreen(image=secilenMetin2,region=(0,67,1020,600),matchvalue=confidence)
                        if metin != None:
                            bilgi.configure(text="Metin Bulundu")
                            metinAvla(metin)
                            time.sleep(coolDown)
                        elif metin == None:
                            metin = pyBotOpenCV.AllLocateOnScreen(image=secilenMetin3,region=(0,67,1020,600),matchvalue=confidence)
                            if metin != None:
                                bilgi.configure(text="Metin Bulundu")
                                metinAvla(metin)
                                time.sleep(coolDown)
                            elif metin == None:
                                metin = pyBotOpenCV.AllLocateOnScreen(image=secilenMetin4,region=(0,67,1020,600),matchvalue=confidence)
                                if metin != None:
                                    bilgi.configure(text="Metin Bulundu")
                                    metinAvla(metin)
                                    time.sleep(coolDown)
                                elif metin == None:
                                    pass
                except:
                    time.sleep(3)
            if l.get() == 0:
                bilgi.configure(text="Metin Botu Durdu")
    except:
        time.sleep(3) 

   
def otoMetinCommand():
    global is_running
    global coolDown
    global secilenMetin
    global secilenMetin2
    global secilenMetin3
    global secilenMetin4
    global confidence
    global dagilimx
    global dagilimy
    
    if metinValue.get() == "Kıskançlık Metini":
        secilenMetin = "./img/KiskanclikMetini.PNG"
        secilenMetin2 = "./img/KiskanclikMetini2.PNG"
        secilenMetin3 = "./img/KiskanclikMetini3.PNG"
        secilenMetin4 = "./img/KiskanclikMetini4.PNG"
        dagilimx = 0
        dagilimy = +50
        confidence= 0.7
        
    elif metinValue.get() == "Kurak Çöl Metini":
        secilenMetin = "./img/KurakColMetini.PNG"
        secilenMetin2 = "./img/KurakColMetini.PNG"
        secilenMetin3 = "./img/KurakColMetini.PNG"
        secilenMetin4 = "./img/KurakColMetini.PNG"
        dagilimx = 0
        dagilimy = +50
    elif metinValue.get() == "Orman Metini":
        secilenMetin = "./img/OrmanMetini.PNG"
        secilenMetin2 = "./img/OrmanMetini2.PNG"
        secilenMetin3 = "./img/OrmanMetini3.PNG"
        secilenMetin4 = "./img/OrmanMetini4.PNG"
        dagilimx = 0
        dagilimy = +50
    elif metinValue.get() == "Buzul Vadi Metini":
        secilenMetin = "./img/BuzulVadiMetini.PNG"
        secilenMetin2 = "./img/BuzulVadiMetini2.PNG"
        secilenMetin3 = "./img/BuzulVadiMetini3.PNG"
        secilenMetin4 = "./img/BuzulVadiMetini4.PNG"
        dagilimx = 0
        dagilimy = +50
    elif metinValue.get() == "Ayaz Metini":
        secilenMetin = "./img/AyazMetini.PNG"
        secilenMetin2 = "./img/AyazMetini2.PNG"
        secilenMetin3 = "./img/AyazMetini3.PNG"
        secilenMetin4 = "./img/AyazMetini4.PNG"
        dagilimx = 0
        dagilimy = +50


    coolDown = otoMetinEntryValue.get()
    coolDown = float(coolDown)
    threading.Thread(target=metinKesPasif).start()

def AllView(self,hwnd):
    global otoMetinButton
    global otoMetinButton2
    global metinValue
    global otoMetinEntryValue
    global bilgi
    global hwnd1
    global pyBotOpenCV
    global pyBotWin32
    global middle
    global left, top, right, bottom
    global l
    
    hwnd1 = hwnd
    left, top, right, bottom = win32gui.GetWindowRect(hwnd1)
    middle = get_window_size()
    pyBotOpenCV = PyBotOpenCV(hwnd1)
    pyBotWin32 = PyBotWin32(hwnd1)
    metinValue = tk.StringVar(self)
    metinValue.set("Metini Seçiniz")
    metinler = ["Kıskançlık Metini",
    "Kurak Çöl Metini",
    "Orman Metini",
    "Buzul Vadi Metini",
    "Ayaz Metini",
    ]
    otoMetinEntryValue = tk.StringVar(value="0.0")
    otoMetinEntry = customtkinter.CTkEntry(self.otoMetin,textvariable=otoMetinEntryValue,corner_radius=self.entryCornerRadius,text_color="#bababa",width=self.entryWidth,height=self.entryHeight)
    otoMetinEntry.place(relx=0.45, rely=0.01)
    otoMetinLabel = customtkinter.CTkLabel(self.otoMetin, text="Bekleme Süresi =",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoMetinLabel.place(relx=0.01, rely=0.01)

    l = tk.IntVar()
    l.set(0)
    otoMetinButton = customtkinter.CTkCheckBox(self.otoMetin,text="Başlat/Durdur",variable=l, command= otoMetinCommand,onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinButton.place(relx=0.3, rely=0.25)
    otoMetinLabel1 = customtkinter.CTkLabel(self.otoMetin, text="Kesilecek Metin =",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoMetinLabel1.place(relx=0.01, rely=0.1)
    otoMetinButton1 = customtkinter.CTkOptionMenu(self.otoMetin,width=self.optionMenuWidth,height=self.optionMenuHeight, values=metinler,variable=metinValue, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666")
    otoMetinButton1.place(relx=0.35, rely=0.1)
    bilgi = customtkinter.CTkLabel(self.otoMetin, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi.place(relx=0.3, rely=0.18)