import unittest
from TASchedulingApp import TASchedulingApp
from User import User

class Testcode(unittest.TestCase):

  
  App = TASchedulingApp()
 def test_create_lab_invalid_login(self):
    
    self.App.LoggedInUser is None
    self.assertEqual("Invalid command",self.App.createLab("John","361","1"))
  
  def test_create_lab_invalid_clearance(self):
    
    self.App.LoggedInUser = self.User("TA","TA",4)
    self.assertEqual("Invalid command",self.App.createLab("John","361","1"))
  
  def test_create_lab_succesful(self):
    
    self.App.LoggedInUser = self.User("Admin","Admin",1)
    self.assertEqual("Lab Created",self.App.createLab("John","361","1"))

  def test_create_lab_no_class(self):
    
    self.App.LoggedInUser = self.User("Admin","Admin",1)
    self.assertEqual("Course does not exist",self.App.createLab("John","431","1"))

  def test_create_lab_succesful(self):
    
    self.App.LoggedInUser = self.User("Admin","Admin",1)
    self.assertEqual("TA does not exist",self.App.createLab("Jim","361","1"))
  

  def test_create_account_successful(self):
    
    self.App.LoggedInUser = self.User("Admin","Admin",1)

    self.assertTrue(self.App.createAccount("Example","Example",3))

  def test_create_account_existing(self):
    
    self.App.LoggedInUser = self.User("Admin","Admin",1)

    self.App.createAccount("Existing","Existing",1)

    self.assertFalse(self.App.createAccount("Existing","Existing",1))

  def test_create_account_bad_input(self):
    
    self.App.LoggedInUser = self.User("Admin", "Admin", 1)

    self.assertFalse(self.App.createAccount("co,mma","normal",1))

    self.assertFalse(self.App.createAccount("normal","co,mma",1))

    self.assertFalse(self.App.createAccount("normal","normal","bad"))

  def test_create_account_bad_clearance(self):
    
    self.App.LoggedInUser = self.User("TA", "TA", 4)

    self.assertFalse(self.App.createAccount("comma", "normal", 1))



  def test_login_successful(self):
   
    self.App.LoggedInUser = None

    self.assertTrue(self.App.login("Admin","Admin"))

  def test_login_unsuccessful(self):
    
    self.App.LoggedInUser = None

    self.assertFalse(self.App.login("DoesNotExist", "Admin"))

  def test_login_bad_input(self):
   
    self.App.LoggedInUser = None

    self.assertFalse(self.App.login(1,None))



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
