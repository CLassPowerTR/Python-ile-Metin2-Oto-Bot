import customtkinter
import tkinter as tk
import pyautogui
import threading
import time
from AnkaMt2_Bot import Win32
import win32gui
import keyboard
import math
import operator
from AnkaMt2_Bot import botWindow


def oneGetir():
        if hwnd1 != 0:
            win32gui.SetForegroundWindow(hwnd1)
        else:
            print(f"Hata {hwnd1}")
            bilgi.configure(text=f"Hata: {hwnd1}",fg_color="red",text_color="black")

def oneGetir1():
        if hwnd2 != 0:
            win32gui.SetForegroundWindow(hwnd2)
        else:
            print(f"Hata {hwnd2}")
            bilgi.configure(text=f"Hata: {hwnd2}",fg_color="red",text_color="black")

def otoKey():
    if tusGet.get() == 1 or tusGet1.get() == 1:
        if tusGet.get() == 1:
            otoTusDurum.configure(text=f"Tuş : {otoTusEntryValue.get()}")
            keyboard.press(f"{otoTusEntryValue.get()}")
            time.sleep(0.02)
            keyboard.release(f"{otoTusEntryValue.get()}")
        if tusGet1.get() == 1:
            otoTusDurum1.configure(text=f"Tuş : {otoTusEntryValue1.get()}")
            keyboard.press(f"{otoTusEntryValue1.get()}")
            time.sleep(0.02)
            keyboard.release(f"{otoTusEntryValue1.get()}")
    elif tusGet.get() == 0 and tusGet1.get() == 0:
        otoTusBasla.set(0)


def otoTusBaslat():
    if otoTusBasla.get() == 1:
        if self1.hesap1.get() == 1 and self1.hesap2.get() == 1:
            for i in range(3,0,-1):
                bilgi.configure(text=f"Oto Tuş Başlıyor {i}",fg_color="transparent",text_color="white")
                time.sleep(0.99)
            bilgi.configure(text="Oto Tuş Başladı",fg_color="transparent",text_color="white")
            otoTusEntry.configure(state="disabled")
            otoTusEntry1.configure(state="disabled")
            while otoTusBasla.get() == 1:
                try:
                    oneGetir()
                    otoKey()
                    time.sleep(tusHizi[tusHizValue.get()])
                    if otoTusBasla.get() == 1:
                        oneGetir1()
                        otoKey()
                        time.sleep(tusHizi[tusHizValue1.get()])
                    else:
                        bilgi.configure(text="Oto Tuş Durdu",fg_color="transparent",text_color="white")
                        break
                        
                except MemoryError:
                    bilgi.configure(text="Bellek hatası: Bellek sızıntısı, yanlış bellek tahsisi veya bellek alanı taşması")
                    print("Bellek hatası: Bellek sızıntısı, yanlış bellek tahsisi veya bellek alanı taşması")
                    otoTusEntry.configure(state="normal")
                    otoTusEntry1.configure(state="normal")
                    time.sleep(1)
                except Exception as e:
                    bilgi.configure(text=f"Hata: {e}",fg_color="transparent",text_color="white")
                    print(f"Hata: {e}")
                    otoTusEntry.configure(state="normal")
                    otoTusEntry1.configure(state="normal")
                    time.sleep(1)
        
        elif self1.hesap1.get() == 1:
            if tusGet.get() == 1 or tusGet1.get() == 1:
                    otoTusEntry.configure(state="disabled")
                    otoTusEntry1.configure(state="disabled")
                    bilgi.configure(text="Oto Tuş Başladı", fg_color="transparent", text_color="white")
                    while otoTusBasla.get() == 1:
                        try:
                            oneGetir()
                            otoKey()
                            time.sleep(tusHizi[tusHizValue.get()])
                            if otoTusBasla.get() == 0:
                                bilgi.configure(text="Oto Tuş Durdu",fg_color="transparent",text_color="white")
                                otoTusEntry.configure(state="normal")
                                otoTusEntry1.configure(state="normal")
                                break
                        except Exception as e:
                            bilgi.configure(text=f"Hata: {e}",fg_color="transparent",text_color="white")
                            print(e)
            else:
                bilgi.configure(text="Oto Tuş Durdu",fg_color="transparent",text_color="white")
            if tusGet.get() == 0 and tusGet1.get() == 0:
                bilgi.configure(text="Herhangi Bir Tuş Seçin", fg_color="red", text_color="black")
                otoTusBasla.set(0)
        elif self1.hesap2.get() == 1:
            if tusGet.get() == 1 or tusGet1.get() == 1:
                bilgi.configure(text="Oto Tuş Başladı", fg_color="transparent", text_color="white")
                while otoTusBasla.get() == 1:
                        try:
                            oneGetir1()
                            otoKey()
                            time.sleep(tusHizi[tusHizValue1.get()])
                            if otoTusBasla.get() == 0:
                                bilgi.configure(text="Oto Tuş Durdu",fg_color="transparent",text_color="white")
                                otoTusEntry.configure(state="normal")
                                otoTusEntry1.configure(state="normal")
                                break
                        except Exception as e:
                            bilgi.configure(text=f"Hata: {e}",fg_color="transparent",text_color="white")
                            print(e)
                else:
                    bilgi.configure(text="Oto Tuş Durdu",fg_color="transparent",text_color="white")
            if tusGet.get() == 0 and tusGet1.get() == 0:
                bilgi.configure(text="Herhangi Bir Tuş Seçin", fg_color="red", text_color="black")
                otoTusBasla.set(0)
            
        elif self1.hesap1.get() == 0 and self1.hesap2.get() == 0:
            bilgi.configure(text="Herhangi Bir Hesap Seçin", fg_color="red", text_color="black")
            otoTusBasla.set(0)

    elif otoTusBasla.get() == 0:
        bilgi.configure(text="Oto Tuş Durdu",fg_color="transparent",text_color="white")
        otoTusEntry.configure(state="normal")
        otoTusEntry1.configure(state="normal")

def otoTusSetting():
    threading.Thread(target=otoTusBaslat).start()


def AllView(self,hwnd,hwnd3):
    global hwnd1, hwnd2
    global otoTusCheckBox, otoTusCheckBox1
    global otoTusBasla
    global bilgi
    global otoTusEntryValue, otoTusEntryValue1
    global otoTusDurum, otoTusDurum1
    global tusGet, tusGet1
    global tusHizValue, tusHizValue1
    global tusHizi
    global hesapKontrol1, hesapKontrol2
    global self1
    global otoTusEntry, otoTusEntry1
    
    self1 = self

    # Label #
    
    bilgi = customtkinter.CTkLabel(self.otoTus, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi.grid(row=7,columnspan=2,column=0)
    
    otoTusDurum = customtkinter.CTkLabel(self.otoTus, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoTusDurum.grid(row=7,column=2)
    
    otoTusDurum1 = customtkinter.CTkLabel(self.otoTus, text=" ",corner_radius=8,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoTusDurum1.grid(row=8,column=2)

    
    # spacer #
    customtkinter.CTkLabel(self.otoTus,text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight).grid(row=2,column=0)
    
    # CheckBox #
    tusGet = tk.IntVar(self)
    tusGet.set(1)
    customtkinter.CTkCheckBox(self.otoTus,text="1. Tuş =",variable=tusGet, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",width=1,height=1,checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=3,column=0, padx=(0,0), pady=(30,0))
    
    tusGet1 = tk.IntVar(self)
    tusGet1.set(1)
    customtkinter.CTkCheckBox(self.otoTus,text="2. Tuş =",variable=tusGet1, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",width=4,height=4,checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=4 ,column=0)
    
    
    otoTusBasla = tk.IntVar(self)
    otoTusBasla.set(0)
    otoTusCheckBox3 = customtkinter.CTkCheckBox(self.otoTus,text="Oto Tuşu Başlat",variable=otoTusBasla,command= otoTusSetting, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",width=1,height=1,checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=6,column=1)
    
    otoTusBasla2 = tk.IntVar(self)
    otoTusBasla2.set(0)
    otoTusButton3 = customtkinter.CTkCheckBox(self.otoTus,state="disabled",text="Dönerek Vur",variable=otoTusBasla2, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",width=4,height=4,checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=5 ,column=2)
    
    # Entry #
    otoTusEntryValue = tk.StringVar(self)
    otoTusEntryValue.set("F4")
    otoTusEntry = customtkinter.CTkEntry(self.otoTus,textvariable=otoTusEntryValue,width=self.entryWidth,height=self.entryHeight,corner_radius=self.entryCornerRadius,text_color="#bababa")
    otoTusEntry.grid(row=3,column=1, padx=(0,0), pady=(30,0))
    
    otoTusEntryValue1 = tk.StringVar(self)
    otoTusEntryValue1.set("space")
    otoTusEntry1 = customtkinter.CTkEntry(self.otoTus,textvariable=otoTusEntryValue1,width=self.entryWidth,height=self.entryHeight,corner_radius=self.entryCornerRadius,text_color="#bababa")
    otoTusEntry1.grid(row=4,column=1)

    

    # Option Menu #
    
    tusHizValue = tk.StringVar(self)
    tusHizValue.set("Çok Hızlı")
    tusHizValue1 = tk.StringVar(self)
    tusHizValue1.set("Çok Hızlı")
    tusHizi = {
    "Çok Yavaş": 3,
    "Yavaş": 2,
    "Orta": 1,
    "Hızlı": 0.5,
    "Çok Hızlı": 0.05,
    }
    tusHizi1 = [
    "Çok Yavaş",
    "Yavaş",
    "Orta",
    "Hızlı",
    "Çok Hızlı",
    ]
    
    
    tusHiziMenu = customtkinter.CTkOptionMenu(self.otoTus, values=tusHizi1,width=self.optionMenuWidth,height=self.optionMenuHeight, variable=tusHizValue, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666")
    tusHiziMenu.grid(row=3,column=2, padx=(0,0), pady=(30,0))
    tusHiziMenu1 = customtkinter.CTkOptionMenu(self.otoTus, values=tusHizi1,width=self.optionMenuWidth,height=self.optionMenuHeight, variable=tusHizValue1, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666")
    tusHiziMenu1.grid(row=4,column=2)
    

        
    if hwnd3 != 0:
        hwnd2 = hwnd3
        ZpyBotOpenCV = Win32.PyBotOpenCV(hwnd2)
        ZpyBotWin32 = Win32.PyBotWin32(hwnd2)
        self1.hesap1.set(1)
        self1.hesap2.set(1)
    else:
        hwnd2 = 0
        self1.hesap1.set(1)
    hwnd1 = hwnd
    pyBotOpenCV = Win32.PyBotOpenCV(hwnd1)
    pyBotWin32 = Win32.PyBotWin32(hwnd1)
    
    
    