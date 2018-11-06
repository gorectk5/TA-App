import unittest




class ATDDTESTS(unittest.TestCase):
  #admin/supiv

    def setUp(self):
        self.supervisor1 = Supervisor(sup1,pass1,1)
        self.admin1 = Admin(adm1,pass2,2)
        self.instructor = Instructor(inst1,pass3,3)
        self.ta = ta(ta1,pass4,4)
        self.instructor = Instructor(inst2, pass5, 3)
        self.ta = ta(ta2, pass7, 4)
        self.instructor = Instructor(inst3, pass6, 3)
        self.ta = ta(ta3, pass8, 4)
        total_course = 1
        total_ta = 3
        total_account = 8
        total_labs = 6

'''Currently in the system there is only 1 account and a new administrator account'''
  def test_valid_create_account(self,username,password,priority):
      self.assertEquals("Successfully Created Account",self.supervisor1.create_account("admin","admin",1))
    pass
  def test_existing_create_account(self,u,p):
      create_account("admin","admin",1)
      self.assertEquals("Account Already Exists",self.supervisor1.create_account("admin","admin",1))
    pass
  def test_invalid_create_account(self,u,p):
    self.assertEquals("Invalid parameters for create account", self.supervisor1.create_account(5,7,"ten")
    pass
  def test_login_valid_account(self,u,p):
    self.supervisor1.create_account("admin","admin",1)
    self.assertEquals("Sucessfully Logged In",self.admin1.login("admin","admin")
    pass
  def test_login_invalid_account(self,u,p):
    self.assertEquals("Account does not exist", self.admin1.login("fake account","not real")
    pass
   def test_login_nonexisting_account(self,u,p):
    self.assertRaises(Exception, self.login("supervisor2"))
    pass
  def test_delete_nonexisting_account(self,u,p):
    self.assertRaises(Exception, self.deleteAccount("supervisor2"))
    pass
  def test_delete_valid_account(self,u,p):
    self.assertEquals("account supervisor1 deleted", self.deleteAccount("supervisor1"))
    pass
  def test_valid_edit_account(self,u,p):
    self.assertEquals("account supervisor1 edited", self.editAccount("supervisor1"))
    pass
def test_nonexisting_edit_account(self,u,p):
  self.assertEquals("account does not exist",self.admin1.edit_account("admin2"))
def test_notifications(self,user,boolean):
    self.assertEquals(boolean,"false")
    self.assertEquals("notification was sent", self.admin1.notify_user(user))
def test_access_data(self):
  self.assertEquals("supervisor1,admin1,inst1,inst2,inst3,ta1,ta2,ta3",self.admin1.access_data())
#supiv only
def test_assign_insturctor(self,inst,course):
    self.assertEquals("inst was assigned to course", self.supervisor1.assign_insturctor(inst,course))
def test_assign_TA_to_course(self,ta):
    self.assertEquals("TA was assigned to course", self.supervisor1.assign_TA(inst, course))
   def test_assign_TA_to_lab(self,ta):
      self.assertEquals("TA was assigned to lab", self.supervisor1.assign_TA_to_lab(inst, lab))
  #instructor
  def test_edit_contact_info_instructor(self,info):
    self.assertEquals("Instructor contact info has been edited", self.instructor.edit_contact_info_instructor(inst, info))
  def test_view_course_assignment(self):
    self.assertEquals("Course assignments are as follows:", self.instructor.view_course_assignment())
  def test_view_ta_assignment(self):
    self.assertEquals("TA assignments are as follows:", self.instructor.view_ta_assignment())
  def test_send_nodifcation_instructor(self):
    self.assertEquals("Instructor has been notified", self.instructor.send_nodifcation_instructor())
  def test_assign_TA_to_lab_instructor(self,ta):
      self.assertEquals("TA assigned to a lab section", self.instructor.send_nodifcation_instructor())
  def read_PCI_instructor(self):
      self.assertEquals("Supervisor info: ,Admin info: , Instructor info: , TA info: ", self.instructor.read_PCI())
  #TA
  def test_edit_contact_info_ta(self,info):
      self.assertEquals("Enter new contact info: ", self.ta.edit_contact_info_ta())
  def test_view_ta_assignment_ta(self):
      self.assertEquals("All TA assignments: ", self.ta.view_ta_assignment_ta())
  def read_PCI_ta(self):
      self.assertEquals("Supervisor info: ,Admin info: , Instructor info: , TA info: ", self.ta.read_PCI())

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(ATDDTESTS))
runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])
