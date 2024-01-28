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
import gc

def saatBul():
    epoch = time.gmtime(time.time())
    saat = epoch.tm_hour+3
    dakika = epoch.tm_min
    saniye = epoch.tm_sec
    if saniye>=60:
        dakika = dakika +1
        saniye = saniye-60
    if dakika>=60:
        saat=saat+1
        dakika=dakika-60
    if saat>=24:
        saat=saat-24
    return saat,dakika,saniye

def get_window_size(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    del rect
    return (width, height)
   
def find_closest(coords, x, y):
    closest = None
    closest_distance = float('inf')
    for coord in coords:
        distance = math.sqrt((x - coord[0])**2 + (y - coord[1])**2)
        if distance < closest_distance:
            closest = coord
            closest_distance = distance
        del distance
    del closest_distance
    return closest

def metinAvla(metin,lastCoor):
    if f8.get() == 1:
        if lastCoor is None:
            closest_coord = find_closest(metin,middle[0]/2,middle[1]/2)
        else:
            closest_coord = find_closest(metin,lastCoor[0],lastCoor[1])
    else:
        closest_coord = find_closest(metin,middle[0]/2,middle[1]/2)
    bilgi.configure(text=f"Metin Bulundu")
    

    lastCoor = (closest_coord[0], closest_coord[1])
    
    x = closest_coord[0]
    y = closest_coord[1] + dagilimy+30
    
    if closest_coord[0] < 200: 
        x = x+10
    elif closest_coord[0] > 750: 
        x = x-10
    if closest_coord[1] < 280:
        y = y-30
    elif closest_coord[1] < 500:
        y = y-20
    elif y >665:
        y = 665
    
    pyBotWin32.click_pg(x,y,left,top)
    del closest_coord,metin,x,y
    time.sleep(0.2)
    return lastCoor
    
def metinAvla1(metin,lastCoor):
    if f8.get() == 1:
        if lastCoor is None:
            closest_coord = find_closest(metin,middle1[0]/2,middle1[1]/2)
        else:
            closest_coord = find_closest(metin,lastCoor[0],lastCoor[1])
    else:
        closest_coord = find_closest(metin,middle1[0]/2,middle1[1]/2)
    bilgi.configure(text=f"Metin Bulundu")
    

    lastCoor1 = (closest_coord[0], closest_coord[1])
    
    x = closest_coord[0]
    y = closest_coord[1] + dagilimy1+30
    
    if closest_coord[0] < 200: 
        x = x+10
    elif closest_coord[0] > 750: 
        x = x-10
    if closest_coord[1] < 280:
        y = y-30
    elif closest_coord[1] < 500:
        y = y-20
    elif y >665:
        y = 665
    
    ZpyBotWin32.click_pg(x,y,left1,top1)
    del closest_coord,metin,x,y
    time.sleep(0.2)
    return lastCoor

def uyariBul(lastCoor):
    uyari = pyBotOpenCV.AllLocateOnScreen(image="./RikaMt2_Bot/img/uyari.PNG",matchvalue=0.8)
    if uyari is not None:
        pyBotWin32.click_pg(uyari[0], uyari[1]+10, left, top)
        del uyari
    if uyari is None:
        metinBul(lastCoor)

def uyariBul1(lastCoor):
    uyari = ZpyBotOpenCV.AllLocateOnScreen(image="./RikaMt2_Bot/img/uyari.PNG",matchvalue=0.8)
    if uyari is not None:
        ZpyBotWin32.click_pg(uyari[0], uyari[1]+10, left1, top1)
        del uyari
    if uyari is None:
        metinBul1(lastCoor)

def metinBulundu(metin,lastCoor):
    bilgi.configure(text="Metin Bulundu")
    a = metinAvla(metin,lastCoor)
    lastCoor = a
    uyariBul(lastCoor)
    del a,metin
 
def metinBulundu1(metin,lastCoor):
    bilgi.configure(text="Metin Bulundu")
    a = metinAvla1(metin,lastCoor)
    lastCoor = a
    uyariBul1(lastCoor)
    del a,metin

def metinAra(lastCoor):
    bilgi.configure(text="Metin Aranıyor")
    metin = pyBotOpenCV.AllLocateOnScreen(image=secilenMetin,region=(0,0,1020,650),matchvalue=0.6)
    
    if metin is not None:
        metinBulundu(metin,lastCoor)        
    else:
        uyariBul(lastCoor)  
    
def metinAra1(lastCoor):
    bilgi.configure(text="Metin Aranıyor")
    metin = ZpyBotOpenCV.AllLocateOnScreen(image=secilenMetin1,region=(0,0,1020,650),matchvalue=0.6)
    if metin is not None:
        metinBulundu1(metin,lastCoor)        
    else:
        uyariBul1(lastCoor1)

def metinBul(lastCoor,lastCoor1):
    if l.get() == 1:
        if otoMetinLabel.get() == 1:
            Info = pyBotOpenCV.matchTemplateImage(image=secilenMetin,region=stoneInfoArea,matchvalue=0.91)
            if Info is None:
                del Info
                metinAra(lastCoor)
            else:
                if otoMetinLabel1.get() == 1:
                    metinBul1(lastCoor,lastCoor1)
                    del Info
                else:
                    bilgi.configure(text="Metin Kesiliyor") 
                time.sleep(0.1)
                del Info
        elif otoMetinLabel1.get() == 1:
            metinBul1(lastCoor,lastCoor1)
        
def metinBul1(lastCoor,lastCoor1):
    if l.get() == 1:
        Info = ZpyBotOpenCV.matchTemplateImage(image=secilenMetin1,region=stoneInfoArea1,matchvalue=0.91)
        print(Info)
        if Info is None:
            metinAra1(lastCoor1)
        else:
            if otoMetinLabel.get() == 1:
                metinBul(lastCoor,lastCoor1)
            else:
                bilgi.configure(text="Metin Kesiliyor")
            time.sleep(0.1)
            del Info

"""
if l.get() == 1 and biyolog.get() == 1:
                saat,dakika,saniye = saatBul()
                if biyologZamaniDakika == dakika:
                    if biyologZamaniSaat == saat:
                        if saniye - 1 < biyologZamaniSaniye < saniye+5:
                            biyologTeslim()
                bilgi7.configure(text=f"{saat}:{dakika}:{saniye}")
                del saat,dakika,saniye
                uyariBul(lastCoor)
            elif l.get() == 0 and biyolog.get() == 1:
                l.set(0)
                biyologZamanlayici()
"""
def metinKesPasif():
    lastCoor = 0
    lastCoor1 = 0
    if l.get() == 1:
        for i in range(3,0,-1):
            bilgi.configure(text=f"Metin Botu Başlıyor {i}")
            time.sleep(0.99)
            if l.get() == 0:
                break
        bilgi.configure(text="Metin Botu Başladı")

    
    while l.get() == 1:
        try:
            metinBul(lastCoor,lastCoor1)
            gc.collect()
        except MemoryError:
            bilgi.configure(text="Bellek hatası: Bellek sızıntısı, yanlış bellek tahsisi veya bellek alanı taşması")
            del lastCoor
            return
        except Exception as e:
            bilgi.configure(text=f"Hata: {e}")
            print(e)
            time.sleep(0.1)
    if l.get() == 0:
        l.set(0)
        bilgi.configure(text="Metin Botu Durdu")
    del lastCoor
    return


def biyologZamanlayici():
        while biyolog.get() == 1:
            try:
                saat,dakika,saniye = saatBul()
                if biyologZamaniDakika == dakika:
                    if biyologZamaniSaat == saat:
                        if saniye - 1 < biyologZamaniSaniye < saniye+7:
                            return False
                            time.sleep(0.1)
                            bilgi7.configure(text=f"{saat}:{dakika}:{saniye}")
                            del saat,dakika,saniye
                            biyologTeslim()
                        bilgi7.configure(text=f"{saat}:{dakika}:{saniye}")
                        del saat,dakika,saniye
                    bilgi7.configure(text=f"{saat}:{dakika}:{saniye}")
                    del saat,dakika,saniye
                else:
                    bilgi7.configure(text=f"{saat}:{dakika}:{saniye}")
                    del saat,dakika,saniye
                    time.sleep(0.1)
            except MemoryError:
                time.sleep(0.1)
                return
            except Exception as e:
                time.sleep(0.1)

def pencereyiKapat(zatenKapali):
    global biyologZamaniDakika
    global biyologZamaniSaniye
    global biyologZamaniSaat
    #kapat = pyautogui.locateCenterOnScreen("./img/cikis.PNG")
    kapat = pyBotOpenCV.locateCenterOnScreen(image="./RikaMt2_Bot/img/cikis.PNG",matchvalue=0.91)
    if kapat is not None:
        pyBotWin32.click_pg(kapat[0], kapat[1], left, top)
        time.sleep(1)
        del kapat
        #if zatenKapali == False:
            #l.set(1)
        saat, dakika,saniye = saatBul()
        biyologZamaniDakika = dakika + timeSleep
        biyologZamaniSaniye = saniye
        biyologZamaniSaat = saat
        if biyologZamaniDakika >=60:
            biyologZamaniDakika = biyologZamaniDakika - 60
            biyologZamaniSaat = saat + 1
        bilgi4.configure(text=f"{saat}:{dakika}:{saniye}")
        bilgi5.configure(text=f"{biyologZamaniSaat}:{biyologZamaniDakika}:{saniye}")
        bilgi7.configure(text=f"{saat}:{dakika}:{saniye}")
        del saat, dakika,saniye
        biyologZamanlayici()
    else:   
        time.sleep(0.1)
        pencereyiKapat(zatenKapali)

"""
        if l.get() == 1:
            time.sleep(0.1)
            metinKesPasif()
        else:
            time.sleep(0.1)
            biyologZamanlayici()
"""



def biyologTeslimEt(zatenKapali):
    #teslimEt = pyautogui.locateCenterOnScreen("./img/teslimEt.PNG")
    teslimEt = pyBotOpenCV.locateCenterOnScreen(image="./RikaMt2_Bot/img/teslimEt.PNG",matchvalue=0.91)
    if teslimEt is not None:
        pyBotWin32.click_pg(teslimEt[0], teslimEt[1], left, top)
        time.sleep(1)
        pencereyiKapat(zatenKapali)
        del teslimEt
    else:
        biyologTeslimEt(zatenKapali)
        time.sleep(1)

def biyologPenceresiniAc(zatenKapali):
    #biyologAc = pyautogui.locateCenterOnScreen("./img/biyolog.PNG",confidence=0.7)
    biyologAc = pyBotOpenCV.locateCenterOnScreen(image="./RikaMt2_Bot/img/biyolog.PNG",matchvalue=0.91)
    if biyologAc is not None:
        pyBotWin32.click_pg(biyologAc[0], biyologAc[1], left, top)
        time.sleep(1)
        del biyologAc
        biyologTeslimEt(zatenKapali)
    else:
        biyologPenceresiniAc(zatenKapali)
        time.sleep(1)

def biyologTeslim():
    if biyolog.get() == 1:
        for i in range(1,4):
            time.sleep(0.99)
            if biyolog.get() == 0:
                break
        while biyolog.get() == 1:
            try:
                zatenKapali = False
                biyologPenceresiniAc(zatenKapali) 
            except MemoryError:
                time.sleep(0.1)
                return
            except Exception as e:
                print(e)
                time.sleep(0.1)
   
"""
                if l.get() == 1:
                    zatenKapali = False
                    l.set(0)
                    biyologPenceresiniAc(zatenKapali)  
                if l.get() == 0:
                    zatenKapali = True
                    biyologPenceresiniAc(zatenKapali)  
"""
   
def otoMetinCommand():
    global secilenMetin
    global secilenMetin1
    global dagilimy
    global stoneInfoArea
    global dagilimy1
    global stoneInfoArea1
    global left, top, right, bottom
    global middle
    global left1, top1, right1, bottom1
    global middle1
    global hesap1,hesap2
    
    if l.get() == 1:
        hesap1 = False
        hesap2 = False
        hata = False
        
        if otoMetinLabel.get() == 1:
            left, top, right, bottom = win32gui.GetWindowRect(hwnd1)
            middle = get_window_size(hwnd1)
            
            if otoMetinButton4.get() == "Kıskançlık Metini":
                secilenMetin = "./RikaMt2_Bot/img/KiskanclikMetini.PNG"
                dagilimy = 50
                stoneInfoArea = (200,10,500,100)
            elif otoMetinButton4.get() == "Gölge Metini":
                secilenMetin = "./RikaMt2_Bot/img/GolgeMetini.PNG"
                dagilimy = 50
                stoneInfoArea = (200,10,500,100)
            elif otoMetinButton4.get() == "Dayanıklılık Metini":
                secilenMetin = "./RikaMt2_Bot/img/DayaniklilikMetini.PNG"
                dagilimy = 50
                stoneInfoArea = (200,10,500,100)
            elif otoMetinButton4.get() == "Katil Metini":
                secilenMetin = "./RikaMt2_Bot/img/KatilMetini.PNG"
                dagilimy = 50
                stoneInfoArea = (200,10,500,100)
            elif otoMetinButton4.get() == "Jeon-Un Metini":
                secilenMetin  = "./RikaMt2_Bot/img/Jeon-UnMetini.PNG"
                dagilimy = 50
                stoneInfoArea = (200,10,500,100)
            elif otoMetinButton4.get() == "Işıksızlık Metini":
                secilenMetin  = "./RikaMt2_Bot/img/isiksizlikMetini.PNG"
                dagilimy = 50
                stoneInfoArea = (200,10,500,100)
            elif otoMetinButton4.get() == "Namertlik Metini":
                secilenMetin  = "./RikaMt2_Bot/img/NamertlikMetini.PNG"
                dagilimy = 50
                stoneInfoArea = (200,10,500,100)
            else:
                hesap1 = True
                l.set(0)
        
        if otoMetinLabel1.get() == 1:
            left1, top1, right1, bottom1 = win32gui.GetWindowRect(hwnd2)
            middle1 = get_window_size(hwnd2)
            
            if hwnd2 != 0:
                if metinValue.get() == "Kıskançlık Metini":
                    secilenMetin1 = "./RikaMt2_Bot/img/KiskanclikMetini.PNG"
                    dagilimy1 = 50
                    stoneInfoArea1 = (200,10,500,100)
                elif metinValue.get() == "Gölge Metini":
                    secilenMetin1 = "./RikaMt2_Bot/img/GolgeMetini.PNG"
                    dagilimy1 = 50
                    stoneInfoArea1 = (200,10,500,100)
                elif metinValue.get() == "Dayanıklılık Metini":
                    secilenMetin1 = "./RikaMt2_Bot/img/DayaniklilikMetini.PNG"
                    dagilimy1 = 50
                    stoneInfoArea1 = (200,10,500,100)
                elif metinValue.get() == "Katil Metini":
                    secilenMetin1 = "./RikaMt2_Bot/img/KatilMetini.PNG"
                    dagilimy1 = 50
                    stoneInfoArea1 = (200,10,500,100)
                elif metinValue.get() == "Jeon-Un Metini":
                    secilenMetin1  = "./RikaMt2_Bot/img/Jeon-UnMetini.PNG"
                    dagilimy1 = 50
                    stoneInfoArea1 = (200,10,500,100)
                elif metinValue.get() == "Işıksızlık Metini":
                    secilenMetin1  = "./RikaMt2_Bot/img/isiksizlikMetini.PNG"
                    dagilimy1 = 50
                    stoneInfoArea1 = (200,10,500,100)
                elif metinValue.get() == "Namertlik Metini":
                    secilenMetin1  = "./RikaMt2_Bot/img/NamertlikMetini.PNG"
                    dagilimy1 = 50
                    stoneInfoArea1 = (200,10,500,100)
                else:
                    hesap2 = True
                    l.set(0)
            elif hwnd2 ==0:
                hesap2 = True
                hata = True
                l.set(0)
                bilgi.configure(text="2. Hesap Penceresi Belirtilmemiş!")
        if otoMetinLabel.get() == 1 and otoMetinLabel1.get() == 1:
            if hesap1 == True or hesap2 == True:
                bilgi.configure(text="Lütfen Metin Belirtiniz!")
            if hata == True:
                bilgi.configure(text="2. Hesap Penceresi Belirtilmemiş!")
            else:
                threading.Thread(target=metinKesPasif).start()
        elif otoMetinLabel.get() == 1 and otoMetinLabel1.get() == 0:
            if hesap1 == True:
                bilgi.configure(text="Lütfen Metin Belirtiniz!")
            else:
                threading.Thread(target=metinKesPasif).start()
        elif otoMetinLabel.get() == 0 and otoMetinLabel1.get() == 1:
            if hesap2 == True:
                bilgi.configure(text="Lütfen Metin Belirtiniz!")
            if hata == True:
                bilgi.configure(text="2. Hesap Penceresi Belirtilmemiş!")
            else:
                threading.Thread(target=metinKesPasif).start()
        elif otoMetinLabel.get() == 0 and otoMetinLabel1.get() == 0:
            l.set(0)
            bilgi.configure(text="Lütfen Metin veya Hesap Belirtiniz!")

def otoBiyologBaslat():
    global timeSleep
    
    timeSleep = otoMetinEntry1.get()
    timeSleep = int(timeSleep)
    
    threading.Thread(target=biyologTeslim).start()

def oneGetir():
    win32gui.SetForegroundWindow(hwnd1)

def oneGetir1():
    win32gui.SetForegroundWindow(hwnd2)

def AllView(self,hwnd,hwnd3):
    global otoMetinButton
    global otoMetinButton2
    global otoMetinLabel
    global otoMetinLabel1
    global otoMetinButton4
    global metinValue
    global otoMetinEntryValue
    global bilgi
    global hwnd1
    global hwnd2
    global pyBotWin32
    global pyBotOpenCV
    global ZpyBotWin32
    global ZpyBotOpenCV
    global middle
    global l
    global f8
    global otoMetinEntry1
    global biyolog
    global bilgi4
    global bilgi5
    global bilgi7
    
    
    if hwnd3 != 0:
        hwnd2 = hwnd3
        ZpyBotOpenCV = Win32.PyBotOpenCV(hwnd2)
        ZpyBotWin32 = Win32.PyBotWin32(hwnd2)
    else:
        hwnd2 = 0
    hwnd1 = hwnd
    pyBotOpenCV = Win32.PyBotOpenCV(hwnd1)
    pyBotWin32 = Win32.PyBotWin32(hwnd1)
    metinValue = tk.StringVar(self)
    metinValue.set("Metini Seçiniz!")
    metinler = ["Kıskançlık Metini",
    "Gölge Metini",
    "Dayanıklılık Metini",
    "Katil Metini",
    "Jeon-Un Metini",
    "Işıksızlık Metini",
    "Namertlik Metini",
    ]
    
    otoMetinButton4 = customtkinter.CTkOptionMenu(self.otoMetin,width=self.optionMenuWidth,height=self.optionMenuHeight, values=metinler, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666")
    otoMetinButton4.place(relx=0.35, rely=0.01)
    otoMetinButton4.set("Metini Seçiniz!")
    otoMetinLabel = customtkinter.CTkCheckBox(self.otoMetin,text="1. Hesap",onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinLabel.place(relx=0.01, rely=0.01)

    l = tk.IntVar()
    l.set(0)
    otoMetinButton = customtkinter.CTkCheckBox(self.otoMetin,text="Başlat/Durdur",variable=l, command= otoMetinCommand,onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinButton.place(relx=0.3, rely=0.25)
    otoMetinLabel1 = customtkinter.CTkCheckBox(self.otoMetin,text="2. Hesap",onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinLabel1.place(relx=0.01, rely=0.1)
    otoMetinButton1 = customtkinter.CTkOptionMenu(self.otoMetin,width=self.optionMenuWidth,height=self.optionMenuHeight, values=metinler,variable=metinValue, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666")
    otoMetinButton1.place(relx=0.35, rely=0.1)
    bilgi = customtkinter.CTkLabel(self.otoMetin, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi.place(relx=0.3, rely=0.18)
    f8 = tk.IntVar()
    f8.set(0)
    otoMetinButton2 = customtkinter.CTkCheckBox(self.otoMetin,text="F8 İle Farm",variable=f8,onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinButton2.place(relx=0.01, rely=0.18)
    biyolog = tk.IntVar()
    biyolog.set(0)
    otoMetinButton3 = customtkinter.CTkCheckBox(self.otoMetin,text="Biyolog Teslim",command=otoBiyologBaslat,variable=biyolog,onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinButton3.place(relx=0.01, rely=0.33)
    otoMetinEntry1 = customtkinter.CTkEntry(self.otoMetin,placeholder_text="Dakika Giriniz!",corner_radius=self.entryCornerRadius,text_color="#bababa",height=self.entryHeight)
    otoMetinEntry1.place(relx=0.40, rely=0.34)
    bilgi2 = customtkinter.CTkLabel(self.otoMetin, text="Biyolog Verilen Saat :",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi2.place(relx=0.01, rely=0.43)
    bilgi3 = customtkinter.CTkLabel(self.otoMetin, text="Biyolog Verilecek Saat :",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi3.place(relx=0.01, rely=0.49)
    bilgi4 = customtkinter.CTkLabel(self.otoMetin, text="00.00.00",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi4.place(relx=0.42, rely=0.43)
    bilgi5 = customtkinter.CTkLabel(self.otoMetin, text="00.00.00",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi5.place(relx=0.42, rely=0.49)
    bilgi6 = customtkinter.CTkLabel(self.otoMetin, text="Şuanki Saat :",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi6.place(relx=0.01, rely=0.55)
    bilgi7 = customtkinter.CTkLabel(self.otoMetin, text="00.00.00",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi7.place(relx=0.42, rely=0.55)
    button = customtkinter.CTkButton(self.otoMetin, text="Öne Çıkar", command=oneGetir, width=30, height=20)
    button.place(relx=0.7, rely=0.01)
    button1 = customtkinter.CTkButton(self.otoMetin, text="Öne Çıkar", command=oneGetir1, width=30, height=20)
    button1.place(relx=0.7, rely=0.1)

