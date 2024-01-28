import customtkinter
import tkinter as tk
import pyautogui
import threading
import time
from AnkaMt2_Bot import Win32
import keyboard
import win32gui, win32api, win32con

def kanalSec(kanalMatchValue,left, top):
    bilgi1.configure(text="Server Bulundu")
    server = pyBotOpenCV.locateCenterOnScreen(image=kanal,matchvalue=kanalMatchValue)
    if server != None:
        pyBotWin32.click_pg(server[0],server[1],left,top)
        time.sleep(1)
    elif server == None:
        kanalMatchValue = kanalMatchValue - 0.01
        return kanalSec(kanalMatchValue,pyBotOpenCV,pyBotWin32,left, top)

def hataAra(left, top):
    hata = pyBotOpenCV.locateCenterOnScreen("./AnkaMt2_Bot/img/ok.PNG")
    if hata != None:
        bilgi1.configure(text="Giriş Yapılıyor")
        pyBotWin32.click_pg(hata[0],hata[1],left,top)
        time.sleep(5)

def otomatikGiris():
    try:
        if oG.get() == 1:
            kAdi = otoGirisEntryValue.get()
            sifre = otoGirisEntryValue1.get()
            bilgi1.configure(text="Başladı")
            kanalMatchValue = 0.99
            baslaMatchValue = 0.6
            while oG.get() == 1:
                try:
                    server = pyBotOpenCV.locateCenterOnScreen("./AnkaMt2_Bot/img/server.PNG",matchvalue=0.6)
                    if server != None:
                        kanalSec(kanalMatchValue,pyBotOpenCV,pyBotWin32,left, top)
                        
                    giris = pyBotOpenCV.locateCenterOnScreen("./AnkaMt2_Bot/img/giris.PNG")
                    if giris != None:
                        bilgi1.configure(text="Servere Giriliyor")
                        pyBotWin32.click_pg(giris[0],giris[1],left,top)
                        time.sleep(5)
                        hataAra(pyBotOpenCV,pyBotWin32,left, top)
                        
                    hesap = pyBotOpenCV.locateCenterOnScreen("./AnkaMt2_Bot/img/hesap.PNG")
                    if hesap != None:
                        bilgi1.configure(text="K.Adi Giriliyor")
                        pyBotWin32.writeWord(kAdi)
                        pyBotWin32.press_Enter()
                        time.sleep(0.5)
                        bilgi1.configure(text="Şifre Giriliyor")
                        pyBotWin32.writeWord(sifre)
                        bilgi1.configure(text="Hesaba Giriliyor")
                        pyBotWin32.press_Enter()
                        time.sleep(10)
                        pyBotWin32.click_pg(185,516+20,left,top)
                    time.sleep(3)
                except:
                    time.sleep(3)
            if oG.get() == 0:
                    bilgi1.configure(text="Durdu")
    except:
        time.sleep(3)
                
def ataBin():
    hwnd2 = win32gui.GetForegroundWindow()
    win32gui.SetForegroundWindow(hwnd1)
    atTusu = yBentryValue.get()
    keyboard.press(atTusu)
    time.sleep(0.1)
    keyboard.release(atTusu)
    time.sleep(2)
    keyboard.press("ctrl")
    keyboard.press("h")
    time.sleep(0.1)
    keyboard.release("ctrl")
    keyboard.release("h")
    win32gui.SetForegroundWindow(hwnd2)

def binegeBin():
    hwnd2 = win32gui.GetForegroundWindow()
    win32gui.SetForegroundWindow(hwnd1)
    binekTus = yBentryValue1.get()
    keyboard.press(binekTus)
    time.sleep(0.1)
    keyboard.release(binekTus)
    win32gui.SetForegroundWindow(hwnd2)
    
def yenidenBasla():
    try:
        if yB.get() == 1:
            bilgi2.configure(text="Başladı")
            while yB.get() == 1:
                try:
                    yenidenBasla = pyBotOpenCV.locateCenterOnScreen("./AnkaMt2_Bot/img/yenidenBasla.PNG")
                    if yenidenBasla != None:
                        bilgi2.configure(text="Yeniden Başlanıyor")
                        time.sleep(10)
                        pyBotWin32.click_pg(yenidenBasla[0],yenidenBasla[1]-25,left,top)
                        if aT.get() ==1:
                            ataBin()
                        elif binek.get(1):
                            binegeBin()
                            
                        time.sleep(2)
                    else:
                        time.sleep(3)
                except:
                    time.sleep(3)
            if yB.get() == 0:
                bilgi2.configure(text="Durdu")
    except:
        time.sleep(3)
def otoGirisCommand():
    global kanal
    if ch.get() == "Kanal 1":
        kanal = "./AnkaMt2_Bot/img/Kanal1.PNG"
    elif ch.get() == "Kanal 2":
        kanal = "./AnkaMt2_Bot/img/Kanal2.PNG"
    elif ch.get() == "Kanal 3":
        kanal = "./AnkaMt2_Bot/img/Kanal3.PNG"
    elif ch.get() == "Kanal 4":
        kanal = "./AnkaMt2_Bot/img/Kanal4.PNG"
    elif ch.get() == "Kanal 5":
        kanal = "./AnkaMt2_Bot/img/Kanal5.PNG"
    elif ch.get() == "Kanal 6":
        kanal = "./AnkaMt2_Bot/img/Kanal6.PNG"
    t1 = threading.Thread(target=otomatikGiris)
    t1.start()
def yBasla():
        t2 = threading.Thread(target=yenidenBasla)
        t2.start()

def AllView(self,hwnd,hwnd3):
    global ch
    global oG
    global yB
    global otoGirisEntryValue
    global otoGirisEntryValue1
    global bilgi1
    global bilgi2
    global aT
    global binek
    global yBentryValue
    global yBentryValue1
    global pyBotOpenCV
    global pyBotWin32
    global ZpyBotOpenCV
    global ZpyBotWin32
    global pyBotWin32
    global left, top, right, bottom
    global hwnd1
    global hwnd2
    
    
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    
    if hwnd3 != 0:
        hwnd2 = hwnd3
        ZpyBotOpenCV = Win32.PyBotOpenCV(hwnd2)
        ZpyBotWin32 = Win32.PyBotWin32(hwnd2)
        left1, top1, right1, bottom1 = win32gui.GetWindowRect(hwnd3)
    else:
        hwnd2 = 0
    hwnd1 = hwnd
    pyBotOpenCV = Win32.PyBotOpenCV(hwnd1)
    pyBotWin32 = Win32.PyBotWin32(hwnd1)
    
    
    
    
    ch = tk.StringVar()
    ch.set("Kanal 1")
    channels = [
    "Kanal 1",
    "Kanal 2",
    "Kanal 3",
    "Kanal 4",
    "Kanal 5",
    "Kanal 6",
    ]
    otoGirisLabel = customtkinter.CTkOptionMenu(self.otoGiris, values=channels, variable=ch, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666",width=self.optionMenuWidth,height=self.optionMenuHeight).grid(row=2,column=1)
    oG = tk.IntVar()
    oG.set(0)
    otoGirisButton = customtkinter.CTkCheckBox(self.otoGiris,checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth, text="Otomatik Giriş", variable=oG,command=otoGirisCommand, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa").grid(row=3,column=1)
    otoGirisEntryValue = tk.StringVar()
    otoGirisEntryValue1 = tk.StringVar()
    otoGirisEntry = customtkinter.CTkEntry(self.otoGiris,placeholder_text="Kullanıcı Adı",textvariable = otoGirisEntryValue, corner_radius=self.entryCornerRadius,text_color="#bababa",width=150,height=self.entryHeight).grid(row=0, column=1, padx=(0,0), pady=(50,0))
    otoGirisEntry1 = customtkinter.CTkEntry(self.otoGiris,placeholder_text="Şifre",textvariable = otoGirisEntryValue1, corner_radius=self.entryCornerRadius,text_color="#bababa",show="*",width=150,height=self.entryHeight).grid(row=1,column=1, padx=(0,0), pady=(0,0))
    otoGirisLabel1 = customtkinter.CTkLabel(self.otoGiris, text="Kullanıcı Adı =",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight).grid(row=0,column=0, padx=(0,0), pady=(50,0))
    otoGirisLabel2 = customtkinter.CTkLabel(self.otoGiris, text="Şifre =",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight).grid(row=1,column=0, padx=(0,0), pady=(0,0))
    chLabel = customtkinter.CTkLabel(self.otoGiris, text="Kanal : ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight).grid(row=2,column=0, padx=(0,0), pady=(0,0))
    yB = tk.IntVar()
    yB.set(0)
    otoGirisButton = customtkinter.CTkCheckBox(self.otoGiris, text="Yeniden Başla", variable=yB, onvalue=1,command=yBasla, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth).grid(row=3,column=0, padx=(0,0), pady=(0,0))
    bilgi2 = customtkinter.CTkLabel(self.otoGiris, text="",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi2.grid(row=6,column=0, padx=(0,0), pady=(0,0))
    bilgi1 = customtkinter.CTkLabel(self.otoGiris, text="",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi1.grid(row=6,column=1, padx=(0,0), pady=(0,0))
    aT = tk.IntVar()
    aT.set(0)
    yBbutton = customtkinter.CTkCheckBox(self.otoGiris, text="At ile", variable=aT, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth).grid(row=4,column=0, padx=(0,0), pady=(0,0))
    binek = tk.IntVar()
    binek.set(0)
    yBentryValue = tk.StringVar()
    yBentryValue1 = tk.StringVar()
    yBbutton1 = customtkinter.CTkCheckBox(self.otoGiris, text="Binek Mührü", variable=binek, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth).grid(row=4,column=1, padx=(0,0), pady=(0,0))
    yBentry = customtkinter.CTkEntry(self.otoGiris,textvariable=yBentryValue,placeholder_text="At Tuşu", corner_radius=self.entryCornerRadius,text_color="#bababa",width=120,height=self.entryHeight).grid(row=5,column=0, padx=(0,0), pady=(0,0))
    yBentry1 = customtkinter.CTkEntry(self.otoGiris,textvariable=yBentryValue1, placeholder_text="Binek Tuşu", corner_radius=self.entryCornerRadius,text_color="#bababa",width=120,height=self.entryHeight).grid(row=5,column=1, padx=(0,0), pady=(0,0))