from tkinter import *

def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")
   
def displayInfo(Toplevel, canvas):
    text2 = Label(Toplevel, bg = "#87CEFA", fg = "#FFFFFF", text = "Name:", font = ("Arial Bold", 16))
    canvas.create_window(84, 100, window = text2)
    text3 = Label(Toplevel, bg = "#87CEFA", fg = "#FFFFFF", text = "Employees number:", font = ("Arial Bold", 16))
    canvas.create_window(153, 150, window = text3)
    text4 = Label(Toplevel, bg = "#87CEFA", fg = "#FFFFFF", text = "Entry salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(137, 200, window = text4)
    text5 = Label(Toplevel, bg = "#87CEFA", fg = "#FFFFFF", text = "Junior salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(143, 250, window = text5)
    text6 = Label(Toplevel, bg = "#87CEFA", fg = "#FFFFFF", text = "Senior salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(142, 300, window = text6)
    text7 = Label(Toplevel, bg = "#87CEFA", fg = "#FFFFFF", text = "Leader salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(145, 350, window = text7)
    text8 = Label(Toplevel, bg = "#87CEFA", fg = "#FFFFFF", text = "Manager salary rate:", font = ("Arial Bold", 16))
    canvas.create_window(153, 400, window = text8)

    entry2 = Entry(Toplevel, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(450, 100, window = entry2)
    entry3 = Entry(Toplevel, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(450, 150, window = entry3)
    entry4 = Entry(Toplevel, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(450, 200, window = entry4)
    entry5 = Entry(Toplevel, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(450, 250, window = entry5)
    entry6 = Entry(Toplevel, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(450, 300, window = entry6)
    entry7 = Entry(Toplevel, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(450, 350, window = entry7)
    entry8 = Entry(Toplevel, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(450, 400, window = entry8)
    
    #Need more codes to import data
    
def editDepWindow():
    root = Toplevel()
    root.title("Excrucia Inc.")
    root.geometry("640x750")
    root.minsize(640, 750)
    root.maxsize(640, 750)
    
    bg = PhotoImage(file = "editbackground.png")
    
    canvas = Canvas(root, width = 640, height = 750)
    canvas.pack(fill = "both", expand = True)
    
    canvas.create_image(0, 0, image = bg, anchor = "nw")
    
    entry0 = Entry(root, bg = "#87CEFA", fg ="#BFEFFF", font = ("Arial Bold", 18), width = 15)
    entry0.insert(0, "Enter ID")
    canvas.create_window(150, 50, window = entry0)
    
    saveB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Save", 
                   width = 13)
    saveB.bind('<Enter>', lambda event: on_enter(saveB))
    saveB.bind('<Leave>', lambda event: on_leave(saveB))
    canvas.create_window(200, 600, window = saveB)
    
    restoreB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Restore", 
                      width = 13)
    restoreB.bind('<Enter>', lambda event: on_enter(restoreB))
    restoreB.bind('<Leave>', lambda event: on_leave(restoreB))
    canvas.create_window(450, 600, window = restoreB)
    
    cancelB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Cancel", 
                     width = 13, command = root.destroy)
    cancelB.bind('<Enter>', lambda event: on_enter(cancelB))
    cancelB.bind('<Leave>', lambda event: on_leave(cancelB))
    canvas.create_window(325, 680, window = cancelB)
    
    displayInfo(root, canvas)
    
    root.mainloop()

#Delete codes below after connect all windows
if __name__ == "__main__":
    editDepWindow()