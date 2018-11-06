import unittest
class Testcode(unittest.TestCase):
  login = Admin
  login2 = NULL
  sTA = "John"
  iCourse = "361"
  isec = "1"
  iCourse2 = "431"
  isec2 = "5"
  def add_ta_succesful()
     self.assertEqual(login.assignTA(self,sTA,iCourse,isec),"TA added to lab")
  def add_ta_no_lab(self,sTA,iCourse,isec)
    self.assertEqual(login.assignTA(self,sTA,iCourse,isec2),"Lab does not exist")
  def add_ta_no_course(self,sTA,iCourse,isec)
     self.assertEqual(login.assignTA(self,sTA,iCourse2,isec),"course does not exist")
  def add_ta_no_login(self,sTA,iCourse,isec)
     self.assertEqual(login2.assignTA(self,sTA,iCourse,isec),"Invalid command")
  suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Testcode))
runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])
