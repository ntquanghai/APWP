from tkinter import *
import addEmpWindow
import addDepWindow
import editEmpWindow
import editDepWindow
import loginWindow

def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")
   
def addEmp():
    addEmpWindow.addWindow()
    
def editEmp():
    editEmpWindow.editEmpWindow()
    
def addDep():
    addDepWindow.addWindow()
    
def editDep():
    editDepWindow.editDepWindow()

class mainWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("Excrucia Inc.")
        self.root.geometry("800x800")
        self.root.minsize(800, 600)
        self.root.maxsize(800, 600)
        
        self.bg = PhotoImage(file = "mainbackground.png")
        self.canvas = Canvas(self.root, width = 800, height = 600)
        self.canvas.pack(fill = "both", expand = True)
        
        self.canvas.create_image(0, 0, image = self.bg, anchor = "nw")
        
        self.text1 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Welcome!", font = ("Arial Bold", 28))
        self.canvas.create_window(400, 50, window = self.text1) 
        
        self.addEmpB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), 
                              text ="Add employee",  width = 20, command = addEmp)
        self.addEmpB.bind('<Enter>', lambda event: on_enter(self.addEmpB))
        self.addEmpB.bind('<Leave>', lambda event: on_leave(self.addEmpB))
        self.canvas.create_window(200, 200, window = self.addEmpB)
        
        self.editEmpB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), 
                               text ="View employee info",  width = 20, command = editEmp)
        self.editEmpB.bind('<Enter>', lambda event: on_enter(self.editEmpB))
        self.editEmpB.bind('<Leave>', lambda event: on_leave(self.editEmpB))
        self.canvas.create_window(600, 200, window = self.editEmpB)
        
        self.addDepB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), 
                              text ="Add department", width = 20, command = addDep)
        self.addDepB.bind('<Enter>', lambda event: on_enter(self.addDepB))
        self.addDepB.bind('<Leave>', lambda event: on_leave(self.addDepB))
        self.canvas.create_window(200, 300, window = self.addDepB)
        
        self.editDepB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), 
                               text ="View department info", width = 20, command = editDep)
        self.editDepB.bind('<Enter>', lambda event: on_enter(self.editDepB))
        self.editDepB.bind('<Leave>', lambda event: on_leave(self.editDepB))
        self.canvas.create_window(600, 300, window = self.editDepB)
        
        self.logOutB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), 
                              text ="Log out", width = 20, command = self.logOut)
        self.logOutB.bind('<Enter>', lambda event: on_enter(self.logOutB))
        self.logOutB.bind('<Leave>', lambda event: on_leave(self.logOutB))
        self.canvas.create_window(400, 400, window = self.logOutB)
    
        self.root.mainloop()
    
    def logOut(self):
        command = self.root.destroy()
        lw = loginWindow.loginWindow()
        
#if __name__ == "__main__":
#    mainWindow()