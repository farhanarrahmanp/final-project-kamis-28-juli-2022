import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Employee List sub-menu
class Test1VerifyTheEmployeeListSubMenu(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_033
    # Search an Employee Name
    def test_tc_033(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running TC_007
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # 2. Click "PIM" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[2]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Employee Name text box and input characters and 
        # 2. Click the available option
        browser.find_element(By.ID,"empsearch_employee_name_empName").send_keys("Linda Jane Anderson") 
        time.sleep(1)
        # 3. Click "Search" button
        browser.find_element(By.ID,"searchBtn").click() 
        time.sleep(3)

        # validation
        validation = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody").text

        # Employee found
        self.assertIn('Linda Jane', validation)

    # TC_034
    # Input data and reset
    def test_tc_034(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running TC_007
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # 2. Click "PIM" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[2]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click drop-down lists (Employment Status, Include, Job Title, and Sub Unit) and choose an option
        select = Select(browser.find_element(By.ID,'empsearch_employee_status'))
        select.select_by_visible_text('Full-Time Permanent')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'empsearch_termination'))
        select.select_by_visible_text('Current Employees Only')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'empsearch_job_title'))
        select.select_by_visible_text('VP - Sales & Marketing')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'empsearch_sub_unit'))
        select.select_by_visible_text('Administration')
        time.sleep(1)
        # 2. Click text boxes (Employee Name, Id, and Supervisor Name), input characters, and click the available option (except Id text box)
        browser.find_element(By.ID,"empsearch_employee_name_empName").send_keys("Linda Jane Anderson")
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_id").send_keys("0016")
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_supervisor_name").send_keys("John Smith")
        time.sleep(1)
        # 3. Click "Reset" button
        browser.find_element(By.ID,"resetBtn").click()
        time.sleep(3)

        # validation
        validation = browser.find_element(By.ID,"empsearch_employee_name_empName").get_attribute("value")

        # Text boxes are empty and drop-down lists are set to "All" (except Include set to "Current Employees Only")
        self.assertIn('', validation)

    def tearDown(self): 
        self.browser.close()

# Test Scenario: Verify the Add Employee page
class Test2VerifyTheAddEmployeePage(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_035
    # Input data only in Required text box
    def test_tc_035(self):
        # steps
        browser = self.browser # open web browser
        browser.get(url) # open website
        time.sleep(3)
        # Pre-condition
        # 1. Running TC_007
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # 1. Click Username text box
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # 2. Click Password text box
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # 3. Click "LOGIN" button
        time.sleep(1)
        # 2. Click "PIM" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[2]/a/b").click()
        time.sleep(1)
        # 3. Click "Add" button
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        # Test Steps
        # 1. Click First Name text box and input characters
        browser.find_element(By.ID,"firstName").send_keys("Bili") 
        time.sleep(1)
        # 2. Click Last Name text box and input characters
        browser.find_element(By.ID,"lastName").send_keys("Jin") 
        time.sleep(1)
        # 3. Click "Save" button
        browser.find_element(By.ID,"btnSave").click() 
        time.sleep(3)
        
        # validation
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[2]/ul/li[2]/a").click()
        time.sleep(3)
        validation = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody").text
        
        # Successfully saved
        self.assertIn('Bili', validation)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()