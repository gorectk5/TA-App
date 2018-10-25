from User import User
from TASchedulingApp import TASchedulingApp


App = TASchedulingApp()
print("Login\n")
username = input("Username: ")
password = input("Password: ")

App.login(username,password)
App.createAccount("TA","TA",4)
