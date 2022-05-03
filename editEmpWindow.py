from tkinter import *
import addUserWindow

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
    
class editEmpWindow():
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Excrucia Inc.")
        self.root.geometry("640x750")
        self.root.minsize(640, 750)
        self.root.maxsize(640, 750)
        
        self.bg = PhotoImage(file = "editbackground.png")
        
        self.canvas = Canvas(self.root, width = 640, height = 750)
        self.canvas.pack(fill = "both", expand = True)
        
        self.canvas.create_image(0, 0, image = self.bg, anchor = "nw")
        
        self.entry0 = Entry(self.root, bg = "#87CEFA", fg ="#BFEFFF", font = ("Arial Bold", 18), width = 15)
        self.entry0.insert(0, "Enter ID")
        self.canvas.create_window(150, 50, window = self.entry0)
        
        self.displayInfo()
        
        self.root.mainloop()
        
        def displayInfo(self):
            self.text2 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "First Name:", font = ("Arial Bold", 16))
            self.canvas.create_window(84, 100, window = self.text2)
            self.text3 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Last Name:", font = ("Arial Bold", 16))
            self.canvas.create_window(84, 150, window = self.text3)
            self.text4 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Date of birth:", font = ("Arial Bold", 16))
            self.canvas.create_window(92, 200, window = self.text4)
            self.text6 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Email:", font = ("Arial Bold", 16))
            self.canvas.create_window(58, 300, window = self.text6)
            self.text7 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Salary:", font = ("Arial Bold", 16))
            self.canvas.create_window(61, 350, window = self.text7)
            self.text8 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Shift:", font = ("Arial Bold", 16))
            self.canvas.create_window(53, 400, window = self.text8)
            self.text9 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Years:", font = ("Arial Bold", 16))
            self.canvas.create_window(59, 450, window = self.text9)
            self.text10 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Department:", font = ("Arial Bold", 16))
            self.canvas.create_window(89, 500, window = self.text10)
            self.text11 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Position:", font = ("Arial Bold", 16))
            self.canvas.create_window(71, 550, window = self.text11)
            
            #Need more codes to import data
            
            self.entry2 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
            self.canvas.create_window(350, 100, window = self.entry2)
            self.entry3 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
            self.canvas.create_window(350, 150, window = self.entry3)
            self.entry4 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
            self.canvas.create_window(350, 200, window = self.entry4)
            self.entry6 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
            self.canvas.create_window(350, 300, window = self.entry6)
            self.entry7 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
            self.canvas.create_window(350, 350, window = self.entry7)
            self.entry8 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
            self.canvas.create_window(350, 400, window = self.entry8)
            self.entry9 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
            self.canvas.create_window(350, 450, window = self.entry9)
            self.entry10 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
            self.canvas.create_window(350, 500, window = self.entry10)
            
            self.clicked = StringVar()
            self.clicked.set("Marketing")
            self.drop = OptionMenu(self.root, self.clicked, *options, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20 )
            self.canvas.create_window(350, 550, window = self.drop)
            
            self.saveB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Save", 
                           width = 13)
            self.saveB.bind('<Enter>', lambda event: on_enter(self.saveB))
            self.saveB.bind('<Leave>', lambda event: on_leave(self.saveB))
            self.canvas.create_window(200, 600, window = self.saveB)
            
            self.restoreB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Restore", 
                              width = 13)
            self.restoreB.bind('<Enter>', lambda event: on_enter(self.restoreB))
            self.restoreB.bind('<Leave>', lambda event: on_leave(self.restoreB))
            self.canvas.create_window(450, 600, window = self.restoreB)
            
            self.promoteB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Promote", 
                              width = 13)
            self.promoteB.bind('<Enter>', lambda event: on_enter(self.promoteB))
            self.promoteB.bind('<Leave>', lambda event: on_leave(self.promoteB))
            self.canvas.create_window(200, 650, window = self.promoteB)
            
            self.demoteB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Demote", 
                             width = 13)
            self.demoteB.bind('<Enter>', lambda event: on_enter(self.demoteB))
            self.demoteB.bind('<Leave>', lambda event: on_leave(self.demoteB))
            self.canvas.create_window(450, 650, window = self.demoteB)
            
            self.removeB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Remove", 
                             width = 13)
            self.removeB.bind('<Enter>', lambda event: on_enter(self.removeB))
            self.removeB.bind('<Leave>', lambda event: on_leave(self.removeB))
            self.canvas.create_window(200, 700, window = self.removeB)
            
            self.cancelB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Cancel", 
                             width = 13, command = self.root.destroy)
            self.cancelB.bind('<Enter>', lambda event: on_enter(self.cancelB))
            self.cancelB.bind('<Leave>', lambda event: on_leave(self.cancelB))
            self.canvas.create_window(450, 700, window = self.cancelB)

#if __name__ == "__main__":
#    editEmpWindow()