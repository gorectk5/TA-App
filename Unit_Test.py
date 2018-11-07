import unittest
from TASchedulingApp import TASchedulingApp
from User import User

class Testcode(unittest.TestCase):

  
  App = TASchedulingApp()

  login = "Admin"
  login2 = "TA"
  sTA = "John"
  iCourse = "361"
  isec = "1"
  iCourse2 = "431"
  sTA2 = "Jim"
  App.LoggedInUser is None
  def create_lab_invalid_login(self,sTA,iCourse,isec):
    self.assertEqual("Invalid command",App.createlab(sTA,iCourse,isec))
  App.LoggedInUser = User(login2,"TA","4")
  def create_lab_invalid_clearance(self,sTA,iCourse,isec):
    self.assertEqual("Invalid command",App.createlab(sTA,iCourse,isec))
  App.LoggedInUser = User(login,"Admin","1")
  def create_lab_succesful(self,sTA,iCourse,isec):
    self.assertEqual("Lab Created",App.createlab(sTA,iCourse,isec))
  def create_lab_no_class(self,sTA,iCourse2,isec):
    self.assertEqual(App.createlab("Course does not exist",sTA,iCourse2,isec))
  def create_lab_succesful(self,sTA2,iCourse,isec):
    self.assertEqual("TA does not exist",App.createlab(sTA2,iCourse,isec))
  

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

  def test_delete_account_invalid(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.assertEquals(self.App.deleteAccount("jack"), "No account jack found")
  def test_delete_account_valid(self):
    self.App.LoggedInUser = User("Admin", "Admin", 1)
    self.App.createAccount("bob","bob","2")
    self.assertEquals(self.App.deleteAccount("bob"), "account bob deleted")
  def test_delete_account_invalid_clearance(self):
    self.App.LoggedInUser = User("TA", "TA", 4)
    self.assertEquals(self.App.deleteAccount("jack"), "Invalid command")




suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Testcode))
runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])
