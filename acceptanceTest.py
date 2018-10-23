import unittest




class ATDDTESTS(unittest.TestCase):
  #admin/supiv
  total = 1

    def setUp(self):
        self.supervisor1 = Supervisor(sup1,pass1,1)
        self.admin1 = Admin(adm1,pass2,2)
        self.intstructor = Instructor(inst1,pass3,3)
        self.ta = ta(ta1,pass4,4)
        self.intstructor = Instructor(inst2, pass5, 3)
        self.ta = ta(ta2, pass7, 4)
        self.intstructor = Instructor(inst3, pass6, 3)
        self.ta = ta(ta3, pass8, 4)
        total_course = 1
        total_ta = 3
        total_account = 8
        total_labs = 6

'''Currently in the system there is only 1 account and a new administrator account'''
  def test_valid_create_account(self,username,password,priority):
    self.supervisor1.createCourse
    self.Asserq
    pass
  def test_existing_create_account(self,u,p):
    pass
  def test_invalid_create_account(self,u,p):
    pass
  def test_login_valid_account(self,u,p):
    pass
  def test_login_invalid_account(self,u,p):
    pass
  def test_login_nonexisting_account(self,u,p):
    pass
  def test_delete_nonexisting_account(self,u,p):
    pass
  def test_delete_valid_account(self,u,p):
      pass
  def test_valid_edit_account(self,u,p):
    pass
  def test_existing_edit_account(self,u,p):
    pass
  i
  def test_assign_TA_to_lab(self,ta):
    pass
  #instructor
  def test_edit_contact_info_instructor(self,info):
    pass
  def test_view_course_assignment(self):
    pass
  def test_view_ta_assignment(self):
    pass
  def test_send_nodifcation_instructor(self):
    pass
  def test_assign_TA_to_lab_instructor(self,ta):
    pass
  def read_PCI_instructor(self):
    pass
  #TA
  def test_edit_contact_info_ta(self,info):
    pass
  def test_view_ta_assignment_ta(self):
    pass
  def read_PCI_ta(self):
    pass

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(ATDDTESTS))
runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])