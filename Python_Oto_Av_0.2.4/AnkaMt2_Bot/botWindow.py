import customtkinter
import tkinter as tk
from AnkaMt2_Bot import etkinlikLabel
import threading
import time
import win32gui
from AnkaMt2_Bot import otoMetinMenu
from AnkaMt2_Bot import otoMetinMenuTest
from AnkaMt2_Bot import otoGirisMenu
from AnkaMt2_Bot import otoTusMenu
from AnkaMt2_Bot import etkinlikSaati


class Window(customtkinter.CTk):
    def __init__(self,hwnd,hwnd1,titleName, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hwnd = hwnd
        self.hwnd1 = hwnd1
        self.geometry("360x420")
        self.resizable(width = False, height = False)
        versionNum = "0.2.3"
        version = customtkinter.CTkLabel(self, text=f"By Batuhan | Anka2_METİN_BOTU_Version v{versionNum}",width=15,height=8,corner_radius=8)
        version.pack(side= tk.BOTTOM)
        self.title(titleName)
        self.menu = customtkinter.CTkTabview(self)
        self.protocol("WM_DELETE_WINDOW", self.pencereyiKapat)
        self.menu.pack(side= tk.TOP,expand=True, fill="both")
        self.otoGiris = self.menu.add("Oto Giriş")
        self.otoMetin = self.menu.add("Oto Metin")
        self.otoTus = self.menu.add("Oto Tuş")
        self.etkinlik = self.menu.add("Etkinlik")
        self.ticaret = self.menu.add("Ticaret")
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


        ##################################################################################################################
        #                                             HESAPLAR                                                           #
        ##################################################################################################################       
        self.hesap1 = tk.IntVar(self)
        self.hesap1.set(0)
        self.hesap2 = tk.IntVar(self)
        self.hesap2.set(0)
        hesap1CheckBox = customtkinter.CTkCheckBox(master=self,text="1. Hesap",onvalue=1, offvalue=0,variable=self.hesap1,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
        hesap1CheckBox.place(x=10, y=50)
        hesap2CheckBox = customtkinter.CTkCheckBox(master=self,text="2. Hesap",onvalue=1, offvalue=0,variable=self.hesap2,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_height=self.checkboxHeight,checkbox_width=self.checkboxWidth)
        hesap2CheckBox.place(x=180, y=50)
        
            # Buttons
        # Pencereyi Öne Çıkar #
        button = customtkinter.CTkButton(master=self, text="Öne Çıkar", command=self.oneGetir, width=30, height=20)
        button.place(x=100, y=50)
        button1 = customtkinter.CTkButton(master=self, text="Öne Çıkar", command=self.oneGetir1, width=30, height=20)
        button1.place(x=270, y=50)

        if hwnd1 == 0:
            hesap2CheckBox.configure(state="disabled")
            button1.configure(state="disabled")
        ################################### OTO GİRİŞ ###########################################
        self.after(1, otoGirisMenu.AllView(self,self.hwnd,self.hwnd1))
        ################################### OTO METİN ###########################################
        self.after(1, otoMetinMenu.AllView(self,self.hwnd,self.hwnd1))
        ################################### OTO TUŞ ###########################################
        self.after(1, otoTusMenu.AllView(self,self.hwnd,self.hwnd1))
        ################################################ CHLER ARASI FARM ########################################################
        """
        chlerArasiFarmBilgi = customtkinter.CTkLabel(self.otoTus, text="CHLER",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        chlerArasiFarmBilgi.grid(row=4,column=0)
        chlerArasiFarmBilgi1 = customtkinter.CTkLabel(self.otoTus, text="ARASI",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        chlerArasiFarmBilgi1.grid(row=4,column=1)
        chlerArasiFarmBilgi2 = customtkinter.CTkLabel(self.otoTus, text="FARM",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        chlerArasiFarmBilgi2.grid(row=4,column=2)
        otoFarm = customtkinter.CTkLabel(self.otoTus, text="Deaktif",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        otoFarm.grid(row=5,column=3)
        otoTusButton4Baslat = tk.IntVar(self)
        otoTusButton4Baslat.set(0)
        otoTusButton4 = customtkinter.CTkCheckBox(self.otoTus,text="BAŞLAT", variable=otoTusButton4Baslat, onvalue=1,offvalue=0,corner_radius=self.checkboxCornerRadius,text_color="#bababa",checkbox_width=self.checkboxWidth,checkbox_height=self.checkboxHeight).grid(row=5,column=2)
        otoTusLabel6 = customtkinter.CTkLabel(self.otoTus,text="Kanal =",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        otoTusLabel6.grid(row=5 ,column=0)
        secilenKanal = tk.StringVar(self)
        channels = [
        "Kanal 1",
        "Kanal 2",
        "Kanal 3",
        "Kanal 4",
        "Kanal 5",
        "Kanal 6",
        ]
        secilenKanal.set("Kanal 1")
        otoTusButton5 = customtkinter.CTkOptionMenu(self.otoTus, values=channels, variable=secilenKanal,width=self.optionMenuWidth,height=self.optionMenuHeight, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666").grid(row=5,column=1)


        chlerArasiFarmBilgi3 = customtkinter.CTkLabel(self.otoTus, text="Bot Durumu: ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        chlerArasiFarmBilgi3.grid(row=6,column=1)
        chlerArasiFarmBilgi4 = customtkinter.CTkLabel(self.otoTus, text="Şuan ki Kanal: ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        chlerArasiFarmBilgi4.grid(row=7,column=1)
        chlerArasiFarmBilgi5 = customtkinter.CTkLabel(self.otoTus, text="Sonra ki Kanal: ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        chlerArasiFarmBilgi5.grid(row=8,column=1)
        chlerArasiFarmBilgi6 = customtkinter.CTkLabel(self.otoTus, text="Deaktif",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        chlerArasiFarmBilgi6.grid(row=6,column=2)
        chlerArasiFarmBilgi7 = customtkinter.CTkLabel(self.otoTus, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        chlerArasiFarmBilgi7.grid(row=7,column=2)
        chlerArasiFarmBilgi8 = customtkinter.CTkLabel(self.otoTus, text=" ",corner_radius=self.labelCornerRadius,text_color="#bababa",width=self.labelWidth,height=self.labelHeight)
        chlerArasiFarmBilgi8.grid(row=8,column=2)
        """
        ##################################################################################################################
        #                                             ETKİNLİK                                                           #
        ##################################################################################################################
        self.after(1, etkinlikLabel.labels(self))
        

        ##################################################################################################################
        #                                             TİCARET                                                            #
        ##################################################################################################################
        karakter = tk.StringVar(self)
        karakter.set("Karakter")
        karakterler = ["Savaşcı","Ninja","Sura","Şaman"]
        etkinlikMenu = customtkinter.CTkOptionMenu(master=self.ticaret, values=karakterler, variable=karakter, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666").grid(row=0,column=0,columnspan=2, padx=(100,0), pady=(50,0))
        nesne = tk.StringVar(self)
        nesne.set("Nesneler")
        nesneler = ["Hepsi","Silahlar","Ekipman","Kostümler"]
        etkinlikMenu1 = customtkinter.CTkOptionMenu(master=self.ticaret, values=nesneler, variable=nesne, corner_radius=self.optionMenuCornerRadius,text_color="#bababa",button_color="#56aaff",button_hover_color="#666666").grid(row=0,column=0,columnspan=2, padx=(0,200), pady=(50,0))
        tekCift = tk.StringVar(self)
        ticaretLabel= customtkinter.CTkLabel(master=self.ticaret, text="İtem İsmi =",corner_radius=self.labelCornerRadius,text_color="#bababa")
        ticaretLabel.grid(row=1,column=0, padx=(20,0), pady=(10,0))
        ticaretEntryValue = tk.StringVar(self)
        ticaretEntry = customtkinter.CTkEntry(master=self.ticaret,placeholder_text="İtem Adı", textvariable = ticaretEntryValue, corner_radius=self.entryCornerRadius,text_color="#bababa",width=150)
        ticaretEntry.grid(row=1,column=1, padx=(0,20), pady=(10,0))
        ticaretLabel1= customtkinter.CTkLabel(master=self.ticaret, text="CHAT BAĞIRMA | MESAJINIZI YAZINIZ",corner_radius=self.labelCornerRadius,text_color="#bababa")
        ticaretLabel1.grid(row=3,column=0,columnspan=2, padx=(0,0), pady=(0,0))
        ticaretEntryValue1 = tk.StringVar(self)
        ticaretEntry1 = customtkinter.CTkEntry(master=self.ticaret,placeholder_text="Bagirma Mesaji Giriniz...", textvariable = ticaretEntryValue1, corner_radius=self.entryCornerRadius,text_color="#bababa",width=300)
        ticaretEntry1.grid(row=4,column=0,columnspan=2, padx=(0,0), pady=(0,0))


        ##################################################################################################################
        #                                         ETKİNLİK SAATİ                                                         #
        ##################################################################################################################
        self.after(1, etkinlikSaati.etkinlikSaatiBaslat(self))
        
    def pencereyiKapat(self):
        try:
            self.quit()
        except Exception as e:
            print(f"Hata: {e}")
            self.quit()

    def oneGetir(self):
        try:
            if self.hwnd != 0:
                win32gui.SetForegroundWindow(self.hwnd)
            else:
                print(f"Hata {self.hwnd}")
        except Exception as e:
            print(f"Hata: {e}")

    def oneGetir1(self):
        try:
            if self.hwnd1 != 0:
                win32gui.SetForegroundWindow(self.hwnd1)
            else:
                print(f"Hata {self.hwnd1}")
        except Exception as e:
            print(f"Hata: {e}")


def startBotWindow(hwnd,hwnd1,titleName):
    app = Window(hwnd,hwnd1,titleName)
    app.after(100, app.mainloop())