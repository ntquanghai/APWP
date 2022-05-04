from logging import root
from tkinter import *
import json
from os.path import exists
import tkinter.messagebox as tkm
import mainWindow



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
      
      
      self.canvas.create_text(52, 80, text = "Name", font = ("Arial Bold", 16), fill = "black")
      self.canvas.create_text(112, 140, text = "Entry salary rate:", font = ("Arial Bold", 16), fill = "black")
      # self.text3 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Entry salary rate:", font = ("Arial Bold", 16))
      # self.canvas.create_window(112, 200, window = self.text3)
      self.canvas.create_text(118, 200, text = "Junior salary rate: ", font = ("Arial Bold", 16), fill = "black")
      # self.text4 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Junior salary rate:", font = ("Arial Bold", 16))
      # self.canvas.create_window(118, 260, window = self.text4)
      self.canvas.create_text(118, 260, text = "Senior salary rate: ", font = ("Arial Bold", 16), fill = "black")
      # self.text5 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Senior salary rate:", font = ("Arial Bold", 16))
      # self.canvas.create_window(118, 320, window = self.text5)
      self.canvas.create_text(121, 320, text = "Leader salary rate: ", font = ("Arial Bold", 16), fill = "black")
      # self.text6 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Leader salary rate:", font = ("Arial Bold", 16))
      # self.canvas.create_window(121, 380, window = self.text6)
      self.canvas.create_text(129, 380, text = "Manager salary rate: ", font = ("Arial Bold", 16), fill = "black")
      # self.text7 = Label(self.root, bg = "#87CEFA", fg = "#FFFFFF", text = "Manager salary rate:", font = ("Arial Bold", 16))
      # self.canvas.create_window(129, 440, window = self.text7)
      # self.canvas.create_text(129, 440, text = "ID: ", font = ("Arial Bold", 16), fill = "black")
      
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
      def addDep(root):
         if(exists("src\data\depData/"+self.entry1.get().lower()+".txt")):
            tkm.showerror(title="Error", message="Department already exists. Please try again")
         else:
            answer = tkm.askyesno(title="Adding Department", message = "Are you sure you want to add this department?")
            if answer:
               with open("src\data\depData/"+self.entry1.get().lower()+".txt", "w+") as f:
                  tempDict = {
                     "name": self.entry1.get().capitalize(),
                     "empNumber": 0,
                     "salaryRate": {
                        "entry": "$"+self.entry2.get()+"/hr",
                        "jr": "$"+self.entry3.get()+"/hr",
                        "sr": "$"+self.entry4.get()+"/hr",
                        "leader": "$"+self.entry5.get()+"/hr",
                        "manager": "$"+self.entry6.get()+"/hr"
                     }
                  }
                  f.write(json.dumps(tempDict))
               tkm.showinfo(title = "Successful", message = "Department added!")
            root.destroy()
      
      self.addB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Add", 
                     width = 15)
      self.addB.bind('<Enter>', lambda event: on_enter(self.addB))
      self.addB.bind('<Button-1>', lambda event: addDep(self.root))
      self.addB.bind('<Leave>', lambda event: on_leave(self.addB))
      self.canvas.create_window(160, 600, window = self.addB)
      
      self.cancelB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Cancel", 
                        width = 15, command = self.root.destroy)
      self.cancelB.bind('<Enter>', lambda event: on_enter(self.cancelB))
      self.cancelB.bind('<Leave>', lambda event: on_leave(self.cancelB))
      self.canvas.create_window(480, 600, window = self.cancelB)
      
      self.root.mainloop()
            
if __name__ == "__main__":
   addWindow()
