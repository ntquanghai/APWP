from posixpath import split
from tkinter import *

from numpy import full
import addUserWindow
import json
import src.domains.utils as utils
from tkcalendar import DateEntry
from tkinter.messagebox import askyesno


def on_enter(button):
   button.config(background="#B0E2FF")
def on_leave(button):
   button.config(background= "#87CEFF")

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

def searchById(canvas, root, searchedId):
    with open("src\data\empData\empData.txt","r") as f:
        data = json.loads(f.read())
        print(data)
    empIndex = utils.find(data,"id",searchedId)
    if(empIndex == -1): 
        pass
    else:
        searchedEmp = data[empIndex]
        
        entry2 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        entry2.insert(0, splitName(searchedEmp["name"])["firstName"])
        canvas.create_window(350, 100, window = entry2)
        entry3 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 20)
        entry3.insert(0, splitName(searchedEmp["name"])["lastName"])
        day = splitDob(searchedEmp["dob"])["day"]
        month = splitDob(searchedEmp["dob"])["month"]
        year = splitDob(searchedEmp["dob"])["year"]
        entry4 = DateEntry(root, selectmode="day", date_pattern="dd/mm/yyyy", day = day, month =month, year = year)
        entry4.configure(background="#87CEFA", font = ("Arial", 16), width = 18, borderwidth= 1)
        canvas.create_window(350, 150, window = entry3)
        canvas.create_window(350, 200, window = entry4)
        canvas.create_text(350, 250, text = searchedEmp["email"], font = ("Arial Bold", 16))
        canvas.create_text(350, 300, text = searchedEmp["salary"], font = ("Arial Bold", 16))
        canvas.create_text(350, 350, text = searchedEmp["dep"], font = ("Arial Bold", 16))
        canvas.create_text(350, 400, text = searchedEmp["pos"].capitalize(), font = ("Arial Bold", 16))
   
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
        
    entry2 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 0)
    canvas.create_window(350, 100, window = entry2)
    entry3 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 0)
    canvas.create_window(350, 150, window = entry3)
    entry4 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 0)
    canvas.create_window(350, 200, window = entry4)
    entry5 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 0)
    canvas.create_window(350, 250, window = entry5)
    entry6 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 0)
    canvas.create_window(350, 300, window = entry6)
    entry7 = Entry(root, bg = "#87CEFA", fg ="#000000", font = ("Arial Bold", 16), width = 0)
    canvas.create_window(350, 350, window = entry7)
    
    searchB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Search", 
                   width = 13)
    searchB.bind('<Enter>', lambda event: on_enter(searchB))
    searchB.bind('<Button-1>', lambda event: searchById(canvas, root, entry0.get()))
    searchB.bind('<Leave>', lambda event: on_leave(searchB))
    canvas.create_window(200, 600, window = searchB)
    
    saveB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Save", 
                      width = 13)
    saveB.bind('<Enter>', lambda event: on_enter(saveB))
    saveB.bind('<Leave>', lambda event: on_leave(saveB))
    canvas.create_window(450, 600, window = saveB)
    
    promoteB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Promote", 
                      width = 13)
    promoteB.bind('<Enter>', lambda event: on_enter(promoteB))
    promoteB.bind('<Leave>', lambda event: on_leave(promoteB))
    canvas.create_window(200, 650, window = promoteB)
    
    demoteB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Demote", 
                     width = 13)
    demoteB.bind('<Enter>', lambda event: on_enter(demoteB))
    demoteB.bind('<Leave>', lambda event: on_leave(demoteB))
    canvas.create_window(450, 650, window = demoteB)
    
    cancelB = Button(root, bd = 1, bg = "#87CEFF", fg = "#FFFFFF", activebackground = "#B0E2FF", activeforeground = "#FFFFFF", font = ("Arial Bold", 16), text ="Cancel", 
                     width = 13, command = root.destroy)
    cancelB.bind('<Enter>', lambda event: on_enter(cancelB))
    cancelB.bind('<Leave>', lambda event: on_leave(cancelB))
    canvas.create_window(325, 700, window = cancelB)
        
    root.mainloop()

if __name__ == "__main__":
   editEmpWindow()


