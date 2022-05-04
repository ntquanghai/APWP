from tkinter import *
from turtle import bgcolor
import os
import json
import pickle
import src.domains.utils as utils
from src.domains.employee import Employee
from tkcalendar import DateEntry
from tkinter.messagebox import askyesno


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
                    salary = Employee.getSalary(getDep(dep), getPos(pos))
                    currData["name"] = name
                    currData["id"] = "ER-1"
                    currData["dob"] = dob
                    currData["email"] = email
                    currData["pos"] = getPos(pos.lower())
                    currData["salary"] = salary
                    currData["dep"] = dep
                    wrapper.append(currData)
                    f.write(json.dumps(wrapper))
                    updateEmpNum(dep)
                if(currData["pos"]=="leader" or currData["pos"]=="manager" or currData["pos"]=="executive"):
                    with open("src/data/empData/accounts.txt", "wb+") as f:
                        data = []
                        accInfo = {
                            "email": email,
                            "password": utils.emailName(name)+dob.replace("/","")
                        }
                        data.append(accInfo)
                        serData = pickle.dumps(data)
                        f.write(serData)
            else:
                with open('src\data\empData\empData.txt', 'r+') as f:
                    picData = json.loads(f.read())
                    id = "ER-"+str(utils.getIdNum(picData[-1]["id"])+1)
                    name = firstName.get() + " " + lastName.get()
                    email = utils.emailName(name)+"."+id.lower()+"@gmail.com"
                    salary = Employee.getSalary(getDep(dep), getPos(pos))
                    currData = {}
                    currData["name"] = name
                    currData["id"] = id
                    currData["dob"] = dob
                    currData["email"] = email
                    currData["pos"] = getPos(pos.lower())
                    currData["salary"] = salary
                    currData["dep"] = dep
                    picData.append(currData)
                    updateEmpNum(dep)
                with open('src\data\empData\empData.txt', 'w+') as f:
                    f.write(json.dumps(utils.sortListInDict(picData,"id")))
                if(currData["pos"]=="leader" or currData["pos"]=="manager" or currData["pos"]=="executive"):
                    with open("src/data/empData/accounts.txt", "rb+") as f:
                        data = pickle.loads(f.read())
                    with open("src/data/empData/accounts.txt", "wb+") as f:
                        accInfo = {
                            "email": email,
                            "password": utils.emailName(name)+dob.replace("/","")
                        }
                        data.append(accInfo)
                        serData = pickle.dumps(data)
                        f.write(serData)

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
    

    addB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Add", 
                  width = 15)
    addB.bind('<Enter>', lambda event: on_enter(addB))
    with open('src\data\empData\currentUser.txt', 'rb+') as f:
        data = pickle.loads(f.read())
    if(data["pos"] == "manager" or data["pos"] == "executive"):
        if(data["pos"] == "manager"): 
            value_inside4 = StringVar(root)
            value_inside4.set("Select a position")
            optionsList = ["Entry", "Junior","Senior","Leader"]
            entry4 = OptionMenu(root, value_inside4, *optionsList)
            entry4.configure(background="#87CEFA", activebackground="#87CEFA", highlightthickness=0, border = 1, font = ("Arial", 16), width = 20, indicatoron=0, padx = 0, borderwidth= 1)
            canvas.create_window(350, 260, window = entry4)
            canvas.create_text(88, 320, text = "Department:" , font = ("Arial Bold", 16), fill = "black" )
            value_inside7 = StringVar(root)
            value_inside7.set("Select a department")
            optionsList = depList("src\data\depData")
            entry7 = OptionMenu(root, value_inside7, *optionsList)
            entry7.configure(background="#87CEFA", activebackground="#87CEFA", highlightthickness=0, border = 1, font = ("Arial", 16), width = 20, indicatoron=0, padx = 0, borderwidth= 1)
            canvas.create_window(350, 320, window = entry7)
            addB.bind('<Button-1>', lambda event: addEmp(entry1, entry2, str(entry3.get_date()), value_inside4.get().lower(), getDep(value_inside7.get()), canvas))
        elif(data["pos"] == "executive"):
            value_inside4 = StringVar(root)
            value_inside4.set("Select a position")
            optionsList = ["Entry", "Junior","Senior","Leader","Manager"]
            entry4 = OptionMenu(root, value_inside4, *optionsList)
            entry4.configure(background="#87CEFA", activebackground="#87CEFA", highlightthickness=0, border = 1, font = ("Arial", 16), width = 20, indicatoron=0, padx = 0, borderwidth= 1)
            canvas.create_window(350, 260, window = entry4)
            canvas.create_text(88, 320, text = "Department:" , font = ("Arial Bold", 16), fill = "black" )
            value_inside7 = StringVar(root)
            value_inside7.set("Select a department")
            optionsList = depList("src\data\depData")
            entry7 = OptionMenu(root, value_inside7, *optionsList)
            entry7.configure(background="#87CEFA", activebackground="#87CEFA", highlightthickness=0, border = 1, font = ("Arial", 16), width = 20, indicatoron=0, padx = 0, borderwidth= 1)
            canvas.create_window(350, 320, window = entry7)
            addB.bind('<Button-1>', lambda event: addEmp(entry1, entry2, str(entry3.get_date()), value_inside4.get().lower(), getDep(value_inside7.get()), canvas))
    else:
        value_inside4 = StringVar(root)
        value_inside4.set("Select a position")
        optionsList = ["Entry", "Junior","Senior"]
        entry4 = OptionMenu(root, value_inside4, *optionsList)
        entry4.configure(background="#87CEFA", activebackground="#87CEFA", highlightthickness=0, border = 1, font = ("Arial", 16), width = 20, indicatoron=0, padx = 0, borderwidth= 1)
        canvas.create_window(350, 260, window = entry4)
        addB.bind('<Button-1>', lambda event: addEmp(entry1, entry2, str(entry3.get_date()), value_inside4.get().lower(), data["dep"], canvas))
        pass
    addB.bind('<Leave>', lambda event: on_leave(addB))
    canvas.create_window(160, 600, window = addB)
    
    cancelB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 18), text ="Cancel", 
                     width = 15, command = root.destroy)
    cancelB.bind('<Enter>', lambda event: on_enter(cancelB))
    cancelB.bind('<Leave>', lambda event: on_leave(cancelB))
    canvas.create_window(480, 600, window = cancelB)
    root.mainloop()
if __name__ == "__main__":
   addWindow()
