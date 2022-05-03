from employee import Employee
import pickle
import utils
import os 
import json
from department import Department
from depLeader import DepLeader

class Manager(DepLeader):
    def __init__(self, id, name, dob, email, pos, salary, dep):
        super().__init__(id, name, dob, email, pos, salary, dep)
        self.pos = "manager"

    def newDepLeader(self):
        name = Employee.initName(self)
        dob = Employee.setDob()
        dep = input("Enter the manager's department: ")
        pos = "leader"
        salary = Employee.getSalary(dep,pos)

        if((not os.path.exists("src\data\empData\empData.txt")) or (os.path.getsize("src\data\empData\empData.txt")==0)):
            with open('src\data\empData\empData.txt', 'w+') as f:
                wrapper = []
                currData = {}
                email = utils.emailName(name)+"."+"er-1"+"@gmail.com"
                pic = DepLeader("ER-1",name,dob,email,pos,salary,dep)
                currData["name"] = pic.name
                currData["id"] = pic.id
                currData["dob"] = pic.dob
                currData["email"] = pic.email
                currData["pos"] = pic.pos
                currData["salary"] = pic.salary
                currData["dep"] = pic.dep
                wrapper.append(currData)
                f.write(json.dumps(wrapper))
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
                email = utils.emailName(name)+"."+id.lower()+"@gmail.com"
                pic = DepLeader(id,name,dob,email,pos,salary,dep)
                currData = {}
                currData["name"] = pic.name
                currData["id"] = pic.id
                currData["dob"] = pic.dob
                currData["email"] = pic.email
                currData["pos"] = pic.pos
                currData["salary"] = pic.salary
                currData["dep"] = pic.dep
                picData.append(currData)
            with open('src\data\empData\empData.txt', 'w+') as f:
                f.write(json.dumps(utils.sortListInDict(picData,"id")))
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
            

    def managerPromote(self):
        promotedEmp = DepLeader.searchById(self)
        dep = DepLeader.getDep(self)
        with open('src\data\empData\empData.txt', 'r+') as f:
            data = json.loads(f.read())
            promotedEmpIndex = utils.find(data,"id",promotedEmp["id"])
        with open('src\data\empData\empData.txt', 'w+') as f:
            while True:
                if(data[promotedEmpIndex]["pos"] == "sr"):
                    data[promotedEmpIndex]["pos"] = "depLeader"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
            print(data)
            f.write(json.dumps(utils.sortListInDict(data,"id")))
    
    def managerDemote(self):
        demotedEmp = DepLeader.searchById(self)
        dep = DepLeader.getDep(self)
        with open('src\data\empData\empData.txt', 'r+') as f:
            data = json.loads(f.read())
            promotedEmpIndex = utils.find(data,"id",demotedEmp["id"])
        with open('src\data\empData\empData.txt', 'w+') as f:
            while True:
                if(data[promotedEmpIndex]["pos"] == "depLeader"):
                    data[promotedEmpIndex]["pos"] = "sr"
                    data[promotedEmpIndex]["salary"] = Employee.getSalary(data[promotedEmpIndex]["dep"],data[promotedEmpIndex]["pos"])
                    break
            print(data)
            f.write(json.dumps(utils.sortListInDict(data,"id")))

    
# man = Manager("ER-4","Harry Styles","29/04/2002","asdf","manager",2,"IT")
# man.newDepLeader()
with open("src/data/empData/empData.txt", "rb+") as f:
    data = json.loads(f.read())
print(data[utils.find(data,"email","haroldlang.er-1@gmail.com")])