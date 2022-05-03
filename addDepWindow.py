from tkinter import *

def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")
def add():
    pass



def addWindow():
    root = Toplevel()
    
    root.title("Excrucia Inc.")
    root.geometry("640x730")
    root.minsize(640, 750)
    root.maxsize(640, 750)
    
    bg = PhotoImage(file = "addbackground.png")
    
    canvas = Canvas(root, width = 640, height = 750)
    canvas.pack(fill = "both", expand = True)
    
    canvas.create_image(0, 0, image = bg, anchor = "nw")
    
    text1 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "ID:", font = ("Arial Bold", 16))
    canvas.create_window(40, 80, window = text1)
    text2 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "Name:", font = ("Arial Bold", 16))
    canvas.create_window(59, 140, window = text2)
    text3 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "Entry salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(112, 200, window = text3)
    text4 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "Junior salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(118, 260, window = text4)
    text5 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "Senior salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(118, 320, window = text5)
    text6 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "Leader salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(121, 380, window = text6)
    text7 = Label(root, bg = "#87CEFA", fg = "#FFFFFF", text = "Manager salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(129, 440, window = text7)
    
    entry1 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(400, 80, window = entry1)
    entry2 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(400, 140, window = entry2)
    entry3 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(400, 200, window = entry3)
    entry4 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(400, 260, window = entry4)
    entry5 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(400, 320, window = entry5)
    entry6 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(400, 380, window = entry6)
    entry7 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(400, 440, window = entry7)
    
    addB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Add", 
                  width = 15, command = add)
    addB.bind('<Enter>', lambda event: on_enter(addB))
    addB.bind('<Leave>', lambda event: on_leave(addB))
    canvas.create_window(200, 600, window = addB)
    
    cancelB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Cancel", 
                     width = 15, command = root.destroy)
    cancelB.bind('<Enter>', lambda event: on_enter(cancelB))
    cancelB.bind('<Leave>', lambda event: on_leave(cancelB))
    canvas.create_window(500, 600, window = cancelB)
    
    root.mainloop()

#if __name__ == "__main__":
#    addWindow()