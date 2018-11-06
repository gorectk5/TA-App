from User import User
from Course import Course
class TASchedulingApp:
  LoggedInUser = "Null" #Not sure how to do actual Null
  def __init__(self):
    LoggedInUser = "Null"
  
  def login(self,sUsername,sPassword):
    file_object = open("Accounts.txt","r")
    for line in file_object:
      lsUser = line.split(",")
      if(lsUser[0]==sUsername and lsUser[1]==sPassword):
        self.LoggedInUser = User(sUsername,sPassword,int(lsUser[2]))
    if self.LoggedInUser == "Null":
      print("could not login")
    else:
      print("Logged In!")

  def createAccount(self,sUsername,sPassword,iClearance):
    if self.LoggedInUser != "Null" and self.LoggedInUser.clearance < 3 :
      oUser = User(sUsername,sPassword,iClearance)
      file_object = open("Accounts.txt","a")
      file_object.write(sUsername + "," + sPassword + "," + str(iClearance) + "\n")
      file_object.close()
      print("Created Account")  
    else:
      print("Invalid command")
      
  def editAccount(self, tUsername, nUsername, nPassword, nClearance):
    if self.LoggedInUser != "Null" and self.LoggedInUser.clearance < 3:
        file_object = open("Accounts.txt", "r+")
        lines = file_object.readlines()
        file_object.seek(0)
        for i in lines:
            if tUsername not in i:
                file_object.write(i)
            else:
                file_object.write(nUsername + "," + nPassword + "," + nClearance + "\n")
        file_object.truncate()
        file_object.close()
        print("Edited Account")
    else:
        print("Invalid command or insufficient access")

  def createCourses(self, uniqId, courseNumber, Professor):
    if self.LoggedInUser != "Null" and self.LoggedInUser.clearance < 2:
      course = Course(uniqId, courseNumber, Professor)
      file_object = open("Courses.txt", "a")
      file_object.write(uniqId + "," + courseNumber + "," + Professor + "\n")
      file_object.close()
      print("Created Course")
    else:
      print("Invalid command")

  def createLab(self,sTA,icourse,ilab):
    
    if self.LoggedInUser != "Null" and self.LoggedInUser.clearance < 3 :

      file_object = open("Labs.txt","a")
      file_object.write(ilab + "," + icourse + "," + sTA + "\n")
      file_object.close()
      print("Lab Created")

    else:

      print("Invalid command")

      
  def deleteAccount(self, sUsername):
    
    file_object = open("Accounts.txt", "r")
    usernames = file_object.readlines()
    file_object.close()
    file_object = open("Accounts.txt", "w")
    deleted = False
    for line in usernames:
      user = line.split(",")
      if(user[0]!=sUsername):
        file_object.write(line)
      else:
        deleted = True
    if(deleted == False):
        print("No account " + sUsername + " found")
        return "No account " + sUsername + " found"
    else:
        print("account " + sUsername + " deleted")
        return "account " + sUsername + " deleted"
