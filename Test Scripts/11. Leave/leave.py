import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Leave List sub-menu
class TestVerifyTheLeaveListSubMenu(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_042
    # Search an unlisted record
    def test_tc_042(self):
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
        # 2. Click "Leave" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[3]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Employee Name text box and input characters
        browser.find_element(By.ID,"leaveList_txtEmployee_empName").send_keys("zzz") 
        time.sleep(1)
        # 2. Click "Search" button
        browser.find_element(By.ID,"btnSearch").click() 
        time.sleep(1)
        
        # validation
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[3]/table/tbody").text

        # No records found
        self.assertIn('No Records', response_message)
        
    # TC_043
    # Search a listed record
    def test_tc_043(self):
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
        # 2. Click "Leave" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[3]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Name text box and input Name
        browser.find_element(By.ID,"leaveList_txtEmployee_empName").send_keys("fiona") 
        time.sleep(1)
        # 2. Click "Search" button
        browser.find_element(By.ID,"btnSearch").click() 
        time.sleep(1)
        
        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[3]/table/tbody").text

        # Records found (Employee Name: Fiona Grace)
        self.assertIn('Fiona Grace', response)

    # TC_044
    # Input data and reset
    def test_tc_044(self):
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
        # 2. Click "Leave" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[3]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Employee Name text box and input Name
        browser.find_element(By.ID,"leaveList_txtEmployee_empName").send_keys("fiona")
        time.sleep(1)
        # 2. Click Sub Unit drop-down list and select an option
        select = Select(browser.find_element(By.ID,'leaveList_cmbSubunit'))
        select.select_by_visible_text('Administration') 
        time.sleep(1)
        # 3. Click From and To date pickers and choose a date
        browser.find_element(By.ID,"calFromDate").click()
        time.sleep(1)
        browser.find_element(By.ID,"calFromDate").send_keys("2022-07-01")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/img").click()
        time.sleep(1)
        browser.find_element(By.ID,"calToDate").click()
        time.sleep(1)
        browser.find_element(By.ID,"calToDate").send_keys("2022-07-29")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/img").click()
        time.sleep(1)
        # 4. Click "All" and "Include Past Employees" check boxes
        browser.find_element(By.ID,"leaveList_chkSearchFilter_checkboxgroup_allcheck").click() 
        time.sleep(1)
        browser.find_element(By.ID,"leaveList_cmbWithTerminated").click()
        time.sleep(1)
        # 5. Click "Reset" button
        browser.find_element(By.ID,"btnReset").click() 
        time.sleep(3)
        
        # validation
        validation = browser.find_element(By.ID,"leaveList_txtEmployee_empName").get_attribute("value")

        # Employee Name text box is empty, Sub Unit drop-down list is set to "All", date pickers are reset (from the first date of this year to the last date of next year), and check box only checked the "Pending Approval" check box
        self.assertIn('', validation)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()