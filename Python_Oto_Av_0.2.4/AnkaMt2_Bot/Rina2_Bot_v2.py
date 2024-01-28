import customtkinter
import botWindow
import win32gui
import tkinter as tk

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue") 
class MainWindow(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x180")
        self.resizable(False, False)
        self.title("Start RinaMt2 Bot Test")
        version = customtkinter.CTkLabel(self, text="CLassPowerTR | METİN_BOTU_Version v2 Test",width=15,height=8,corner_radius=8)
        version.pack(side= tk.BOTTOM)
        label = customtkinter.CTkLabel(self, text="Select Window", corner_radius=8, width=150, height=30)
        label.place(relx=0.22, rely=0.1)
        
        self.combobox = customtkinter.CTkComboBox(self, width=200, height=30, font=("Arial", 15))
        self.combobox.place(relx=0.15, rely=0.3)
        self.combobox.set(" ")
        
        self.button = customtkinter.CTkButton(self, text="Start RinaMt2 Bot", command=self.open_new_window, width=200, height=30)
        self.button.place(relx=0.15, rely=0.7)
        self.add_comboitem()
    def open_new_window(self):
        selected_option = self.combobox.get()
        titleName = self.combobox.get()
        if selected_option !=" ":
            hwnd = int(selected_option.split()[0])
            self.protocol("WM_DELETE_WINDOW")
            self.destroy()
            botWindow.startBotWindow(hwnd,titleName)
        else:
            label1 = customtkinter.CTkLabel(self, text="Lütfen Pencereyi Seçiniz", corner_radius=8, width=120, height=25, fg_color="#FF3333")
            label1.place(relx=0.22, rely=0.5)

    def listWindowNames(self):
        def winEnumHandler(hwnd, data_hwnd):
            if win32gui.IsWindowVisible(hwnd):
                data_hwnd.append((hwnd,win32gui.GetWindowText(hwnd)))
        data_hwnd = []
        win32gui.EnumWindows(winEnumHandler, data_hwnd)
        return data_hwnd

    def add_comboitem(self):
        values = []
        for name_pg, window_text in self.listWindowNames():
            if len(win32gui.GetWindowText(name_pg)) != 0:
                window_text = str(name_pg)+ " = "+str(win32gui.GetWindowText(name_pg))
                values.append(window_text)
        self.combobox.configure(values=values,text_color= "White",font=("Arial", 15))

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
