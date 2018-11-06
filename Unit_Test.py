import unittest
class Testcode(unittest.TestCase):

  from TASchedulingApp import TASchedulingApp

  App = TASchedulingApp()

  login = "Admin"
  login2 = "TA"
  sTA = "John"
  iCourse = "361"
  isec = "1"
  iCourse2 = "431"
  sTA2 = "Jim"
  App.login(NULL,NULL)
  def create_lab_invalid_login(sTA,iCourse,isec)
     self.assertEqual(App.createlab(sTA,iCourse,isec),"Invalid command")
  App.login(login2,"TA")
   def create_lab_invalid_clearance(sTA,iCourse,isec)
     self.assertEqual(App.createlab(sTA,iCourse,isec),"Invalid command")
  App.login(login,"Admin")
  def create_lab_succesful(sTA,iCourse,isec)
     self.assertEqual(App.createlab(sTA,iCourse,isec),"Lab Created")
  def create_lab_no_class(sTA,iCourse2,isec)
     self.assertEqual(App.createlab(sTA,iCourse2,isec),"Course does not exist")
  def create_lab_succesful(sTA2,iCourse,isec)
     self.assertEqual(App.createlab(sTA2,iCourse,isec),"TA does not exist")

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Testcode))
runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])
