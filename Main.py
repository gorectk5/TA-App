from User import User
from TASchedulingApp import TASchedulingApp


App = TASchedulingApp()
print("Login\n")
username = input("Username: ")
password = input("Password: ")

App.login(username,password)
Command = input("Command: ")
while Command!="Exit":
  if Command == "Create Account":
    username = input("Username: ")
    password = input("Password: ")
    clearance = input("Clearance: ")
    if clearance == "Supervisor":
      App.createAccount(username,password,1)
    elif clearance == "Administrator":
      App.createAccount(username,password,2)
    elif clearance == "Professor":
      App.createAccount(username,password,3)
    elif clearance == "TA":
      App.createAccount(username,password,4)
    else:
      print("Invalid clearance")

  elif (Command == "Create Course"):
    username = input("Username: ")
    nusername = input("New Username: ")
    npassword = input("New Password: ")
    nclearance = input("New Clearance: ")
    App.editAccount(username, nusername, npassword, nclearance)

  elif (Command == "Create Course"):
    id = input("Enter Unique Course id: ")
    courseNum = input("Enter Course number: ")
    numOfSections = input("Enter Number of sections: ")
    if clearance == "Supervisor" or clearance == "Administrator":
      App.createCourses(id,courseNum,numOfSections)
    else:
      print("Invalid Clearance")

  elif Command == "Delete Account":
    username = input("Username: ")
    App.deleteAccount(username)


  else:
    print("Invalid Command")
  Command = input("Command: ")



