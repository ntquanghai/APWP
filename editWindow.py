from tkinter import *

def displayInfo(Tk, canvas):
    text2 = Label(Tk, bg = "#87CEFA", fg = "#FFFFFF", text = "First Name:", font = ("Arial Bold", 16))
    canvas.create_window(84, 140, window = text2)
    text3 = Label(Tk, bg = "#87CEFA", fg = "#FFFFFF", text = "Last Name:", font = ("Arial Bold", 16))
    canvas.create_window(84, 200, window = text3)
    text4 = Label(Tk, bg = "#87CEFA", fg = "#FFFFFF", text = "Date of birth:", font = ("Arial Bold", 16))
    canvas.create_window(92, 260, window = text4)
    text5 = Label(Tk, bg = "#87CEFA", fg = "#FFFFFF", text = "Phone:", font = ("Arial Bold", 16))
    canvas.create_window(63, 320, window = text5)
    text6 = Label(Tk, bg = "#87CEFA", fg = "#FFFFFF", text = "Salary:", font = ("Arial Bold", 16))
    canvas.create_window(61, 380, window = text6)
    text7 = Label(Tk, bg = "#87CEFA", fg = "#FFFFFF", text = "Shift:", font = ("Arial Bold", 16))
    canvas.create_window(53, 440, window = text7)
    
    #Need more codes to import data
    
    entry2 = Entry(Tk, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 140, window = entry2)
    entry3 = Entry(Tk, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 200, window = entry3)
    entry4 = Entry(Tk, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 260, window = entry4)
    entry5 = Entry(Tk, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 320, window = entry5)
    entry6 = Entry(Tk, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 380, window = entry6)
    entry7 = Entry(Tk, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 440, window = entry7)
    
def editWindow():
    root = Tk()
    root.title("Excrucia Inc.")
    root.geometry("640x730")
    root.minsize(640, 730)
    root.maxsize(640, 730)
    
    bg = PhotoImage(file = "otherbackground.png")
    
    canvas = Canvas(root, width = 640, height = 750)
    canvas.pack(fill = "both", expand = True)
    
    canvas.create_image(0, 0, image = bg, anchor = "nw")
    
    entry0 = Entry(root, bg = "#87CEFA", fg ="#BFEFFF", font = ("Arial Bold", 18), width = 15)
    entry0.insert(0, "Enter ID")
    canvas.create_window(150, 50, window = entry0)
    
    displayInfo(root, canvas)
    
    root.mainloop()

#Delete codes below after connect all windows
if __name__ == "__main__":
    editWindow()