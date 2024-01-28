import customtkinter
import tkinter as tk
import threading
import time


def pencereyiKapat():
    g=0
    #self1.quit()
    self1.after(100, self1.quit())

def etkinlikSaati():
        global g
        self1.labelWidth=12
        self1.labelHeight=12
        etkinlikUyari = customtkinter.CTkLabel(self1, text= "Aktif Etkinlik Yok",width=self1.labelWidth,height=self1.labelHeight,text_color="#000000",corner_radius=8,fg_color="transparent")
        etkinlikUyari.place(x=100, y=310)
        sonrakiEtkinlik = customtkinter.CTkLabel(self1, text= "Sonraki Etkinlik: ",width=self1.labelWidth,height=self1.labelHeight,text_color="#bababa",corner_radius=8,fg_color="transparent")
        sonrakiEtkinlik.place(x=0,y=330)
        aaa = customtkinter.CTkLabel(self1, text= "Şuanki Etkinlik: ",width=self1.labelWidth,height=self1.labelHeight,text_color="#bababa",corner_radius=8,fg_color="transparent")
        aaa.place(x=0,y=310)
        sonrakiEtkinlik1 = customtkinter.CTkLabel(self1, text= "",width=self1.labelWidth,height=self1.labelHeight,text_color="#000000",corner_radius=8,fg_color="transparent")
        sonrakiEtkinlik1.place(x=100,y=330)
        saatLabel = customtkinter.CTkLabel(self1, text= "00.00.00.00",width=self1.labelWidth,height=self1.labelHeight,text_color="#bababa",corner_radius=8,fg_color="transparent")
        saatLabel.place(x=130, y=290)
        kapat = customtkinter.CTkButton(self1, text="Kapat", command=pencereyiKapat)
        kapat.pack(side=tk.BOTTOM)
        gunler=[(0,"Pazartesi"),(1,"Salı"),(2,"Çarşamba"),(3,"Perşembe"),(4,"Cuma"),(5,"Cumartesi"),(6,"Pazar")]
        g = 1
        try:
            while g==1:

                    epoch = time.gmtime(time.time())
                    saat = epoch.tm_hour+3
                    saat1 = epoch.tm_hour+3
                    dakika = epoch.tm_min
                    saniye = epoch.tm_sec
                    gun = epoch.tm_wday
                    if saniye>=60:
                        dakika = dakika +1
                        saniye = saniye-60
                    if dakika>=60:
                        saat=saat+1
                        dakika=dakika-60
                    if saat>=24:
                        saat=saat-24
                        
                    for a,b in gunler:
                        if int(gun)==int(a):
                            gunlerden = b
                            if saat1>=24:
                                if gunlerden=="Pazar":
                                    gunlerden = gunler[0]
                                    gunlerden = gunlerden[1]
                                else:
                                    gunlerden= gunler[a+1]
                                    gunlerden = gunlerden[1]
                            break
                    
                    saat_str = str(saat)
                    dakika_str = str(dakika)
                    saniye_str = str(saniye)
                    if len(saat_str) == 1 or len(dakika_str) == 1 or len(saniye_str) == 1:
                        if len(saat_str) == 1:
                            saat = f"0{saat}"
                        if len(dakika_str) == 1:
                            dakika = f"0{dakika}"
                        if len(saniye_str) == 1:
                            saniye = f"0{saniye}"
                    saatLabel.configure(text="{}: {}:{}:{}".format(gunlerden,saat,dakika,saniye))
                    time.sleep(1)
                   #### Pazar Günü İçin ####
                    if gunlerden == "Pazar":
                        if (saat>=13 and saat<15) or (saat>=19 and saat<21):
                            suankiEtkinlik = "Yeşil Vadi Etkinliği"
                            etkinlikUyari.configure(text = "Yeşil Vadi Etkinliği Aktif",bg_color="#e897a9")
                        elif (saat>=15 and saat <17) or (saat>=21 and saat<23):
                            suankiEtkinlik = "Harf Etkinliği"
                            etkinlikUyari.configure(text = "Harf Etkinliği Aktif",bg_color="#bee96a")
                        elif (saat>=17 and saat <19 and gunlerden=="Pazar"):
                            suankiEtkinlik = "Sanal Evren Etkinliği"
                            etkinlikUyari.configure(text = "Sanal Evren Etkinliği Aktif",bg_color="#f6f566")
                        else:
                            etkinlikUyari.configure(text = "Aktif Etkinlik Yok")
                        if saat<13:
                            sonrakiEtkinlik1.configure(text = "13.00/15.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                        elif saat>=13 and saat<15:
                            sonrakiEtkinlik1.configure(text = "15.00/17.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>=15 and saat<17:
                            sonrakiEtkinlik1.configure(text = "17.00/19.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=17 and saat<19:
                            sonrakiEtkinlik1.configure(text = "19.00/21.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                        elif saat>=19 and saat<21:
                            sonrakiEtkinlik1.configure(text = "21.00/23.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat1>=21:
                            sonrakiEtkinlik1.configure(text = "Pazartesi 13.00/15.00  Harf Etkinliği",bg_color="#bee96a")
                    #### Pazartesi Günü İçin ####
                    elif gunlerden == "Pazartesi":
                        if (saat>=13 and saat<15):
                            suankiEtkinlik = "Harf Etkinliği"
                            etkinlikUyari.configure(text = "Harf Etkinliği Aktif",bg_color="#bee96a")
                        elif (saat>=15 and saat <16) or (saat>=19 and saat<22):
                            suankiEtkinlik = "Kusursuz Sandık Etkinliği"
                            etkinlikUyari.configure(text = "Kusursuz Sandık Etkinliği Aktif",bg_color="#aafaf7")
                        elif (saat>=16 and saat <17) or (saat>=22 and saat <23):
                            suankiEtkinlik = "Sanal Evren Etkinliği"
                            etkinlikUyari.configure(text = "Sanal Evren Etkinliği Aktif",bg_color="#f6f566")
                        else:
                            etkinlikUyari.configure(text = "Aktif Etkinlik Yok")
                        if saat<13:
                            sonrakiEtkinlik1.configure(text = "13.00/15.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>=13 and saat<15:
                            sonrakiEtkinlik1.configure(text = "15.00/16.00  Kusursuz Sandık Etkinliği",bg_color="#aafaf7")
                        elif saat>=15 and saat<16:
                            sonrakiEtkinlik1.configure(text = "16.00/17.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=16 and saat<19:
                            sonrakiEtkinlik1.configure(text = "19.00/22.00  Kusursuz Sandık Etkinliği",bg_color="#aafaf7")
                        elif saat>=19 and saat<22:
                            sonrakiEtkinlik1.configure(text = "22.00/23.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat1>=22:
                            sonrakiEtkinlik1.configure(text = "Salı 13.00/15.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                    #### Salı Günü İçin ####
                    if gunlerden == "Salı":
                        if (saat>=13 and saat<15) or (saat>=19 and saat<21):
                            suankiEtkinlik = "Yeşil Vadi Etkinliği"
                            etkinlikUyari.configure(text = "Yeşil Vadi Etkinliği Aktif",bg_color="#e897a9")
                        elif (saat>=15 and saat <16) or (saat>=21 and saat<22):
                            suankiEtkinlik = "Harf Etkinliği"
                            etkinlikUyari.configure(text = "Harf Etkinliği Aktif",bg_color="#bee96a")
                        elif (saat>=16 and saat <17) or (saat>=22 and saat <23):
                            suankiEtkinlik = "Sanal Evren Etkinliği"
                            etkinlikUyari.configure(text = "Sanal Evren Etkinliği Aktif",bg_color="#f6f566")
                        else:
                            etkinlikUyari.configure(text = "Aktif Etkinlik Yok")
                        if saat<13:
                            sonrakiEtkinlik1.configure(text = "13.00/15.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                        elif saat>=13 and saat<15:
                            sonrakiEtkinlik1.configure(text = "15.00/16.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>=15 and saat<16:
                            sonrakiEtkinlik1.configure(text = "16.00/17.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=16 and saat<19:
                            sonrakiEtkinlik1.configure(text = "19.00/21.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                        elif saat>=19 and saat<21:
                            sonrakiEtkinlik1.configure(text = "21.00/22.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>=21 and saat<22:
                            sonrakiEtkinlik1.configure(text = "22.00/23.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat1>=22:
                            sonrakiEtkinlik1.configure(text = "Çarşamba 13.00/16.00  Kusursuz Sandık Etkinliği",bg_color="#aafaf7")
                    #### Çarşamba Günü İçin ####
                    if gunlerden =="Çarşamba":
                        if (saat>=13 and saat <16) or (saat>=21 and saat<22):
                            suankiEtkinlik = "Kusursuz Sandık Etkinliği"
                            etkinlikUyari.configure(text = "Kusursuz Sandık Etkinliği Aktif",bg_color="#aafaf7")
                        elif (saat>=19 and saat <21):
                            suankiEtkinlik = "Harf Etkinliği"
                            etkinlikUyari.configure(text = "Harf Etkinliği Aktif",bg_color="#bee96a")
                        elif (saat>=16 and saat <17) or (saat>=22 and saat <23):
                            suankiEtkinlik = "Sanal Evren Etkinliği"
                            etkinlikUyari.configure(text = "Sanal Evren Etkinliği Aktif",bg_color="#f6f566")
                        else:
                            etkinlikUyari.configure(text = "Aktif Etkinlik Yok")
                        if saat<13:
                            sonrakiEtkinlik1.configure(text = "13.00/16.00  Kusursuz Sandık Etkinliği",bg_color="#aafaf7")
                        elif saat>=13 and saat<16:
                            sonrakiEtkinlik1.configure(text = "16.00/17.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=16 and saat<19:
                            sonrakiEtkinlik1.configure(text = "19.00/21.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>=19 and saat<21:
                            sonrakiEtkinlik1.configure(text = "21.00/22.00  Kusursuz Sandık Etkinliği",bg_color="#aafaf7")
                        elif saat>=21 and saat<22:
                            sonrakiEtkinlik1.configure(text = "22.00/23.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat1>=22:
                            sonrakiEtkinlik1.configure(text = "Perşembe 13.00/14.00  Harf Etkinliği",bg_color="#bee96a")
                    #### Perşembe Günü İçin ####
                    if gunlerden=="Perşembe":
                        if (saat>=13 and saat <14) or (saat>=19 and saat<20):
                            suankiEtkinlik = "Harf Etkinliği"
                            etkinlikUyari.configure(text = "Harf Etkinliği Aktif",bg_color="#bee96a")
                        elif (saat>=14 and saat<16) or (saat>=20 and saat<22):
                            suankiEtkinlik = "Yeşil Vadi Etkinliği"
                            etkinlikUyari.configure(text = "Yeşil Vadi Etkinliği Aktif",bg_color="#e897a9")
                        elif (saat>=16 and saat <17) or (saat>=22 and saat <23):
                            suankiEtkinlik = "Sanal Evren Etkinliği"
                            etkinlikUyari.configure(text = "Sanal Evren Etkinliği Aktif",bg_color="#f6f566")
                        else:
                            etkinlikUyari.configure(text = "Aktif Etkinlik Yok")
                        if saat<13:
                            sonrakiEtkinlik1.configure(text = "13.00/14.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>=13 and saat<14:
                            sonrakiEtkinlik1.configure(text = "14.00/16.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                        elif saat>=14 and saat<16:
                            sonrakiEtkinlik1.configure(text = "16.00/17.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=16 and saat<19:
                            sonrakiEtkinlik1.configure(text = "19.00/20.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>=19 and saat<20:
                            sonrakiEtkinlik1.configure(text = "20.00/22.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                        elif saat>=20 and saat<22:
                            sonrakiEtkinlik1.configure(text = "22.00/23.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=22:
                            sonrakiEtkinlik1.configure(text = "Cuma 13.00/15.00  Harf Etkinliği",bg_color="#bee96a")
                    #### Cuma Günü İçin ####
                    if gunlerden=="Cuma":
                        if (saat>=13 and saat <15):
                            suankiEtkinlik = "Harf Etkinliği"
                            etkinlikUyari.configure(text = "Harf Etkinliği Aktif",bg_color="#bee96a")
                        elif (saat>=15 and saat <16) or (saat>=20 and saat<23):
                            suankiEtkinlik = "Kusursuz Sandık Etkinliği"
                            etkinlikUyari.configure(text = "Kusursuz Sandık Etkinliği Aktif",bg_color="#aafaf7")
                        elif (saat>=16 and saat <17) or (saat>=23 and saat1<24):
                            suankiEtkinlik = "Sanal Evren Etkinliği"
                            etkinlikUyari.configure(text = "Sanal Evren Etkinliği Aktif",bg_color="#f6f566")
                        else:
                            etkinlikUyari.configure(text = "Aktif Etkinlik Yok")
                        if saat<13:
                            sonrakiEtkinlik1.configure(text = "13.00/15.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>= 13 and saat<15:
                            sonrakiEtkinlik1.configure(text = "15.00/16.00  Kusursuz Sandık Etkinliği",bg_color="#aafaf7")
                        elif saat>=15 and saat<16:
                            sonrakiEtkinlik1.configure(text = "16.00/17.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=16 and saat<20:
                            sonrakiEtkinlik1.configure(text = "20.00/23.00  Kusursuz Sandık Etkinliği",bg_color="#aafaf7")
                        elif saat>=20 and saat<23:
                            sonrakiEtkinlik1.configure(text = "23.00/24.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=23:
                            sonrakiEtkinlik1.configure(text = "Cumartesi 13.00/15.00  Harf Etkinliği",bg_color="#bee96a")
                    #### Cumartesi Günü İçin ####
                    if gunlerden=="Cumartesi":
                        if (saat>=13 and saat <15) or (saat>=19 and saat<21):
                            suankiEtkinlik = "Harf Etkinliği"
                            etkinlikUyari.configure(text = "Harf Etkinliği Aktif",bg_color="#bee96a")
                        elif (saat>=15 and saat<17) or (saat>=21 and saat<23):
                            suankiEtkinlik = "Yeşil Vadi Etkinliği"
                            etkinlikUyari.configure(text = "Yeşil Vadi Etkinliği Aktif",bg_color="#e897a9")
                        elif (saat>=17 and saat <18) or (saat>=23 and saat1<24):
                            suankiEtkinlik = "Sanal Evren Etkinliği"
                            etkinlikUyari.configure(text = "Sanal Evren Etkinliği Aktif",bg_color="#f6f566")
                        else:
                            etkinlikUyari.configure(text = "Aktif Etkinlik Yok")
                        if saat<13:
                            sonrakiEtkinlik1.configure(text = "13.00/15.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>=13 and saat<15:
                            sonrakiEtkinlik1.configure(text = "15.00/17.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                        elif saat>=15 and saat<17:
                            sonrakiEtkinlik1.configure(text = "17.00/18.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=17 and saat<19:
                            sonrakiEtkinlik1.configure(text = "19.00/21.00  Harf Etkinliği",bg_color="#bee96a")
                        elif saat>=19 and saat<21:
                            sonrakiEtkinlik1.configure(text = "21.00/23.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                        elif saat>=21 and saat<23:
                            sonrakiEtkinlik1.configure(text = "23.00/24.00  Sanal Evren Etkinliği",bg_color="#f6f566")
                        elif saat>=23:
                            sonrakiEtkinlik1.configure(text = "Pazar 13.00/15.00  Yeşil Vadi Etkinliği",bg_color="#e897a9")
                    #############################
                    if g==0:
                        self1.after(100, pencereyiKapat)
                        break
            if g==0:
                self1.after(100, pencereyiKapat)

        except Exception as e:
            if g==0:
                #break
                self1.after(100, pencereyiKapat)
            #bilgi.configure(text=f"Hata: {e}")
            print(e)
            
                
            
def etkinlikSaatiBaslat(self):
    global self1
    self1 = self
    threading.Thread(target=etkinlikSaati).start()