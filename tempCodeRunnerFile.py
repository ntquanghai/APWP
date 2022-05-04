from tkinter import *
import os
import json
import pickle
import tkinter.messagebox as tkm


def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")

def getPos(input):
    if(input.lower() == "junior"):
        return "jr"
    elif(input.lower() == "sernior"):
        return "sr"

def depList(directory):
   depArr = []
   for filename in os.listdir(directory):
      f = os.path.join(directory, filename)
      if os.path.isfile(f):
        with open(f, 'r+') as r:
            data = json.loads(r.read())
        depArr.append(data["name"])
   return depArr

def getDep(input):
    abrv = ""
    strInput = str(input)
    if(not " " in strInput):
        return strInput.lower()
    else:
        for i in range(0, len(strInput)):
            if(i==0):
                abrv = abrv + strInput[i]
            if(strInput[i]==" "):
                abrv = abrv + strInput[i+1]
        return(abrv.lower())

def updateEmpNum(dep):
    with open("src\data\empData\empData.txt", "r+") as f:
        data = json.loads(f.read())
    empNum = 0
    for i in range(0, len(data)):
        if(data[i]["dep"].lower() == dep):
            empNum = empNum + 1
    with open("src\data\depData/"+dep.lower()+".txt", "r+") as f:
        depData = json.loads(f.read())
        depData["empNumber"]= empNum
    with open("src\data\depData/"+dep.lower()+".txt", "w+") as f:
        f.write(json.dumps(depData))


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
        self.entry0.insert(0, "Enter department name")
        self.canvas.create_window(150, 50, window = self.entry0)
        
        self.displayInfo()
        
        self.root.mainloop()
    
    def displayInfo(self):
        self.canvas.create_text(84,100, text = "Name:", font = ("Arial Bold", 16), fill = "black")
        self.canvas.create_text(153,150, text = "Employees number:", font = ("Arial Bold", 16), fill = "black")
        self.canvas.create_text(137,200, text = "Entry salary rate:", font = ("Arial Bold", 16), fill = "black")
        self.canvas.create_text(143,250, text = "Junior salary rate:", font = ("Arial Bold", 16), fill = "black")
        self.canvas.create_text(142,300, text = "Senior salary rate:", font = ("Arial Bold", 16), fill = "black")
        self.canvas.create_text(145,350, text = "Leader salary rate:", font = ("Arial Bold", 16), fill = "black")
        self.canvas.create_text(153,400, text = "Manager salary rate:", font = ("Arial Bold", 16), fill = "black")

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

        def searchByName(root, searchedName):
            listofdep = depList("src\data\depData")
            flag = True
            print(searchedName)
            for i in range(0,len(listofdep)):
                print(listofdep)
                if(searchedName.capitalize() in listofdep):
                    self.entry2.insert(0,listofdep[i]["name"])
                    self.entry3.insert(0,updateEmpNum(self.entry2.get().lower()))
                    self.entry4.insert(0,listofdep[i]["salaryRate"]["entry"])
                    self.entry5.insert(0,listofdep[i]["salaryRate"]["jr"])
                    self.entry6.insert(0,listofdep[i]["salaryRate"]["sr"])
                    self.entry7.insert(0,listofdep[i]["salaryRate"]["leader"])
                    self.entry8.insert(0,listofdep[i]["salaryRate"]["manager"])
                else:
                    tkm.showerror(title="Error", message = "Invalid name")
                    break
                

        def saveData(root):
            answer = tkm.askyesno(title="Adding Department", message = "Are you sure you want to add this department?")
            if answer:
                if((not os.path.exists("src\data\depData/"+self.entry1.get().lower()+".txt")) or (os.path.getsize("src\data\depData/"+self.entry1.get().lower()+".txt")==0)):
                    with open("src\data\depData/"+self.entry1.get().lower()+".txt", "w+") as f:
                        tempDict = {
                            "name": self.entry2.get().capitalize(),
                            "empNumber": updateEmpNum(self.entry2.get().lower()),
                            "salaryRate": {
                                "entry": "$"+self.entry4.get()+"/hr",
                                "jr": "$"+self.entry5.get()+"/hr",
                                "sr": "$"+self.entry6.get()+"/hr",
                                "leader": "$"+self.entry7.get()+"/hr",
                                "manager": "$"+self.entry8.get()+"/hr"
                            }
                        }
                        f.write(json.dumps(tempDict))
                        tkm.showinfo(title = "Successful", message = "Department added!")
                else:
                    with open("src\data\depData/"+self.entry1.get().lower()+".txt", "r+") as f:
                        depData = json.loads(f.read())
                    with open("src\data\depData/"+self.entry1.get().lower()+".txt", "w+") as f:
                        depData["name"] = self.entry2.get().capitalize(),
                        depData["empNumber"] = updateEmpNum(self.entry2.get().lower()),
                        depData["salaryRate"] = {
                            "entry": "$"+self.entry3.get()+"/hr",
                            "jr": "$"+self.entry4.get()+"/hr",
                            "sr": "$"+self.entry5.get()+"/hr",
                            "leader": "$"+self.entry6.get()+"/hr",
                            "manager": "$"+self.entry7.get()+"/hr"
                        }
                        f.write(json.dumps(depData))
                        tkm.showinfo(title = "Successful", message = "Department added!")
            root.destroy() 
        
        self.saveB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Search", 
                       width = 13)
        self.saveB.bind('<Enter>', lambda event: on_enter(self.saveB))
        self.saveB.bind('<Button-1>', lambda event: searchByName(self.root,self.entry2.get()))
        self.saveB.bind('<Leave>', lambda event: on_leave(self.saveB))
        self.canvas.create_window(200, 600, window = self.saveB)
        
        self.restoreB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Save", 
                          width = 13)
        self.restoreB.bind('<Enter>', lambda event: on_enter(self.restoreB))
        self.restoreB.bind('<Button-1>', lambda event: saveData(self.root,self.entry2.get()))
        self.restoreB.bind('<Leave>', lambda event: on_leave(self.restoreB))
        self.canvas.create_window(450, 600, window = self.restoreB)
        
        self.cancelB = Button(self.root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Cancel", 
                         width = 13, command = self.root.destroy)
        self.cancelB.bind('<Enter>', lambda event: on_enter(self.cancelB))
        self.cancelB.bind('<Leave>', lambda event: on_leave(self.cancelB))
        self.canvas.create_window(325, 680, window = self.cancelB)


if __name__ == "__main__":
   editDepWindow()

