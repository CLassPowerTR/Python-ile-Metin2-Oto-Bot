import customtkinter
import win32gui
import tkinter as tk
from Phebia2_Bot import botWindow as phebia2
from RikaMt2_Bot import botWindow as rika2
from AnkaMt2_Bot import botWindow as anka2
   

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class MainWindow(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x300")
        self.resizable(False, False)
        self.title("Start Stone Bot")
        
        version = customtkinter.CTkLabel(self, text="CLassPowerTR | METİN_BOTU_Version v1 Test",width=15,height=8,corner_radius=8)
        version.pack(side= tk.BOTTOM)
        label = customtkinter.CTkLabel(self, text="Select Window", corner_radius=8, width=15, height=8)
        label.place(relx=0.35, rely=0.05)
        
        label1 = customtkinter.CTkLabel(self, text="1.Hesap", corner_radius=8, width=300, height=50)
        label1.place(relx=0.01, rely=0.1)
        label2 = customtkinter.CTkLabel(self, text="2. Hesap", corner_radius=8, width=300, height=50)
        label2.place(relx=0.01, rely=0.25)
        
        self.label1 = customtkinter.CTkLabel(self, text="", corner_radius=8, width=120, height=25, fg_color="#FF3333")
        self.label1.place(relx=0.22, rely=0.65)
        
        self.combobox = customtkinter.CTkComboBox(self, width=200, height=30, font=("Arial", 15))
        self.combobox.place(relx=0.15, rely=0.2)
        self.combobox.set("Pencereyi Seçiniz! (*)")
        
        self.combobox2 = customtkinter.CTkComboBox(self, width=200, height=30, font=("Arial", 15))
        self.combobox2.place(relx=0.15, rely=0.35)
        self.combobox2.set("Pencereyi Seçiniz!")
        
        self.combobox3 = customtkinter.CTkComboBox(self, width=200, height=30, font=("Arial", 15))
        self.combobox3.place(relx=0.15, rely=0.5)
        self.combobox3.set("Server Seçiniz! (*)")
        
        self.button = customtkinter.CTkButton(self, text="Start Stone Bot", command=self.open_new_window, width=200, height=30)
        self.button.place(relx=0.15, rely=0.75)
        self.add_comboitem()
        self.add_serverName()
        
    def open_new_window(self):
        selected_option = self.combobox.get()
        titleName = self.combobox.get()
        selected_option2 = self.combobox2.get()
        titleName2 = self.combobox2.get()

        if selected_option == selected_option2:
            self.label1.configure(text="İki Pencere Aynı Olamaz!")

        else:
            if self.combobox3.get() == "Phebia2" and selected_option != "Pencereyi Seçiniz! (*)":
                    if selected_option2 != "Pencereyi Seçiniz!":
                        hwnd = int(selected_option.split()[0])
                        hwnd1 = int(selected_option2.split()[0])
                        titleName = f"{hwnd}  ve {hwnd1} - Phebia"
                        self.protocol("WM_DELETE_WINDOW")
                        self.destroy()
                        phebia2.startBotWindow(hwnd,hwnd1,titleName)
                    else:
                        hwnd = int(selected_option.split()[0])
                        hwnd1 = int(0)
                        self.protocol("WM_DELETE_WINDOW")
                        self.destroy()
                        phebia2.startBotWindow(hwnd,hwnd1,titleName)

            elif self.combobox3.get() == "RikaMt2" and selected_option != "Pencereyi Seçiniz! (*)":
                    if selected_option2 != "Pencereyi Seçiniz!":
                        hwnd = int(selected_option.split()[0])
                        hwnd1 = int(selected_option2.split()[0])
                        titleName = f"{hwnd}  ve {hwnd1} - RikaMt2"
                        self.protocol("WM_DELETE_WINDOW")
                        self.destroy()
                        rika2.startBotWindow(hwnd,hwnd1,titleName)
                    else:
                        hwnd = int(selected_option.split()[0])
                        hwnd1 = int(0)
                        self.protocol("WM_DELETE_WINDOW")
                        self.destroy()
                        rika2.startBotWindow(hwnd,hwnd1,titleName)
                        
            elif self.combobox3.get() == "Anka2" and selected_option != "Pencereyi Seçiniz! (*)":
                    if selected_option2 != "Pencereyi Seçiniz!":
                        hwnd = int(selected_option.split()[0])
                        hwnd1 = int(selected_option2.split()[0])
                        titleName = f"{hwnd}  ve {hwnd1} - RikaMt2"
                        self.protocol("WM_DELETE_WINDOW")
                        self.destroy()
                        anka2.startBotWindow(hwnd,hwnd1,titleName)
                    else:
                        hwnd = int(selected_option.split()[0])
                        hwnd1 = int(0)
                        self.protocol("WM_DELETE_WINDOW")
                        self.destroy()
                        anka2.startBotWindow(hwnd,hwnd1,titleName)
                        
            else:
                self.label1.configure(text="Lütfen Server Seçiniz!")

            
    def listWindowNames(self):
        def winEnumHandler(hwnd, data_hwnd):
            if win32gui.IsWindowVisible(hwnd):
                data_hwnd.append((hwnd,win32gui.GetWindowText(hwnd)))
        data_hwnd = []
        win32gui.EnumWindows(winEnumHandler, data_hwnd)
        return data_hwnd

    def add_serverName(self):
        servers = ["Phebia2","RikaMt2","Anka2"]
        self.combobox3.configure(values=servers,text_color= "White",font=("Arial", 15))

    def add_comboitem(self):
        values = []
        for name_pg, window_text in self.listWindowNames():
            if len(win32gui.GetWindowText(name_pg)) != 0:
                window_text = str(name_pg)+ " = "+str(win32gui.GetWindowText(name_pg))
                values.append(window_text)
        self.combobox.configure(values=values,text_color= "White",font=("Arial", 15))
        self.combobox2.configure(values=values,text_color= "White",font=("Arial", 15))

if __name__ == "__main__":
    app = MainWindow()
    app.after(0, app.mainloop())