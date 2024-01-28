import customtkinter
import tkinter as tk
import pyautogui
import threading
import time
from Phebia2_Bot import Win32
import keyboard
import win32gui, win32api, win32con

def kanalSec(kanalMatchValue,left, top):
    bilgi1.configure(text="Server Bulundu")
    server = pyBotOpenCV.locateCenterOnScreen(image=kanal,matchvalue=kanalMatchValue)
    if server != None:
        pyBotWin32.click_pg(server[0],server[1],left,top)
        del server
        time.sleep(1)
    elif server == None:
        del server
        kanalMatchValue = kanalMatchValue - 0.01
        return kanalSec(kanalMatchValue,pyBotOpenCV,pyBotWin32,left, top)

def hataAra(left, top):
    hata = pyBotOpenCV.locateCenterOnScreen(".\Phebia2_Bot\img\ok.PNG")
    if hata != None:
        bilgi1.configure(text="Giriş Yapılıyor")
        pyBotWin32.click_pg(hata[0],hata[1],left,top)
        del hata
        time.sleep(5)

def oyundaMi():
    Info = pyBotOpenCV.matchTemplateImage(image="./Phebia2_Bot\img/oyundaMi.PNG",matchvalue=0.91)
    if Info is None:
        del Info
        oyundaMi()
    else:
        win32gui.SetForegroundWindow(hwnd1)
        keyboard.press("F8")
        time.sleep(0.1)
        keyboard.release("F8")
        time.sleep(0.1)
def otomatikGiris():
        if oG.get() == 1:
            bilgi1.configure(text="Başladı")
            while oG.get() == 1:
                try:
                    giris = pyBotOpenCV.locateCenterOnScreen(".\Phebia2_Bot\img\giris.PNG")
                    if giris != None:
                        pyBotWin32.click_pg(kanal[0],kanal[1],left,top)
                        bilgi1.configure(text="Servere Giriliyor")
                        time.sleep(0.5)
                        pyBotWin32.click_pg(hesap[0],hesap[1],left,top)
                        time.sleep(5)
                        hata = pyBotOpenCV.locateCenterOnScreen(".\Phebia2_Bot\img\ok.PNG")
                        del giris
                        if hata != None:
                            pyBotWin32.click_pg(hata[0],hata[1],left,top)
                            del hata
                        del hata
                    karakter = pyBotOpenCV.locateCenterOnScreen(".\Phebia2_Bot\img\karakter.PNG")
                    if karakter != None:
                        pyBotWin32.click_pg(463,665,left,top)
                        del karakter
                        time.sleep(8)
                        oyundaMi()
                except Exception as e:
                    print(e)
                    time.sleep(10)
            if oG.get() == 0:
                    bilgi1.configure(text="Durdu")
                

    
def yenidenBasla():
    try:
        if yB.get() == 1:
            bilgi2.configure(text="Başladı")
            while yB.get() == 1:
                try:
                    yenidenBasla = pyBotOpenCV.locateCenterOnScreen(".\Phebia2_Bot\img\yenidenBasla.PNG")
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
    global hesap
    if ch.get() == "Kanal 1":
        kanal = [499,368]
    elif ch.get() == "Kanal 2":
        kanal = [554,368]
    elif ch.get() == "Kanal 3":
        kanal = [497,428]
    elif ch.get() == "Kanal 4":
        kanal = [553,426]
    elif ch.get() == "Kanal 5":
        kanal = [499,479]
    elif ch.get() == "Kanal 6":
        kanal = [552,475]
    
    if ac.get() == "Hesap 1":
        hesap = [622,366]
    elif ac.get() == "Hesap 2":
        hesap = [755,366]
    elif ac.get() == "Hesap 3":
        hesap = [622,400]
    elif ac.get() == "Hesap 4":
        hesap = [763,400]
    elif ac.get() == "Hesap 5":
        hesap = [621,443]
    elif ac.get() == "Hesap 6":
        hesap = [759,443]
     
    t1 = threading.Thread(target=otomatikGiris)
    t1.start()
def yBasla():
        t2 = threading.Thread(target=yenidenBasla)
        t2.start()

def AllView(self,hwnd,hwnd3):
    global ch
    global hwnd1
    global oG
    global yB
    global ac
    global otoGirisEntryValue
    global otoGirisEntryValue1
    global bilgi1
    global bilgi2
    global pyBotOpenCV
    global pyBotWin32
    global left, top, right, bottom
    hwnd1 = hwnd
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    pyBotOpenCV = Win32.PyBotOpenCV(hwnd1)
    pyBotWin32 = Win32.PyBotWin32(hwnd1)
    ch = tk.StringVar()
    ch.set("Kanal Seçiniz!")
    channels = [
    "Kanal 1",
    "Kanal 2",
    "Kanal 3",
    "Kanal 4",
    "Kanal 5",
    "Kanal 6",
    ]
    ac = tk.StringVar()
    ac.set("Hesap Seçiniz!")
    accounts = [
    "Hesap 1",
    "Hesap 2",
    "Hesap 3",
    "Hesap 4",
    "Hesap 5",
    "Hesap 6",
    ]
    otoGirisLabel = customtkinter.CTkOptionMenu(self.otoGiris, values=channels, variable=ch, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666",width=self.optionMenuWidth,height=self.optionMenuHeight)
    otoGirisLabel.place(relx=0.35, rely=0.1)
    otoGirisMenu = customtkinter.CTkOptionMenu(self.otoGiris, values=accounts, variable=ac, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666",width=self.optionMenuWidth,height=self.optionMenuHeight)
    otoGirisMenu.place(relx=0.35, rely=0.01)
    oG = tk.IntVar()
    oG.set(0)
    otoGirisButton = customtkinter.CTkCheckBox(self.otoGiris,checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth, text="Otomatik Giriş", variable=oG,command=otoGirisCommand, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa")
    otoGirisButton.place(relx=0.4, rely=0.2)
    otoGirisLabel2 = customtkinter.CTkLabel(self.otoGiris, text="Hesap :",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoGirisLabel2.place(relx=0.01, rely=0.01)
    chLabel = customtkinter.CTkLabel(self.otoGiris, text="Kanal : ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    chLabel.place(relx=0.01, rely=0.1)
    yB = tk.IntVar()
    yB.set(0)
    otoGirisButton = customtkinter.CTkCheckBox(self.otoGiris, text="Yeniden Başla", variable=yB, onvalue=1,command=yBasla, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoGirisButton.place(relx=0.05, rely=0.20)
    bilgi2 = customtkinter.CTkLabel(self.otoGiris, text="",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi2.place(relx=0.05, rely=0.3)
    bilgi1 = customtkinter.CTkLabel(self.otoGiris, text="",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi1.place(relx=0.3, rely=0.3)
    