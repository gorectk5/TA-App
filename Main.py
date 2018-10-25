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
  else:
    print("Invalid Command")
  Command = input("Command: ")
