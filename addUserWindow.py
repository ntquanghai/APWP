from tkinter import *

def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")
def add():
    pass











def addUserWindow():
    root = Toplevel()
    root.title("Excrucia Inc.")
    root.geometry("300x300")
    root.minsize(500, 300)
    root.maxsize(500, 300)
    
    bg = PhotoImage(file = "inituserbackground.png")
    
    canvas = Canvas(root, width = 500, height = 300)
    canvas.pack(fill = "both", expand = True)
    
    canvas.create_image(0, 0, image = bg, anchor = "nw")
    
    text2 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "Username:", font = ("Arial Bold", 12))
    canvas.create_window(80, 50, window = text2)
    text3 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "Password:", font = ("Arial Bold", 12))
    canvas.create_window(79, 100, window = text3)
    text4 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "Confirm Password:", font = ("Arial Bold", 12))
    canvas.create_window(112, 150, window = text4)
    
    entry1 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 18)
    canvas.create_window(350, 50, window = entry1)
    entry2 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 18)
    canvas.create_window(350, 100, window = entry2)
    entry3 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 18)
    canvas.create_window(350, 150, window = entry3)
    
    addB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 14), text ="Add", 
                  width = 10, command = add)
    addB.bind('<Enter>', lambda event: on_enter(addB))
    addB.bind('<Leave>', lambda event: on_leave(addB))
    canvas.create_window(150, 225, window = addB)
    
    cancelB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 14), text ="Cancel", 
                     width = 10, command = root.destroy)
    cancelB.bind('<Enter>', lambda event: on_enter(cancelB))
    cancelB.bind('<Leave>', lambda event: on_leave(cancelB))
    canvas.create_window(350, 225, window = cancelB)
    
    root.mainloop()

#if __name__ == "__main__":
#    addUserWindow()