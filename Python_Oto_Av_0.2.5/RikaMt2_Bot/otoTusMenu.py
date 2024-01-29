import customtkinter
import tkinter as tk
import pyautogui
import threading
import time
from RikaMt2_Bot import Win32
import win32gui
import keyboard
import math
import operator
from RikaMt2_Bot import botWindow

def otoKey():
    if otoTusBasla.get() == 1:
        time.sleep(0.1)
        keyboard.press(f"{otoTusEntryValue1.get()}")
        for i in range(5):
            keyboard.press(f"{otoTusEntryValue.get()}")
            time.sleep(0.1)
            keyboard.release(f"{otoTusEntryValue.get()}")
            time.sleep(0.2)
        time.sleep(3)
    keyboard.release(f"{otoTusEntryValue1.get()}")


def otoTusBaslat():
    if otoTusCheckBox.get() == 1 and otoTusCheckBox.get() == 1:
        if otoTusBasla.get() == 1:
            for i in range(3,0,-1):
                bilgi.configure(text=f"Oto Tuş Başlıyor {i}")
                time.sleep(0.99)
            while otoTusBasla.get() == 1:
                try:
                    bilgi.configure(text="Oto Tuş Başladı")
                    oneGetir()
                    otoKey()
                    if otoTusBasla.get() == 1:
                        oneGetir1()
                        otoKey()
                    else:
                        bilgi.configure(text="Oto Tuş Durdu")
                        break
                        
                except MemoryError:
                    bilgi.configure(text="Bellek hatası: Bellek sızıntısı, yanlış bellek tahsisi veya bellek alanı taşması")
                    print("Bellek hatası: Bellek sızıntısı, yanlış bellek tahsisi veya bellek alanı taşması")
                    time.sleep(1)
                except Exception as e:
                    bilgi.configure(text=f"Hata: {e}")
                    print(f"Hata: {e}")
                    time.sleep(1)
        else:
            bilgi.configure(text="Oto Tuş Başladı")
        
    else:
        if otoTusBasla.get() == 1:
            try:
                while otoTusBasla.get() == 1:
                    oneGetir()
                    otoKey() 
                
            except:
                pass
        else:
            bilgi.configure(text="Oto Tuş Başladı")

def oneGetir():
    if hwnd1 != 0:
        win32gui.SetForegroundWindow(hwnd1)
    else:
        print(f"Hata {hwnd1}")

def oneGetir1():
    if hwnd2 != 0:
        win32gui.SetForegroundWindow(hwnd2)
    else:
        print(f"Hata {hwn2}")


def otoTusSetting():
    otoTusDurum.configure(text=f"Tuş : {otoTusEntryValue.get()}")
    otoTusDurum1.configure(text=f"Tuş : {otoTusEntryValue1.get()}")
    threading.Thread(target=otoTusBaslat).start()


def AllView(self,hwnd,hwnd3):
    global hwnd1
    global hwnd2
    global otoTusCheckBox
    global otoTusCheckBox1
    global otoTusBasla
    global bilgi
    global otoTusEntryValue
    global otoTusEntryValue1
    global otoTusDurum
    global otoTusDurum1
    
    # Label #
    
    bilgi = customtkinter.CTkLabel(self.otoTus, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi.grid(row=7,column=1)
    
    otoTusDurum = customtkinter.CTkLabel(self.otoTus, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoTusDurum.grid(row=3,column=2)
    
    otoTusDurum1 = customtkinter.CTkLabel(self.otoTus, text=" ",corner_radius=8,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoTusDurum1.grid(row=4,column=2)
    
    otoTusLabel4 = customtkinter.CTkLabel(self.otoTus,text="Pelerin Tuşu =",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoTusLabel4.grid(row=3,column=0)
    
    otoTusLabel5 = customtkinter.CTkLabel(self.otoTus,text="Attak Tuşu =",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoTusLabel5.grid(row=4, column=0)
    
    # spacer #
    customtkinter.CTkLabel(self.otoTus,text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight).grid(row=2,column=0)
    
    # CheckBox #
    otoTusBasla = tk.IntVar(self)
    otoTusBasla.set(0)
    otoTusCheckBox3 = customtkinter.CTkCheckBox(self.otoTus,text="Oto Tuşu Başlat",variable=otoTusBasla,command= otoTusSetting, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",width=1,height=1,checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=6,column=1)
    
    otoTusBasla2 = tk.IntVar(self)
    otoTusBasla2.set(0)
    otoTusButton3 = customtkinter.CTkCheckBox(self.otoTus,text="Dönerek Vur",variable=otoTusBasla2, onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",width=4,height=4,checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=5 ,column=2)
    
    # Entry #
    otoTusEntryValue = tk.StringVar(self)
    otoTusEntryValue.set("F4")
    otoTusEntry = customtkinter.CTkEntry(self.otoTus,textvariable=otoTusEntryValue,width=self.entryWidth,height=self.entryHeight,corner_radius=self.entryCornerRadius,text_color="#bababa").grid(row=3,column=1)


    otoTusEntryValue1 = tk.StringVar(self)
    otoTusEntryValue1.set("space")
    otoTusEntry1 = customtkinter.CTkEntry(self.otoTus,textvariable=otoTusEntryValue1,width=self.entryWidth,height=self.entryHeight,corner_radius=self.entryCornerRadius,text_color="#bababa").grid(row=4,column=1)

    
    # Hesaplar #
    otoTusCheckBox = customtkinter.CTkCheckBox(self.otoTus,text="1. Hesap",onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoTusCheckBox.grid(row=0,column=0)
    otoTusCheckBox1 = customtkinter.CTkCheckBox(self.otoTus,text="2. Hesap",onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoTusCheckBox1.grid(row=1,column=0)

    # Option Menu #
    """
    tusHizValue = tk.StringVar(self)
    tusHizValue.set("Hızlı")
    tusHizValue1 = tk.StringVar(self)
    tusHizValue1.set("Çok Hızlı")
    tusHizi = ["Çok Yavaş",
    "Yavaş",
    "Orta",
    "Hızlı",
    "Çok Hızlı",
    ]
    
    otoTusButton4 = customtkinter.CTkOptionMenu(self.otoTus, values=tusHizi,width=self.optionMenuWidth,height=self.optionMenuHeight, variable=tusHizValue1, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666").grid(row=3,column=1)
    otoTusButton2 = customtkinter.CTkOptionMenu(self.otoTus, values=tusHizi,width=self.optionMenuWidth,height=self.optionMenuHeight, variable=tusHizValue, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666").grid(row=2,column=1)
    """

    # Button #
    # Pencereyi Öne Çıkar # 
    button = customtkinter.CTkButton(self.otoTus, text="Öne Çıkar", command=oneGetir, width=30, height=20)
    button.grid(row=0,column=1)
    button1 = customtkinter.CTkButton(self.otoTus, text="Öne Çıkar", command=oneGetir1, width=30, height=20)
    button1.grid(row=1,column=1)

        
    if hwnd3 != 0:
        hwnd2 = hwnd3
        ZpyBotOpenCV = Win32.PyBotOpenCV(hwnd2)
        ZpyBotWin32 = Win32.PyBotWin32(hwnd2)
    else:
        hwnd2 = 0
        otoTusCheckBox1.configure(state="disabled")
        button1.configure(state="disabled")
    hwnd1 = hwnd
    pyBotOpenCV = Win32.PyBotOpenCV(hwnd1)
    pyBotWin32 = Win32.PyBotWin32(hwnd1)