import unittest
class Testcode(unittest.TestCase):

  from TASchedulingApp import TASchedulingApp
  from User import User
  App = TASchedulingApp()

  login = "Admin"
  login2 = "TA"
  sTA = "John"
  iCourse = "361"
  isec = "1"
  iCourse2 = "431"
  sTA2 = "Jim"
  App.LoggedInUser = None
  def create_lab_invalid_login(self,sTA,iCourse,isec):
    self.assertEqual(App.createlab(sTA,iCourse,isec),"Invalid command")
    App.login(login2,"TA")
  def create_lab_invalid_clearance(self,sTA,iCourse,isec):
     self.assertEqual(App.createlab(self,sTA,iCourse,isec),"Invalid command")
  App.login(login,"Admin")
  def create_lab_successful(self,sTA,iCourse,isec):
     self.assertEqual(App.createlab(sTA,iCourse,isec),"Lab Created")
  def create_lab_no_class(self,sTA,iCourse2,isec):
     self.assertEqual(App.createlab(sTA,iCourse2,isec),"Course does not exist")
  def create_lab_successful(self,sTA2,iCourse,isec):
     self.assertEqual(App.createlab(sTA2,iCourse,isec),"TA does not exist")

  def create_account_successful(self):
    App.LoggedInUser = User("Admin","Admin","1")
    self.assertTrue(App.CreateAccount("Example","Example","3"))
  def create_account_existing(self):
    App.LoggedInUser = User("Admin","Admin","1")
    App.CreateAccount("Existing","Existing","1")
    self.assertFalse(App.CreateAccount("Existing","Existing","1"))
  def create_account_bad_input(self):
    App.LoggedInUser = User("Admin", "Admin", "1")
    self.assertFalse(App.CreateAccount("co,mma","normal","1"))
    self.assertFalse(App.CreateAccount("normal","co,mma","1"))
    self.assertFalse(App.CreateAccount("normal","normal","bad"))
  def create_account_bad_clearance(self):
    App.LoggedInUser = User("TA", "TA", "4")
    self.assertFalse(App.CreateAccount("comma", "normal", "1"))

  def login_successful(self):
    App.LoggedInUser = None
    self.assertTrue(App.Login("Admin","Admin"))
  def login_unsuccessful(self):
    App.LoggedInUser = None
    self.assertFalse(App.Login("DoesNotExist", "Admin"))
  def login_bad_input(self):
    App.LoggedInUser = None
    self.assertFalse(App.Login(1,None))






suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Testcode))
runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])
