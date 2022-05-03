from tkinter import *

def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")
    
class editDepWindow():
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
        self.text2 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Name:", font = ("Arial Bold", 16))
        self.canvas.create_window(84, 100, window = self.text2)
        self.text3 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Employees number:", font = ("Arial Bold", 16))
        self.canvas.create_window(153, 150, window = self.text3)
        self.text4 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Entry salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(137, 200, window = self.text4)
        self.text5 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Junior salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(143, 250, window = self.text5)
        self.text6 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Senior salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(142, 300, window = self.text6)
        self.text7 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Leader salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(145, 350, window = self.text7)
        self.text8 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Manager salary rate:", font = ("Arial Bold", 16))
        self.canvas.create_window(153, 400, window = self.text8)

        self.entry2 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(450, 100, window = self.entry2)
        self.entry3 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(450, 150, window = self.entry3)
        self.entry4 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(450, 200, window = self.entry4)
        self.entry5 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(450, 250, window = self.entry5)
        self.entry6 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(450, 300, window = self.entry6)
        self.entry7 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(450, 350, window = self.entry7)
        self.entry8 = Entry(self.root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        self.canvas.create_window(450, 400, window = self.entry8)
        
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
        
        self.cancelB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Cancel", 
                         width = 13, command = self.root.destroy)
        self.cancelB.bind('<Enter>', lambda event: on_enter(self.cancelB))
        self.cancelB.bind('<Leave>', lambda event: on_leave(self.cancelB))
        self.canvas.create_window(325, 680, window = self.cancelB)
        
        #Need more codes to import data

#if __name__ == "__main__":
#    editDepWindow()