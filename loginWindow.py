from email import utils
from tkinter import *
import mainWindow
import pickle
import json
from src.domains import utils

def clear_u(entry):
    if entry.get() == "Username":
        entry.delete(0, END)
        entry.configure(foreground = "#FFFFFF")
    else:
        pass
def clear_p(entry):
    if entry.get() == "Password":
        entry.delete(0, END)
        entry.configure(foreground = "#FFFFFF")
        entry.config(show = "*")
    else:
        pass
    
def fill_u(entry):
    if entry.get() == "":
        entry.configure(foreground = "#BFEFFF")
        entry.insert(0, "Username")
    else:
        pass
def fill_p(entry):
    if entry.get() == "":
        entry.configure(foreground = "#BFEFFF")
        entry.config(show = "")
        entry.insert(0, "Password")
    else:
        pass
def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")
   
def login():
    mainWindow.mainWindow()

class loginWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("Excrucia Inc.")
        self.root.geometry("640x730")
        self.root.minsize(640, 730)
        self.root.maxsize(640, 730)
            
        self.bg = PhotoImage(file = "loginbackground.png")
            
        self.canvas = Canvas(self.root, width = 640, height = 730)
        self.canvas.pack(fill = "both", expand = True)
            
        self.canvas.create_image(0, 0, image = self.bg, anchor = "nw")
            
        self.entry1 = Entry(self.root, bg = "#87CEFA", fg ="#BFEFFF", font = ("Arial Bold", 18), width = 15)
        self.entry1.insert(0, "Username")
        self.canvas.create_window(320, 250, window = self.entry1)
        self.entry2 = Entry(self.root, bg = "#87CEFA", fg ="#BFEFFF", font = ("Arial Bold", 18), width = 15)
        self.entry2.insert(0, "Password")
        self.canvas.create_window(320, 310, window = self.entry2)
            
        self.entry1.bind("<FocusIn>", lambda event: clear_u(self.entry1))
        self.entry1.bind("<FocusOut>", lambda event: fill_u(self.entry1))
            
        self.entry2.bind("<FocusIn>", lambda event: clear_p(self.entry2))
        self.entry2.bind("<FocusOut>", lambda event: fill_p(self.entry2))
            
        self.loginB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), 
                             text ="Login", command = self.login)
        self.loginB.bind('<Enter>', lambda event: on_enter(self.loginB))
        self.loginB.bind('<Leave>', lambda event: on_leave(self.loginB))
        self.canvas.create_window(320, 420, window = self.loginB)
            
        self.var = IntVar()
        self.showP = Checkbutton(self.root, fg = "#1E90FF", bg = "#87CEFF", text = "Show password", font = ("Arial Bold", 12), variable = self.var, onvalue = 1, offvalue = 0, 
                                command = self.showPassword, activeforeground = "#1E90FF", activebackground = "#87CEFF")
        self.canvas.create_window(320, 360, window = self.showP)
        
        self.root.mainloop()
        
    def showPassword(self):
        if (self.var.get() == 1):
            self.entry2.config(show = "")
        if (self.var.get() == 0) and (self.entry2.get() != "Password"):
            self.entry2.config(show = "*")
        
    def login(self):
        with open("src/data/empData/accounts.txt", "rb+") as f:
            data = pickle.loads(f.read())
        accountIndex = utils.find(data,"email",self.entry1.get())
        if((accountIndex==-1)or(not data[accountIndex]["password"] == self.entry2.get())):
            self.canvas.create_text(320, 180, text = "Invalid credentials", font = ("Arial", 18), fill = "red")
        else:           
            with open("src\data\empData\empData.txt", "r+") as f:
                userData = json.loads(f.read()) 
                currentUserData = userData[utils.find(userData,"email",self.entry1.get())]
                currentUserData["password"] = data[accountIndex]["password"]
            with open("src\data\empData\currentUser.txt", "wb+") as f:
                serData = pickle.dumps(currentUserData)
                f.write(serData)
            command = self.root.destroy()
            mw = mainWindow.mainWindow()
    
if __name__ == "__main__":
    loginWindow()