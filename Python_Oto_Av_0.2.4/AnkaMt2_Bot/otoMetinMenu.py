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
import gc
from datetime import datetime, timezone, timedelta
   
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
    if lastCoor is None:
        closest_coord = find_closest(metin,middle[0]/2,middle[1]/2)
    else:
        if isinstance(lastCoor, tuple) and len(lastCoor) == 2:
            closest_coord = find_closest(metin, lastCoor[0], lastCoor[1])
        else:
            print(f"lastCoor: {lastCoor}")
            closest_coord = find_closest(metin, lastCoor[0], lastCoor[1])
            print("Hata: lastCoor uygun bir tuple değil.")
    

    lastCoor = (closest_coord[0], closest_coord[1])
    
    
    x = closest_coord[0] + 180
    y = closest_coord[1] + dagilimy+60
    
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
    
def metinAvla1(metin,lastCoor,lastCoor1):
    if lastCoor is None:
        closest_coord = find_closest(metin,middle1[0]/2,middle1[1]/2)
    else:
        closest_coord = find_closest(metin,lastCoor[0],lastCoor[1])

    

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
        y = y-20
    
    ZpyBotWin32.click_pg(x,y,left1,top1)
    del closest_coord,metin,x,y
    time.sleep(0.2)
    return lastCoor

def uyariBul(lastCoor,lastCoor1):
    uyari = pyBotOpenCV.AllLocateOnScreen(image="./AnkaMt2_Bot/img/ok.PNG",matchvalue=0.8)
    if uyari is not None:
        pyBotWin32.click_pg(uyari[0], uyari[1]+10, left, top)
        del uyari
    if uyari is None:
        metinBul(lastCoor,lastCoor1)

def uyariBul1(lastCoor):
    uyari = ZpyBotOpenCV.AllLocateOnScreen(image="./AnkaMt2_Bot/img/ok.PNG",matchvalue=0.8)
    if uyari is not None:
        ZpyBotWin32.click_pg(uyari[0], uyari[1]+10, left1, top1)
        del uyari
    if uyari is None:
        metinBul1(lastCoor)

def metinBulundu(metin,lastCoor,lastCoor1):
    bilgi.configure(text="Metin Bulundu")
    a = metinAvla(metin,lastCoor)
    lastCoor = a
    uyariBul(lastCoor,lastCoor1)
    del a,metin
 
def metinBulundu1(metin,lastCoor,lastCoor1):
    bilgi.configure(text="Metin Bulundu")
    a = metinAvla1(metin,lastCoor)
    lastCoor = a
    uyariBul1(lastCoor)
    del a,metin

def metinAra(lastCoor,lastCoor1):
    bilgi.configure(text="Metin Aranıyor")
    metin = pyBotOpenCV.AllLocateOnScreen(image=secilenMetin,region=(30,30,int(middle[0]*0.95),int(middle[1]*0.95)),matchvalue=0.8)
    if metin is not None:
        metinBulundu(metin,lastCoor,lastCoor1)        
    else:
        uyariBul(lastCoor,lastCoor1)  
    
def metinAra1(lastCoor,lastCoor1):
    bilgi.configure(text="Metin Aranıyor")
    metin = ZpyBotOpenCV.AllLocateOnScreen(image=secilenMetin1,region=(30,30,int(middle[0]*0.95),int(middle[1]*0.95)),matchvalue=0.8)
    if metin is not None:
        metinBulundu1(metin,lastCoor,lastCoor1)        
    else:
        uyariBul1(lastCoor1,lastCoor1)

def metinBul(lastCoor,lastCoor1):
    if l.get() == 1:
        if self1.hesap1.get() == 1:
            Info = pyBotOpenCV.matchTemplateImage(image=secilenMetin,region=stoneInfoArea,matchvalue=0.8)
            if Info is None:
                del Info
                metinAra(lastCoor,lastCoor1)
            else:
                if self1.hesap2.get() == 1:
                    metinBul1(lastCoor,lastCoor1)
                    del Info
                else:
                    bilgi.configure(text="Metin Kesiliyor") 
                time.sleep(0.1)
                del Info
        elif self1.hesap2.get() == 1:
            metinBul1(lastCoor,lastCoor1)
        
def metinBul1(lastCoor,lastCoor1):
    if l.get() == 1:
        Info = ZpyBotOpenCV.matchTemplateImage(image=secilenMetin1,region=stoneInfoArea1,matchvalue=0.91)
        if Info is None:
            metinAra1(lastCoor,lastCoor1)
        else:
            if self1.hesap1.get() == 1:
                metinBul(lastCoor,lastCoor1)
            else:
                bilgi.configure(text="Metin Kesiliyor")
            time.sleep(0.1)
            del Info

def metinKesPasif():
    lastCoor = (0, 0)
    lastCoor1 = (0, 0)
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
            del lastCoor
            return
        except Exception as e:
            print(e)
            time.sleep(0.1)
        
    if l.get() == 0:
        l.set(0)
        bilgi.configure(text="Metin Botu Durdu")
    del lastCoor
    return





   
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
        
        if self1.hesap1.get() == 1:
            left, top, right, bottom = win32gui.GetWindowRect(hwnd1)
            middle = get_window_size(hwnd1)
            if otoMetinButton5.get() == "Kurtuluş Metini":
                secilenMetin = "./AnkaMt2_Bot/img/KurtulusMetini.PNG"
                dagilimy = 150
                stoneInfoArea = (int(middle[0]/9),30,int(middle[0]*0.5),int(middle[1]/10))
            elif otoMetinButton5.get() == "Mutsuzluk Metini":
                secilenMetin = "./AnkaMt2_Bot/img/MutsuzlukMetini.PNG"
                dagilimy = 150
                stoneInfoArea = (int(middle[0]/9),30,int(middle[0]*0.5),int(middle[1]/10))
            elif otoMetinButton5.get() == "Hainlik Metini":
                secilenMetin = "./AnkaMt2_Bot/img/HainlikMetini.PNG"
                dagilimy = 150
                stoneInfoArea = (int(middle[0]/9),30,int(middle[0]*0.5),int(middle[1]/10))
            elif otoMetinButton5.get() == "Yeşil Lastik":
                secilenMetin = "./AnkaMt2_Bot/img/yesilLastik.PNG"
                dagilimy = 150
                stoneInfoArea = (int(middle[0]/9),30,int(middle[0]*0.5),int(middle[1]/10))
            else:
                hesap1 = True
                l.set(0)
        
        if self1.hesap2.get() == 1:
            left1, top1, right1, bottom1 = win32gui.GetWindowRect(hwnd2)
            middle1 = get_window_size(hwnd2)
            if hwnd2 != 0:
                if metinValue.get() == "Kurtuluş Metini":
                    secilenMetin1 = "./AnkaMt2_Bot/img/KurtulusMetini.PNG"
                    dagilimy1 = 150
                    stoneInfoArea = (int(middle[0]/9),30,int(middle[0]*0.5),int(middle[1]/10))
                elif metinValue.get() == "Mutsuzluk Metini":
                    secilenMetin1 = "./AnkaMt2_Bot/img/MutsuzlukMetini.PNG"
                    dagilimy1 = 150
                    stoneInfoArea = (int(middle[0]/9),30,int(middle[0]*0.5),int(middle[1]/10))
                elif metinValue.get() == "Hainlik Metini":
                    secilenMetin1 = "./AnkaMt2_Bot/img/HainlikMetini.PNG"
                    dagilimy1 = 150
                    stoneInfoArea = (int(middle[0]/9),30,int(middle[0]*0.5),int(middle[1]/10))
                elif metinValue.get() == "Yeşil Lastik":
                    secilenMetin1 = "./AnkaMt2_Bot/img/yesilLastik.PNG"
                    dagilimy1 = 150
                    stoneInfoArea = (int(middle[0]/9),30,int(middle[0]*0.5),int(middle[1]/10))
                else:
                    hesap2 = True
                    l.set(0)
            elif hwnd2 ==0:
                hesap2 = True
                hata = True
                l.set(0)
                bilgi.configure(text="2. Hesap Penceresi Belirtilmemiş!")
        if self1.hesap1.get() == 1 and self1.hesap2.get() == 1:
            if hesap1 == True or hesap2 == True:
                bilgi.configure(text="Lütfen Metin Belirtiniz!")
            if hata == True:
                bilgi.configure(text="2. Hesap Penceresi Belirtilmemiş!")
            else:
                threading.Thread(target=metinKesPasif).start()
        elif self1.hesap1.get() == 1 and self1.hesap2.get() == 0:
            if hesap1 == True:
                bilgi.configure(text="Lütfen Metin Belirtiniz!")
            else:
                threading.Thread(target=metinKesPasif).start()
        elif self1.hesap1.get() == 0 and self1.hesap2.get() == 1:
            if hesap2 == True:
                bilgi.configure(text="Lütfen Metin Belirtiniz!")
            if hata == True:
                bilgi.configure(text="2. Hesap Penceresi Belirtilmemiş!")
            else:
                threading.Thread(target=metinKesPasif).start()
        elif self1.hesap1.get() == 0 and self1.hesap2.get() == 0:
            l.set(0)
            bilgi.configure(text="Lütfen Metin veya Hesap Belirtiniz!")


def islemiBaslat():
    if c.get() == 1:
        time.sleep(0.1)
        keyboard.press("ctrl")
        time.sleep(0.1)
        keyboard.press("g")
        time.sleep(0.1)
        keyboard.release("ctrl")
        time.sleep(0.1)
        keyboard.release("g")
        time.sleep(1)
        keyboard.press(str(otoMetinEntryValue1.get()))
        time.sleep(0.1)
        keyboard.release(str(otoMetinEntryValue1.get()))
        time.sleep(2)
        keyboard.press("ctrl")
        time.sleep(0.1)
        keyboard.press("g")
        time.sleep(0.1)
        keyboard.release("ctrl")
        time.sleep(0.1)
        keyboard.release("g")
    if d.get() ==1:
        time.sleep(0.1)
        keyboard.press(str(otoMetinEntryValue1.get()))
        time.sleep(0.2)
        keyboard.release(str(otoMetinEntryValue1.get()))
        time.sleep(0.001)

def havaKiliciYak():
    if a.get() == 1:
        if self1.hesap1.get() == 1 or self1.hesap2.get() == 1:
            if self1.hesap1.get() == 1:
                while a.get() ==1:
                    try:
                        if c.get() == 0 and d.get() == 0:
                             bilgi2.configure(text="Hava Kılıcı Durumunu Belirt !", fg_color="red", text_color="black")
                             a.set(0)
                        elif c.get() == 1 and d.get() == 1:
                             bilgi2.configure(text="Her iki Durum Aktif Olamaz !", fg_color="red", text_color="black")
                             a.set(0)
                        else:
                            bilgi2.configure(text=" ", fg_color="transparent")
                            havaKiliciKapali = pyBotOpenCV.locateCenterOnScreen(image="./AnkaMt2_Bot/img/havaKilici.PNG",matchvalue=0.6,region=(0,0,int(right/3), int(bottom/5) )) # 252,70
                            if havaKiliciKapali == None:
                                win32gui.SetForegroundWindow(hwnd1)
                                islemiBaslat()
                            elif havaKiliciKapali != None:
                                time.sleep(5)

                    except Exception as e:
                        print(f"Hata: {e}")
                        time.sleep(3)
                              
            if self1.hesap2.get() == 1:
                while a.get() ==1:
                    try:
                        if c.get() == 0 and d.get() == 0:
                             bilgi2.configure(text="Hava Kılıcı Durumunu Belirt !", fg_color="red", text_color="black")
                             a.set(0)
                        elif c.get() == 1 and d.get() == 1:
                             bilgi2.configure(text="Her iki Durum Aktif Olamaz !", fg_color="red", text_color="black")
                             a.set(0)
                        else:
                            bilgi2.configure(text=" ", fg_color="transparent")
                            havaKiliciKapali = ZpyBotOpenCV.locateCenterOnScreen(image="./AnkaMt2_Bot/img/havaKilici.PNG",matchvalue=0.6,region=(0,0,int(right/3), int(bottom/5) )) # 252,70
                            if havaKiliciKapali == None:
                                win32gui.SetForegroundWindow(hwnd2)
                                islemiBaslat()
                            elif havaKiliciKapali != None:
                                time.sleep(5)

                    except Exception as e:
                        print(f"Hata: {e}")
                        time.sleep(3)
        
        elif self1.hesap1.get() == 0 and self1.hesap2.get() == 0:
            bilgi2.configure(text="Herhangi bir Hesap Seç !", fg_color="red", text_color="black")
            a.set(0)

def zamanlayici1():
    if o.get() ==1:
        k=1
        try:
            while k ==1:
                turkey_timezone = timezone(timedelta(hours=3))
                now_utc = datetime.now(timezone.utc)
                now_turkey = now_utc.astimezone(turkey_timezone)

                saat = now_turkey.hour
                dakika = now_turkey.minute+2
                saniye = now_turkey.second+40
                if saniye>=60:
                    dakika = dakika +1
                    saniye = saniye-60
                if dakika>=60:
                    saat=saat+1
                    dakika=dakika-60
                if saat>=24:
                    saat=saat-24
                kalanDakika = 2
                kalanSaniye = 40
                cikacakSaat.configure(text=f"{saat:02d}:{dakika:02d}:{saniye:02d}")
                x = now_turkey.second
                g=1
                while g==1:
                    turkey_timezone = timezone(timedelta(hours=3))
                    now_utc = datetime.now(timezone.utc)
                    now_turkey = now_utc.astimezone(turkey_timezone)
                    saat1 = now_turkey.hour
                    if saat1>=24:
                        saat1=saat1-24
                    kalanSüre.configure(text=f"Kalan Süre: 00:{kalanDakika:02d}:{kalanSaniye:02d}")
                    metinZamanlayici.configure(text=f"{saat1:02d}:{now_turkey.minute:02d}:{now_turkey.second:02d}")
                    if x != now_turkey.second:
                        if kalanSaniye==0:
                            kalanDakika = kalanDakika-1
                            kalanSaniye = 60
                        kalanSaniye=kalanSaniye-1
                    if o.get() ==0:
                        metinZamanlayici.configure(text="Durdu")
                        g=0
                        k=0
                    if now_turkey.minute==dakika and now_turkey.second==saniye:
                        g=0
                    x = now_turkey.second
                    time.sleep(0.1)
        except Exception as e:
                metinZamanlayici.configure(text=f"{e}")
                kalanSüre.configure(text="{}".format(e))
                cikacakSaat.configure(text="{}".format(e))
                print(f"Hata: {e}")
                time.sleep(3)
def zamanlayici():
    if o.get() ==1:        
        turkey_timezone = timezone(timedelta(hours=3))
        now_utc = datetime.now(timezone.utc)
        now_turkey = now_utc.astimezone(turkey_timezone)
        metininYenilenenSaati, metininYenilenenDakikasi, metininYenilenenSaniyesi = 13, 1, 6
        kalanZaman = 160
        kalanZamanDakika = 0
        kalanZamanSaniye = 0
        suankiSaniye1 = now_turkey.second
        while o.get() ==1:   
            try:
                turkey_timezone = timezone(timedelta(hours=3))
                now_utc = datetime.now(timezone.utc)
                now_turkey = now_utc.astimezone(turkey_timezone)
                
                suankiSaat, suankiDakika, suankiSaniye = now_turkey.hour, now_turkey.minute, now_turkey.second
                
                #if metininYenilenenSaati <= suankiSaat or (metininYenilenenSaniyesi <= suankiSaniye and metininYenilenenDakikasi == suankiDakika):
                if metininYenilenenSaniyesi <= suankiSaniye:
                    if metininYenilenenDakikasi == suankiDakika:
                        if metininYenilenenSaati <= suankiSaat:
                #if metininYenilenenSaati <= suankiSaat or (metininYenilenenSaniyesi <= suankiSaniye and metininYenilenenDakikasi <= suankiDakika):
                            metininYenilenenDakikasi +=2
                            metininYenilenenSaniyesi +=40
                            kalanZaman = 160
                    
                if metininYenilenenSaniyesi >= 60:
                    metininYenilenenDakikasi +=1
                    metininYenilenenSaniyesi -=60
                if metininYenilenenDakikasi >= 60:
                    metininYenilenenDakikasi -=60
                    metininYenilenenSaati +=1
                if metininYenilenenSaati >= 24:
                    metininYenilenenSaati -= 24
                    

                kalanZamanDakika = kalanZaman // 60
                kalanZamanSaniye = kalanZaman % 60

                if kalanZaman == 0:
                    kalanZaman = 160
                if suankiSaniye1<suankiSaniye:
                    kalanZaman -=1
                suankiSaniye1 = suankiSaniye
                metinZamanlayici.configure(text=f"{suankiSaat:02d}:{suankiDakika:02d}:{suankiSaniye:02d}")
                cikacakSaat.configure(text=f"{metininYenilenenSaati:02d}:{metininYenilenenDakikasi:02d}:{metininYenilenenSaniyesi:02d}")
                kalanSüre.configure(text=f"00:{kalanZamanDakika:02d}:{kalanZamanSaniye:02d}")
                time.sleep(0.1)

            except Exception as e:
                metinZamanlayici.configure(text=f"{e}")
                kalanSüre.configure(text="{}".format(e))
                cikacakSaat.configure(text="{}".format(e))
                print(f"Hata: {e}")
                time.sleep(3)
#######################################################################



def zamanlayiciCommand():
    threading.Thread(target=zamanlayici1).start()
    
def havaKilici():
    threading.Thread(target=havaKiliciYak).start()


def AllView(self,hwnd,hwnd3):
    global metinValue
    global o, l, a, c, d
    global otoMetinEntryValue
    global cikacakSaat, bilgi, kalanSüre, cikacakSaat1
    global metinZamanlayici
    global pyBotOpenCV, pyBotWin32, ZpyBotOpenCV, ZpyBotWin32
    global left, top, right, bottom
    global otoMetinEntryValue1
    global hwnd1, hwnd2
    global bilgi2
    global self1
    global otoMetinButton4, otoMetinButton1, otoMetinButton5

    self1 = self

    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    
   
    metinValue = tk.StringVar(self)
    metinValue.set("Metini Seçiniz!")
    metinler = ["Kurtuluş Metini",
    "Mutsuzluk Metini",
    "Hainlik Metini",
    "Yeşil Lastik",
    ]
    otoMetinButton5 = customtkinter.CTkOptionMenu(self.otoMetin,width=self.optionMenuWidth,height=self.optionMenuHeight, values=metinler, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666")
    otoMetinButton5.grid(row=0, column=1, padx=(0,0), pady=(40,0))
    otoMetinButton5.set("Metini Seçiniz!")
    otoMetinLabel = customtkinter.CTkLabel(self.otoMetin, text="1. Hesap",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight).grid(row=0,column=0, padx=(0,0), pady=(40,0))
    l = tk.IntVar()
    l.set(0)
    otoMetinButton = customtkinter.CTkCheckBox(self.otoMetin,text="Oto Metin Av Başlat",variable=l, command= otoMetinCommand,onvalue=1, offvalue=0,corner_radius=self.optionMenuCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinButton.grid(row=2,column=1, padx=(0,0), pady=(0,0))
    otoMetinLabel1 = customtkinter.CTkLabel(self.otoMetin, text="2. Hesap",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight).grid(row=1,column=0, padx=(0,0), pady=(0,0))
    otoMetinButton1 = customtkinter.CTkOptionMenu(self.otoMetin,width=self.optionMenuWidth,height=self.optionMenuHeight, values=metinler,variable=metinValue, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666")
    otoMetinButton1.grid(row=1,column=1, padx=(0,0), pady=(0,0))

    bilgi2 = customtkinter.CTkLabel(self.otoMetin, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi2.grid(row=7,columnspan=2,column=1)
    metinZamanlayici = customtkinter.CTkLabel(self.otoMetin, text="00.00.00",bg_color= "#9ACC7E",corner_radius=self.labelCornerRadius,text_color="#065535",width=self.labelWidth,height=self.labelHeight)
    metinZamanlayici.grid(row=4, column=1, padx=(60,0), pady=(0,0))
    cikacakSaat1 = customtkinter.CTkLabel(self.otoMetin, text="Metin Yenilenme Saati =",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    cikacakSaat1.grid(row=4, column=0, padx=(0,0), pady=(0,0))
    cikacakSaat = customtkinter.CTkLabel(self.otoMetin, text="00.00.00",bg_color= "#9ACC7E",corner_radius=self.labelCornerRadius,text_color="#065535",width=self.labelWidth,height=self.labelHeight)
    cikacakSaat.grid(row=4, column=1, padx=(0,70), pady=(0,0))
    kalanSüre = customtkinter.CTkLabel(self.otoMetin, text="Kalan Süre =",bg_color= "#9ACC7E",corner_radius=self.labelCornerRadius,text_color="#065535",width=self.labelWidth,height=self.labelHeight)
    kalanSüre.grid(row=3, column=1, padx=(0,0), pady=(15,0))

    bilgi = customtkinter.CTkLabel(self.otoMetin, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    bilgi.grid(row=2,column=0)
    o = tk.IntVar()
    o.set(0)
    metinZamanlayiciButon = customtkinter.CTkCheckBox(self.otoMetin,text="Saat: ",variable=o,command= zamanlayiciCommand, onvalue=1, offvalue=0, corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth,width=1,height=1)
    metinZamanlayiciButon.grid(row=3, column=0, padx=(0,0), pady=(15,0))
    
    a = tk.IntVar()
    a.set(0)
    otoMetinButton2 = customtkinter.CTkCheckBox(self.otoMetin,text="Hava Kılıcı Başlat",variable=a, command= havaKilici,onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinButton2.grid(row=7, column=0, padx=(0,0), pady=(0,0))
    c = tk.IntVar()
    c.set(1)
    otoMetinButton3 = customtkinter.CTkCheckBox(self.otoMetin,text="At Üzerinden",variable=c,onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinButton3.grid(row=6, column=0, padx=(0,30), pady=(0,0))
    d = tk.IntVar()
    d.set(0)
    otoMetinButton4 = customtkinter.CTkCheckBox(self.otoMetin,text="Yerde",variable=d,onvalue=1, offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
    otoMetinButton4.grid(row=6, column=1, padx=(0,40), pady=(0,0))
    otoMetinLabel2 = customtkinter.CTkLabel(self.otoMetin, text="Skill Tuşu =",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
    otoMetinLabel2.grid(row=5, column=0, padx=(20,0), pady=(15,0))
    otoMetinEntryValue1 = tk.StringVar(value=4)
    otoMetinEntry1 = customtkinter.CTkEntry(self.otoMetin,textvariable=otoMetinEntryValue1,corner_radius=self.entryCornerRadius,text_color="#bababa",width=self.entryWidth,height=self.entryHeight)
    otoMetinEntry1.grid(row=5, column=1, padx=(0,70), pady=(15,0))
    

    
    
    #### YENİ SCRİPT ####
    if hwnd3 != 0:
        hwnd2 = hwnd3
        ZpyBotOpenCV = Win32.PyBotOpenCV(hwnd2)
        ZpyBotWin32 = Win32.PyBotWin32(hwnd2)
        left1, top1, right1, bottom1 = win32gui.GetWindowRect(hwnd3)
    else:
        hwnd2 = 0
        otoMetinButton1.configure(state="disabled")
    hwnd1 = hwnd
    pyBotOpenCV = Win32.PyBotOpenCV(hwnd1)
    pyBotWin32 = Win32.PyBotWin32(hwnd1)