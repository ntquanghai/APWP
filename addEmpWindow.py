from tkinter import *
#import employee
#import depLeader
#import manager
#import executive
#import department

options = [
    "Marketing",
    "IT",
    "Finance",
    "HR",
    "Operations",
    "Executives"
]

def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")
    
class addWindow():
    def __init__(self):
        self.root = Toplevel()
        
        self.root.title("Excrucia Inc.")
        self.root.geometry("640x750")
        self.root.minsize(640, 750)
        self.root.maxsize(640, 750)
        
        self.bg = PhotoImage(file = "addbackground.png")
        
        self.canvas = Canvas(self.root, width = 640, height = 750)
        self.canvas.pack(fill = "both", expand = True)
        
        self.canvas.create_image(0, 0, image = self.bg, anchor = "nw")
        
        self.text1 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "ID:", font = ("Arial Bold", 16))
        self.canvas.create_window(40, 80, window = self.text1)
        self.text2 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "First Name:", font = ("Arial Bold", 16))
        self.canvas.create_window(84, 140, window = self.text2)
        self.text3 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Last Name:", font = ("Arial Bold", 16))
        self.canvas.create_window(84, 200, window = self.text3)
        self.text4 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Date of birth:", font = ("Arial Bold", 16))
        self.canvas.create_window(92, 260, window = self.text4)
        self.text5 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Salary:", font = ("Arial Bold", 16))
        self.canvas.create_window(61, 320, window = self.text5)
        self.text6 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Position:", font = ("Arial Bold", 16))
        self.canvas.create_window(71, 380, window = self.text6)
        self.text7 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Department:", font = ("Arial Bold", 16))
        self.canvas.create_window(89, 440, window = self.text7)
        
        self.entry1 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(350, 80, window = self.entry1)
        self.entry2 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(350, 140, window = self.entry2)
        self.entry3 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(350, 200, window = self.entry3)
        self.entry4 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(350, 260, window = self.entry4)
        self.entry5 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(350, 320, window = self.entry5)
        self.entry6 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(350, 380, window = self.entry6)
        
        self.clicked = StringVar()
        self.clicked.set("Marketing")
        self.drop = OptionMenu(self.root, self.clicked, *options, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20 )
        self.canvas.create_window(350, 440, window = self.drop)
        
        self.addB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Add", 
                      width = 15, command = self.add)
        self.addB.bind('<Enter>', lambda event: on_enter(self.addB))
        self.addB.bind('<Leave>', lambda event: on_leave(self.addB))
        self.canvas.create_window(200, 600, window = self.addB)
        
        
        self.cancelB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Cancel", 
                         width = 15, command = self.root.destroy)
        self.cancelB.bind('<Enter>', lambda event: on_enter(self.cancelB))
        self.cancelB.bind('<Leave>', lambda event: on_leave(self.cancelB))
        self.canvas.create_window(500, 600, window = self.cancelB)
        
        self.root.mainloop()
    
    def add(self):
        self.entry1.get()
        
#if __name__ == "__main__":
#    addWindow()