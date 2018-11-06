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

      def assignTA(self,sTA,iCourse,isec):
    
    if self.LoggedInUser != "Null" and self.LoggedInUser.clearance < 3 :

      file_object = open("Courses.txt","a+")
      added = False;
      for line in file_object:

        curcourse = line.split(",")

        if curcourse[1]==icourse:
          added=True;
          for i in curcourse:
            if curcourse[i] == isec:
              for x in curcourse:
                if x  == i:
                  file_object.write(curcourse[x] + sTA)
                else:
                  file_object.write(curcourse[x])
              print("TA added to lab")
          if added != True:
           print("Lab does not exist")
        else:
          print("course does not exist")
    else:

      print("Invalid command")
