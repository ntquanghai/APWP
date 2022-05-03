from tkinter import *
from turtle import bgcolor
import addUserWindow
import os
import json
import pickle
import src.domains.utils as utils
from src.domains.employee import Employee
from tkcalendar import DateEntry
from tkinter.messagebox import askyesno

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

def getDep(input):
    strInput = str(input)
    if(strInput == "Information Technology"):
        return "it"
    elif(strInput == "Marketing"):
        return "marketing"
    elif(strInput == "Finances"):
        return "finance"
    elif(strInput == "Human Resources"):
        return "hr"
    elif(strInput == "Operations"):
        return "operations"

def addEmp(firstName, lastName, dob, pos, dep, canvas):
    if((not firstName.get().isalpha()) or (not lastName.get().isalpha()) or (pos == "Select a position") or (dep == "Select a department")):
        canvas.create_text(320, 400,text = "Invalid credentials.", font = ("Arial Bold", 20), fill = "red")
    else:
        answer = askyesno(title = "Confirmation", message = "Are you sure about the submission?")
        if answer:
            if((not os.path.exists("src\data\empData\empData.txt")) or (os.path.getsize("src\data\empData\empData.txt")==0)):
                with open('src\data\empData\empData.txt', 'w+') as f:
                    wrapper = []
                    currData = {}
                    name = firstName.get() + " " + lastName.get()
                    email = utils.emailName(name)+"."+"er-1"+"@gmail.com"
                    salary = Employee.getSalary(dep, pos)
                    pic = Employee("ER-1",name,dob,email,pos,salary,dep)
                    currData["name"] = pic.name
                    currData["id"] = pic.id
                    currData["dob"] = pic.dob
                    currData["email"] = pic.email
                    currData["pos"] = pic.pos
                    currData["salary"] = pic.salary
                    currData["dep"] = pic.dep
                    wrapper.append(currData)
                    f.write(json.dumps(wrapper))
            else:
                with open('src\data\empData\empData.txt', 'r+') as f:
                    picData = json.loads(f.read())
                    id = "ER-"+str(utils.getIdNum(picData[-1]["id"])+1)
                    name = firstName.get() + " " + lastName.get()
                    email = utils.emailName(name)+"."+id.lower()+"@gmail.com"
                    salary = Employee.getSalary(dep, pos)
                    pic = Employee(id,name,dob,email,pos,salary,dep)
                    currData = {}
                    currData["name"] = pic.name
                    currData["id"] = pic.id
                    currData["dob"] = pic.dob
                    currData["email"] = pic.email
                    currData["pos"] = pic.pos
                    currData["salary"] = pic.salary
                    currData["dep"] = pic.dep
                    picData.append(currData)
                    print(picData)
                with open('src\data\empData\empData.txt', 'w+') as f:
                    f.write(json.dumps(utils.sortListInDict(picData,"id")))


def addWindow():
    root = Toplevel()
    
    root.title("Excrucia Inc.")
    root.geometry("640x750")
    root.minsize(640, 750)
    root.maxsize(640, 750)
    
    bg = PhotoImage(file = "addbackground.png")
    
    canvas = Canvas(root, width = 640, height = 750)
    canvas.pack(fill = "both", expand = True)
    
    canvas.create_image(0, 0, image = bg, anchor = "nw")
    
    canvas.create_text(84, 80, text = "First Name:", font = ("Arial Bold", 16), fill = "black")
    canvas.create_text(84, 140, text = "Last Name:", font = ("Arial Bold", 16), fill = "black")
    canvas.create_text(92, 200, text = "Date of birth:", font = ("Arial Bold", 16), fill = "black")
    canvas.create_text(70, 260, text = "Position:", font = ("Arial Bold", 16), fill = "black")
        
    entry1 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial", 16), width = 20, borderwidth= 1)
    canvas.create_window(350, 80, window = entry1)
    entry2 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial", 16), width = 20, borderwidth= 1)
    canvas.create_window(350, 140, window = entry2)
    entry3 = DateEntry(root, selectmode="day", date_pattern="dd/mm/yyyy")
    entry3.configure(background="#87CEFA", font = ("Arial", 16), width = 18, borderwidth= 1)
    canvas.create_window(350, 200, window = entry3)
    value_inside4 = StringVar(root)
    value_inside4.set("Select a position")
    optionsList = ["Entry", "Junior","Senior"]
    entry4 = OptionMenu(root, value_inside4, *optionsList)
    entry4.configure(background="#87CEFA", activebackground="#87CEFA", highlightthickness=0, border = 1, font = ("Arial", 16), width = 20, indicatoron=0, padx = 0, borderwidth= 1)
    canvas.create_window(350, 260, window = entry4)

    addB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Add", 
                  width = 15)
    addB.bind('<Enter>', lambda event: on_enter(addB))
    with open('src\data\empData\currentUser.txt', 'rb+') as f:
        data = pickle.loads(f.read())
    if(data["pos"] == "manager" or data["pos"] == "executive"):
        canvas.create_text(88, 320, text = "Department:" , font = ("Arial Bold", 16), fill = "black" )
        value_inside7 = StringVar(root)
        value_inside7.set("Select a department")
        optionsList = ["Finances", "Human Resources","Information Technology", "Marketing", "Operations"]
        entry7 = OptionMenu(root, value_inside7, *optionsList)
        entry7.configure(background="#87CEFA", activebackground="#87CEFA", highlightthickness=0, border = 1, font = ("Arial", 16), width = 20, indicatoron=0, padx = 0, borderwidth= 1)
        canvas.create_window(350, 320, window = entry7)
        addB.bind('<Button-1>', lambda event: addEmp(entry1, entry2, str(entry3.get_date()), value_inside4.get().lower(), getDep(value_inside7.get()), canvas))
    else: 
        addB.bind('<Button-1>', lambda event: addEmp(entry1, entry2, str(entry3.get_date()), value_inside4.get().lower(), data["dep"], canvas))
        pass
    addB.bind('<Leave>', lambda event: on_leave(addB))
    canvas.create_window(160, 600, window = addB)
    
    cancelB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Cancel", 
                     width = 15, command = root.destroy)
    cancelB.bind('<Enter>', lambda event: on_enter(cancelB))
    cancelB.bind('<Leave>', lambda event: on_leave(cancelB))
    canvas.create_window(480, 600, window = cancelB)
    
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
    
if __name__ == "__main__":
   addWindow()
