import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Users Management sub-menu
class Test1VerifyTheUsersManagementSubMenu(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_045
    # Search an Username
    def test_tc_045(self):
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
        # 2. Click "Admin" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Username text box and input characters
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("Admin") 
        time.sleep(1)
        # 2. Click "Search" button
        browser.find_element(By.ID,"searchBtn").click() 
        time.sleep(3)

        # validation
        validation = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody").text

        # Records found
        self.assertIn('Admin', validation)

    # TC_046
    # Input data and reset
    def test_tc_046(self):
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
        # 2. Click "Admin" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click User Role and Status drop-down lists and choose an option
        select = Select(browser.find_element(By.ID,'searchSystemUser_userType'))
        select.select_by_visible_text('ESS')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'searchSystemUser_status'))
        select.select_by_visible_text('Enabled')
        time.sleep(1)
        # 2. Click Username and Employee Name text boxes and input characters
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("Anu teju sri")
        time.sleep(1)
        # 3. Click "Reset" button
        browser.find_element(By.ID,"resetBtn").click()
        time.sleep(3)

        # validation
        validation = browser.find_element(By.ID,"searchSystemUser_userName").get_attribute("value")

        # Text boxes are empty and drop-down lists are set to "All"
        self.assertIn('', validation)

    def tearDown(self): 
        self.browser.close()

# Test Scenario: Verify the Add User page
class Test2VerifyTheAddUserPage(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_047
    # Add an User
    def test_tc_047(self):
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
        # 2. Click "Admin" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click()
        time.sleep(1)
        # 3. Click "Add" button
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(3)
        # Test Steps
        # 1. Click text boxes (Employee Name (and click the available option), Username, Password, Confirm Password) and input characters
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Jordan Mathews") 
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_userName").send_keys("jordanmathews") 
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_password").send_keys("jordan890") 
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_confirmPassword").send_keys("jordan890")
        time.sleep(1)
        # 2. Click User Role and Status drop-down lists and input characters
        select = Select(browser.find_element(By.ID,'systemUser_userType'))
        select.select_by_visible_text('ESS')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'systemUser_status')) 
        select.select_by_visible_text('Enabled')
        time.sleep(1)
        # 3. Click "Save" button
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(3)
        
        # validation
        validation = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div/form/div[4]/table/tbody").text
        
        # Successfully saved
        self.assertIn('Jordan Mathews', validation)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()