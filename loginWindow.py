from tkinter import *


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
    pass
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   

def showPassword():
    if (var.get() == 1):
        entry2.config(show = "")
    if (var.get() == 0) and (entry2.get() != "Password"):
        entry2.config(show = "*")
def loginWindow():
    root = Tk()
    
    root.title("Excrucia Inc.")
    root.geometry("640x730")
    root.minsize(640, 730)
    root.maxsize(640, 730)
    
    bg = PhotoImage(file = "loginbackground.png")
    
    canvas = Canvas(root, width = 640, height = 730)
    canvas.pack(fill = "both", expand = True)
    
    canvas.create_image(0, 0, image = bg, anchor = "nw")
    
    entry1 = Entry(root, bg = "#87CEFA", fg ="#BFEFFF", font = ("Arial Bold", 18), width = 15)
    entry1.insert(0, "Username")
    canvas.create_window(320, 250, window = entry1)
    entry2 = Entry(root, bg = "#87CEFA", fg ="#BFEFFF", font = ("Arial Bold", 18), width = 15)
    entry2.insert(0, "Password")
    canvas.create_window(320, 310, window = entry2)
    
    entry1.bind("<FocusIn>", lambda event: clear_u(entry1))
    entry1.bind("<FocusOut>", lambda event: fill_u(entry1))
    
    entry2.bind("<FocusIn>", lambda event: clear_p(entry2))
    entry2.bind("<FocusOut>", lambda event: fill_p(entry2))
    
    loginB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", font = ("Arial Bold", 18), text ="Login", command = login)
    loginB.bind('<Enter>', lambda event: on_enter(loginB))
    loginB.bind('<Leave>', lambda event: on_leave(loginB))
    canvas.create_window(320, 420, window = loginB)
    
    var = IntVar()
    showP = Checkbutton(root, fg = "#1E90FF", bg = "#87CEFF", text = "Show password", font = ("Arial Bold", 12), variable = var, onvalue = 1, offvalue = 0, 
                        command = showPassword, activeforeground = "#1E90FF", activebackground = "#87CEFF")
    canvas.create_window(320, 360, window = showP)
    
    root.mainloop()

if __name__ == "__main__":
    loginWindow()