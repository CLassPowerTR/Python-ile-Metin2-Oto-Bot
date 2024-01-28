import customtkinter

def labels(self):
        labelWidth=12
        labelHeight=12
        saatler = {"13/14":1,"14/15":2,"15/16":3,"16/17":4,"17/18":5,"18/19":6,"19/20":7,"20/21":8,"21/22":9,"22/23":10,"23/24":11}
        gunler = {"P.tesi":1,"Salı":2,"Çarşmb":3,"Perşmb":4,"Cuma":5,"C.tesi":6,"Pazar":7}
        spacer  = customtkinter.CTkLabel(self.etkinlik,text=" ")
        spacer.grid(row=0,column=0, padx=(0,0), pady=(20,0))
        for i in saatler:
            saatlerLabel = customtkinter.CTkLabel(self.etkinlik, text=i,bg_color="#99b7f6",width=labelWidth,height=labelHeight,text_color="#000000")
            saatlerLabel.grid(row=saatler[i],column=0)
            if saatler[i]>=1 and saatler[i]<=2:
                columnn = [1,5,6]
                for f in columnn:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Harf",bg_color="#bee96a",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=saatler[i],column=f)
            elif saatler[i]>2 and saatler[i]<=3:
                a = customtkinter.CTkLabel(self.etkinlik, text="Sandk",bg_color="#aafaf7",width=labelWidth,height=labelHeight,text_color="#000000")
                a.grid(row=saatler[i],column=1)
            elif saatler[i]==4:
                for f in range(1,6):
                    a = customtkinter.CTkLabel(self.etkinlik, text="Sanal",bg_color="#f6f566",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=saatler[i],column=f)
            elif saatler[i] == 5:
                columnn = [1,2,3,4,5]
                for f in range(6,8):
                    a = customtkinter.CTkLabel(self.etkinlik, text="Sanal",bg_color="#f6f566",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=saatler[i],column=f)
                for d in columnn:
                    a = customtkinter.CTkLabel(self.etkinlik, text="----",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=5,column=d)
            elif saatler[i]==6:
                columnn = [1,2,3,4,5,6]
                for f in columnn:
                    a = customtkinter.CTkLabel(self.etkinlik, text="----",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=saatler[i],column=f)
            elif saatler[i]>=7 and saatler[i]<=9:
                a = customtkinter.CTkLabel(self.etkinlik, text="Sandk",bg_color="#aafaf7",width=labelWidth,height=labelHeight,text_color="#000000")
                a.grid(row=saatler[i],column=1)
            elif saatler[i]==10:
                for f in range(1,5):
                    a = customtkinter.CTkLabel(self.etkinlik, text="Sanal",bg_color="#f6f566",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=saatler[i],column=f)
            elif saatler[i] == 11:
                columnn = [1,2,3,4,7]
                for f in range(5,7):
                    a = customtkinter.CTkLabel(self.etkinlik, text="Sanal",bg_color="#f6f566",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=saatler[i],column=f)
                for d in columnn:
                    a = customtkinter.CTkLabel(self.etkinlik, text="----",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=saatler[i],column=d)
        a = customtkinter.CTkLabel(self.etkinlik, text="----",width=labelWidth,height=labelHeight,text_color="#000000")
        a.grid(row=7,column=5)
        for n in gunler:
            a = customtkinter.CTkLabel(self.etkinlik, text=n,bg_color="#f4c679",width=labelWidth,height=labelHeight,text_color="#000000")
            a.grid(row=0,column=gunler[n], padx=(0,0), pady=(30,0))
            if gunler[n]==2:
                roww = [1,2,7,8]
                roww1 = [3,9]
                for f in roww:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Vadi",bg_color="#e897a9",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=f,column=gunler[n])
                for d in roww1:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Harf",bg_color="#bee96a",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=d,column=gunler[n])
            if gunler[n]==3:
                roww = [1,2,3,9]
                for f in roww:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Sandk",bg_color="#aafaf7",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=f,column=gunler[n])
                for d in range(7,9):
                    a = customtkinter.CTkLabel(self.etkinlik, text="Harf",bg_color="#bee96a",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=d,column=gunler[n])
            if gunler[n]==4:
                roww = [2,3,8,9]
                roww1 = [1,7]
                for f in roww:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Vadi",bg_color="#e897a9",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=f,column=gunler[n])
                for d in roww1:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Harf",bg_color="#bee96a",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=d,column=gunler[n])
            if gunler[n]==5:
                roww = [3,8,9,10]
                for f in roww:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Sandk",bg_color="#aafaf7",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=f,column=gunler[n])
            if gunler[n]==6:
                roww = [3,4,9,10]
                for f in roww:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Vadi",bg_color="#e897a9",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=f,column=gunler[n])
                for d in range(7,9):
                    a = customtkinter.CTkLabel(self.etkinlik, text="Harf",bg_color="#bee96a",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=d,column=gunler[n])
            if gunler[n]==7:
                a = customtkinter.CTkLabel(self.etkinlik, text="Sanal",bg_color="#f6f566",width=labelWidth,height=labelHeight,text_color="#000000")
                a.grid(row=6,column=gunler[n])
                roww = [1,2,7,8]
                roww1 = [3,4,9,10]
                for f in roww:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Vadi",bg_color="#e897a9",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=f,column=gunler[n])
                for d in roww1:
                    a = customtkinter.CTkLabel(self.etkinlik, text="Harf",bg_color="#bee96a",width=labelWidth,height=labelHeight,text_color="#000000")
                    a.grid(row=d,column=gunler[n]),
                    