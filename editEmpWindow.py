from posixpath import split
from tkinter import *

from numpy import full
import json
import src.domains.utils as utils
from tkcalendar import DateEntry
from tkinter.messagebox import askyesno
import pickle
import tkinter.messagebox as tkm
from src.domains.employee import Employee
import mainWindow


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
def refresh(root):
    root.destroy()

def splitName(name):
    splitList = name.split()
    firstName = splitList[0]
    lastName = ""
    for i in range(1, len(splitList)):
        lastName = lastName + splitList[i] + " "
    fullName = {"firstName":firstName,"lastName":lastName}
    return fullName

def splitDob(dob):
    day = ""
    month = ""
    year = ""
    count = 0
    for i in range(0, len(dob)):
        if(dob[i] == "-"):
            count = count + 1
        else:
            if(count == 0):
                year = year + dob[i]
            elif(count==1):
                month = month + dob[i]
            elif(count==2):
                day = day + dob[i]
    data = {
        "day": int(day),
        "month": int(month),
        "year": int(year)
    }
    return data

def searchById(canvas, root, searchedId, entry2, entry3, entry5, entry6, entry7, entry8, saveB, entry0):
    with open("src\data\empData\empData.txt","r") as f:
        data = json.loads(f.read())
    empIndex = utils.find(data,"id",searchedId)
    if(empIndex == -1): 
        tkm.showerror("Error","Invalid permission, or the employee does not exist.")
    else:
        searchedEmp = data[empIndex]
        with open("src\data\empData\currentUser.txt", "rb+") as f:
            serData = pickle.loads(f.read())
        if(serData["pos"] == "leader"):
            if(searchedEmp["pos"] == "manager" or searchedEmp["pos"] == "executive" or not (searchedEmp["dep"] == serData["dep"])):
                tkm.showerror(title="Access denied", message="You do not have permission.")
            else:
                entry2.delete(0,len(entry2.get()))
                entry2.insert(0, splitName(searchedEmp["name"])["firstName"])
                entry3.delete(0,len(entry3.get()))
                entry3.insert(0, splitName(searchedEmp["name"])["lastName"])

                day = splitDob(searchedEmp["dob"])["day"]
                month = splitDob(searchedEmp["dob"])["month"]
                year = splitDob(searchedEmp["dob"])["year"]

                entry4 = DateEntry(root, selectmode="day", date_pattern="dd/mm/yyyy", day = day, month =month, year = year)
                entry4.configure(background="#87CEFA", font = ("Arial", 16), width = 18, borderwidth= 1)
                canvas.create_window(350, 200, window = entry4)

                entry5.delete(0,len(entry5.get()))
                entry5.insert(0, searchedEmp["email"])

                entry6.delete(0,len(entry6.get()))
                entry6.insert(0, searchedEmp["salary"])

                entry7.delete(0,len(entry7.get()))
                entry7.insert(0, searchedEmp["dep"])

                entry8.delete(0,len(entry8.get()))
                entry8.insert(0, searchedEmp["pos"].capitalize())

                saveB.bind('<Button-1>', lambda event: saveData(entry0.get(),entry2,entry3,entry4, root))
        elif(serData["pos"]=="manager"):
            if(searchedEmp["pos"] == "executive" or not (searchedEmp["dep"] == serData["dep"])):
                tkm.showerror(title="Access denied", message="You do not have permission.")
            else:
                entry2.delete(0,len(entry2.get()))
                entry2.insert(0, splitName(searchedEmp["name"])["firstName"])
                entry3.delete(0,len(entry3.get()))
                entry3.insert(0, splitName(searchedEmp["name"])["lastName"])

                day = splitDob(searchedEmp["dob"])["day"]
                month = splitDob(searchedEmp["dob"])["month"]
                year = splitDob(searchedEmp["dob"])["year"]

                entry4 = DateEntry(root, selectmode="day", date_pattern="dd/mm/yyyy", day = day, month =month, year = year)
                entry4.configure(background="#87CEFA", font = ("Arial", 16), width = 18, borderwidth= 1)
                canvas.create_window(350, 200, window = entry4)

                entry5.delete(0,len(entry5.get()))
                entry5.insert(0, searchedEmp["email"])

                entry6.delete(0,len(entry6.get()))
                entry6.insert(0, searchedEmp["salary"])

                entry7.delete(0,len(entry7.get()))
                entry7.insert(0, searchedEmp["dep"])

                entry8.delete(0,len(entry8.get()))
                entry8.insert(0, searchedEmp["pos"].capitalize())

                saveB.bind('<Button-1>', lambda event: saveData(entry0.get(),entry2,entry3,entry4, root))
        else:
            entry2.delete(0,len(entry2.get()))
            entry2.insert(0, splitName(searchedEmp["name"])["firstName"])
            entry3.delete(0,len(entry3.get()))
            entry3.insert(0, splitName(searchedEmp["name"])["lastName"])

            day = splitDob(searchedEmp["dob"])["day"]
            month = splitDob(searchedEmp["dob"])["month"]
            year = splitDob(searchedEmp["dob"])["year"]

            entry4 = DateEntry(root, selectmode="day", date_pattern="dd/mm/yyyy", day = day, month =month, year = year)
            entry4.configure(background="#87CEFA", font = ("Arial", 16), width = 18, borderwidth= 1)
            canvas.create_window(350, 200, window = entry4)

            entry5.delete(0,len(entry5.get()))
            entry5.insert(0, searchedEmp["email"])

            entry6.delete(0,len(entry6.get()))
            entry6.insert(0, searchedEmp["salary"])

            entry7.delete(0,len(entry7.get()))
            entry7.insert(0, searchedEmp["dep"])

            entry8.delete(0,len(entry8.get()))
            entry8.insert(0, searchedEmp["pos"].capitalize())

            saveB.bind('<Button-1>', lambda event: saveData(entry0.get(),entry2,entry3,entry4, root))

def saveData(searchedId, firstName, lastName, dob, root):
    with open("src\data\empData\empData.txt","r") as f:
        data = json.loads(f.read())
    empIndex = utils.find(data,"id",searchedId)
    data[empIndex]["name"] = firstName.get() + " " + lastName.get()
    data[empIndex]["dob"] = str(dob.get_date())
    data[empIndex]["email"] = utils.emailName(data[empIndex]["name"])+"."+data[empIndex]["id"].lower()+"@gmail.com"
    with open('src\data\empData\empData.txt', 'w+') as f:
        f.write(json.dumps(utils.sortListInDict(data,"id")))
    tkm.showinfo(title = "Submission sucessful", message = "Employee updated.")
    root.destroy()
    editEmpWindow()

def promote(pos, searchedId, root):
    with open("src\data\empData\currentUser.txt", "rb+") as f:
        serData = pickle.loads(f.read())
    if(serData["pos"] == "leader"):
        if((pos =="Manager") or (pos =="Executive") or (pos=="Leader")):
            tkm.showerror(title = "Access denied", message = "You do not have permission.")
        else:
            flag = tkm.askyesno(title = "Promotion", message = "Are you sure about the promotion?")
            if flag:
                with open("src\data\empData\empData.txt","r") as f:
                    data = json.loads(f.read())
                empIndex = utils.find(data,"id",searchedId)
                if(data[empIndex]["pos"].lower()=="entry"):
                    data[empIndex]["pos"] = "jr"
                    data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
                elif(data[empIndex]["pos"].lower() =="jr"):
                    data[empIndex]["pos"] = "sr"
                    data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
                with open('src\data\empData\empData.txt', 'w+') as f:
                    f.write(json.dumps(utils.sortListInDict(data,"id")))
                tkm.showinfo(title = "Submission sucessful", message = "Employee promoted!")
            root.destroy()
            editEmpWindow()
    elif(serData["pos"] == "executive"):
        flag = tkm.askyesno(title = "Promotion", message = "Are you sure about the promotion?")
        if flag:
            with open("src\data\empData\empData.txt","r") as f:
                data = json.loads(f.read())
            empIndex = utils.find(data,"id",searchedId)
            if(data[empIndex]["pos"].lower()=="entry"):
                data[empIndex]["pos"] = "jr"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() =="jr"):
                data[empIndex]["pos"] = "sr"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() =="sr"):
                data[empIndex]["pos"] = "leader"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() =="leader"):
                data[empIndex]["pos"] = "manager"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() =="manager"):
                data[empIndex]["pos"] = "executive"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            with open('src\data\empData\empData.txt', 'w+') as f:
                f.write(json.dumps(utils.sortListInDict(data,"id")))
            tkm.showinfo(title = "Submission sucessful", message = "Employee promoted!")
        root.destroy()
        editEmpWindow()
    else: 
        flag = tkm.askyesno(title = "Promotion", message = "Are you sure about the promotion?")
        if flag:
            with open("src\data\empData\empData.txt","r") as f:
                data = json.loads(f.read())
            empIndex = utils.find(data,"id",searchedId)
            if(data[empIndex]["pos"].lower()=="entry"):
                data[empIndex]["pos"] = "jr"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() =="jr"):
                data[empIndex]["pos"] = "sr"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() =="sr"):
                data[empIndex]["pos"] = "leader"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() == "leader"):
                data[empIndex]["pos"] = "manager"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            with open('src\data\empData\empData.txt', 'w+') as f:
                f.write(json.dumps(utils.sortListInDict(data,"id")))
            tkm.showinfo(title = "Submission sucessful", message = "Employee promoted!")
        root.destroy()
        editEmpWindow()

def demote(pos, searchedId, root):
    with open("src\data\empData\currentUser.txt", "rb+") as f:
        serData = pickle.loads(f.read())
    if(serData["pos"] == "leader"):
        if((pos =="Manager") or (pos =="Executive") or (pos=="Leader")):
            tkm.showerror(title = "Access denied", message = "You do not have permission.")
        else:
            flag = tkm.askyesno(title = "Demotion", message = "Are you sure about the demotion?")
            if flag:
                with open("src\data\empData\empData.txt","r") as f:
                    data = json.loads(f.read())
                empIndex = utils.find(data,"id",searchedId)
                if(data[empIndex]["pos"].lower()=="jr"):
                    data[empIndex]["pos"] = "entry"
                    data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
                elif(data[empIndex]["pos"].lower() =="sr"):
                    data[empIndex]["pos"] = "jr"
                    data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
                with open('src\data\empData\empData.txt', 'w+') as f:
                    f.write(json.dumps(utils.sortListInDict(data,"id")))
                tkm.showinfo(title = "Submission sucessful", message = "Employee promoted!")
            root.destroy()
            editEmpWindow()
    elif(serData["pos"] == "executive"):
        if(pos == "Executive"):
            tkm.showerror(title = "Access denied", message = "You do not have permission.")
        else:
            flag = tkm.askyesno(title = "Promotion", message = "Are you sure about the promotion?")
            if flag:
                with open("src\data\empData\empData.txt","r") as f:
                    data = json.loads(f.read())
                empIndex = utils.find(data,"id",searchedId)
                if(data[empIndex]["pos"].lower()=="jr"):
                    data[empIndex]["pos"] = "entry"
                    data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
                elif(data[empIndex]["pos"].lower() =="sr"):
                    data[empIndex]["pos"] = "jr"
                    data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
                elif(data[empIndex]["pos"].lower() =="leader"):
                    data[empIndex]["pos"] = "sr"
                    data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
                with open('src\data\empData\empData.txt', 'w+') as f:
                    f.write(json.dumps(utils.sortListInDict(data,"id")))
                tkm.showinfo(title = "Submission sucessful", message = "Employee demoted.")
            root.destroy()
            editEmpWindow()
    else: 
        flag = tkm.askyesno(title = "Promotion", message = "Are you sure about the demotion?")
        if flag:
            with open("src\data\empData\empData.txt","r") as f:
                data = json.loads(f.read())
            empIndex = utils.find(data,"id",searchedId)
            if(data[empIndex]["pos"].lower()=="jr"):
                data[empIndex]["pos"] = "entry"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() =="sr"):
                data[empIndex]["pos"] = "jr"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() =="leader"):
                data[empIndex]["pos"] = "sr"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            elif(data[empIndex]["pos"].lower() == "manager"):
                data[empIndex]["pos"] = "leader"
                data[empIndex]["salary"] = Employee.getSalary(data[empIndex]["dep"],data[empIndex]["pos"])
            with open('src\data\empData\empData.txt', 'w+') as f:
                f.write(json.dumps(utils.sortListInDict(data,"id")))
            tkm.showinfo(title = "Submission sucessful", message = "Employee demoted.")
        root.destroy()
        editEmpWindow()

def fireEmp(pos, searchedId, root):
    with open("src\data\empData\currentUser.txt", "rb+") as f:
        serData = pickle.loads(f.read())
    if(serData["pos"] == "leader"):
        if((pos =="Manager") or (pos =="Executive") or (pos=="Leader")):
            tkm.showerror(title = "Access denied", message = "You do not have permission.")
        else:
            flag = tkm.askyesno(title = "Dismissal", message = "Are you sure you want to fire this employee?")
            if flag:
                with open("src\data\empData\empData.txt","r") as f:
                    data = json.loads(f.read())
                    empIndex = utils.find(data,"id",searchedId)
                    del data[empIndex]
                with open('src\data\empData\empData.txt', 'w+') as f:
                    f.write(json.dumps(utils.sortListInDict(data,"id")))
                tkm.showinfo(title = "Submission sucessful", message = "Employee dismissed.")
            root.destroy()
            editEmpWindow()
    elif(serData["pos"] == "executive"):
        if(pos == "Executive"):
            tkm.showerror(title = "Access denied", message = "You do not have permission.")
        else:
            flag = tkm.askyesno(title = "Promotion", message = "Are you sure you want to fire this employee?")
            if flag:
                with open("src\data\empData\empData.txt","r") as f:
                    data = json.loads(f.read())
                    empIndex = utils.find(data,"id",searchedId)
                    del data[empIndex]
                with open('src\data\empData\empData.txt', 'w+') as f:
                    f.write(json.dumps(utils.sortListInDict(data,"id")))
                tkm.showinfo(title = "Submission sucessful", message = "Employee dismissed.")
            root.destroy()
            editEmpWindow()
    else: 
        flag = tkm.askyesno(title = "Promotion", message = "Are you sure you want to fire this employee?")
        if flag:
            with open("src\data\empData\empData.txt","r") as f:
                data = json.loads(f.read())
                empIndex = utils.find(data,"id",searchedId)
                del data[empIndex]
            with open('src\data\empData\empData.txt', 'w+') as f:
                f.write(json.dumps(utils.sortListInDict(data,"id")))
            tkm.showinfo(title = "Submission sucessful", message = "Employee dismissed.")
        root.destroy()
        editEmpWindow()

# def displayInfo(Toplevel, canvas):
    
def editEmpWindow():
    root = Toplevel()
    root.title("Excrucia Inc.")
    root.geometry("640x750")
    root.minsize(640, 750)
    root.maxsize(640, 750)
    
    bg = PhotoImage(file = "editbackground.png")
    
    canvas = Canvas(root, width = 640, height = 750)
    canvas.pack(fill = "both", expand = True)
    
    canvas.create_image(0, 0, image = bg, anchor = "nw")
    
    entry0 = Entry(root, bg = "#87CEFA", fg ="#BFEFFF", font = ("Arial Bold", 18), width = 15)
    entry0.insert(0, "Enter ID")
    canvas.create_window(125, 50, window = entry0)

    canvas.create_text(84,100, text = "First Name:", font = ("Arial Bold", 16), fill = "black")
    canvas.create_text(84,150, text = "Last Name:", font = ("Arial Bold", 16), fill = "black")
    canvas.create_text(92,200, text = "Date of birth:", font = ("Arial Bold", 16), fill = "black")
    canvas.create_text(58,250, text = "Email:", font = ("Arial Bold", 16), fill = "black")
    canvas.create_text(61,300, text = "Salary:", font = ("Arial Bold", 16), fill = "black")
    canvas.create_text(89,350, text = "Department:", font = ("Arial Bold", 16), fill = "black")
    canvas.create_text(71,400, text = "Position:", font = ("Arial Bold", 16), fill = "black")
        
    entry2 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 100, window = entry2)
    entry3 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 150, window = entry3)
    entry5 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 250, window = entry5)
    entry6 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 300, window = entry6)
    entry7 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 350, window = entry7)
    entry8 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
    canvas.create_window(350, 400, window = entry8)

    saveB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Save", width = 13)
    saveB.bind('<Enter>', lambda event: on_enter(saveB))
    
    saveB.bind('<Leave>', lambda event: on_leave(saveB))
    canvas.create_window(450, 600, window = saveB)

    searchB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Search", 
                   width = 13)
    searchB.bind('<Enter>', lambda event: on_enter(searchB))
    searchB.bind('<Button-1>', lambda event: searchById(canvas, root, entry0.get(), entry2, entry3, entry5, entry6, entry7, entry8, saveB, entry0))
    searchB.bind('<Leave>', lambda event: on_leave(searchB))
    canvas.create_window(200, 600, window = searchB)

    promoteB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Promote", width = 13)
    promoteB.bind('<Enter>', lambda event: on_enter(promoteB))
    promoteB.bind('<Button-1>', lambda event: promote(entry8.get(),entry0.get(), root))
    promoteB.bind('<Leave>', lambda event: on_leave(promoteB))
    canvas.create_window(200, 650, window = promoteB)
    
    demoteB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Demote", 
                     width = 13)
    demoteB.bind('<Enter>', lambda event: on_enter(demoteB))
    demoteB.bind('<Button-1>', lambda event: demote(entry8.get(),entry0.get(), root))
    demoteB.bind('<Leave>', lambda event: on_leave(demoteB))
    canvas.create_window(450, 650, window = demoteB)
    
    cancelB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Cancel", 
                     width = 13)
    cancelB.bind('<Enter>', lambda event: on_enter(cancelB))
    cancelB.bind('<Button-1>', lambda event: refresh(root))
    cancelB.bind('<Leave>', lambda event: on_leave(cancelB))
    canvas.create_window(200, 700, window = cancelB)

    fireB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Fire", width = 13)
    fireB.bind('<Enter>', lambda event: on_enter(fireB))
    fireB.bind('<Button-1>', lambda event: fireEmp(entry8.get(),entry0.get(), root))
    fireB.bind('<Leave>', lambda event: on_leave(fireB))
    canvas.create_window(450, 700, window = fireB)

    root.mainloop()

if __name__ == "__main__":
   editEmpWindow()

