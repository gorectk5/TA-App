from User import User
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
