from tkinter import *

def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")

class addWindow():
    def __init__(self):
        self.root = Toplevel()
        
        self.root.title("Excrucia Inc.")
        self.root.geometry("640x730")
        self.root.minsize(640, 750)
        self.root.maxsize(640, 750)
        
        self.bg = PhotoImage(file = "addbackground.png")
        
        self.canvas = Canvas(self.root, width = 640, height = 750)
        self.canvas.pack(fill = "both", expand = True)
        
        self.canvas.create_image(0, 0, image = self.bg, anchor = "nw")
        
        self.text1 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "ID:", font = ("Arial Bold", 16))
        self.canvas.create_window(40, 80, window = self.text1)
        self.text2 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Name:", font = ("Arial Bold", 16))
        self.canvas.create_window(59, 140, window = self.text2)
        self.text3 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Entry salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(112, 200, window = self.text3)
        self.text4 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Junior salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(118, 260, window = self.text4)
        self.text5 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Senior salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(118, 320, window = self.text5)
        self.text6 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Leader salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(121, 380, window = self.text6)
        self.text7 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Manager salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(129, 440, window = self.text7)
        
        self.entry1 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(400, 80, window = self.entry1)
        self.entry2 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(400, 140, window = self.entry2)
        self.entry3 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(400, 200, window = self.entry3)
        self.entry4 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(400, 260, window = self.entry4)
        self.entry5 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(400, 320, window = self.entry5)
        self.entry6 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(400, 380, window = self.entry6)
        self.entry7 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(400, 440, window = self.entry7)
        
        self.addB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Add", 
                      width = 15, command = add)
        self.addB.bind('<Enter>', lambda event: on_enter(self.addB))
        self.addB.bind('<Leave>', lambda event: on_leave(self.addB))
        self.canvas.create_window(200, 600, window = self.addB)
        
        self.cancelB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Cancel", 
                         width = 15, command = self.root.destroy)
        self.cancelB.bind('<Enter>', lambda event: on_enter(self.cancelB))
        self.cancelB.bind('<Leave>', lambda event: on_leave(self.cancelB))
        self.canvas.create_window(500, 600, window = self.cancelB)
        
        self.self.root.mainloop()
        
        def add(self):
            pass

#if __name__ == "__main__":
#    addWindow()