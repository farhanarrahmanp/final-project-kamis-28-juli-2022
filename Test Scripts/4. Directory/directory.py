import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Check the Search Directory section
class TestCheckTheSearchDirectorySection(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_019
    # Search an unlisted record
    def test_tc_019(self):
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
        # 2. Click "Directory" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[9]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Name text box and input characters
        browser.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys("xyz") 
        time.sleep(1)
        # 2. Click "Search" button
        browser.find_element(By.ID,"searchBtn").click() 
        time.sleep(1)
        
        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]").text

        # No records found
        self.assertIn('No Records', response)
        
    # TC_020
    # Search a listed record
    def test_tc_020(self):
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
        # 2. Click "Directory" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[9]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Name text box and input Name
        browser.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys("john") 
        time.sleep(1)
        # 2. Click "Search" button
        browser.find_element(By.ID,"searchBtn").click() 
        time.sleep(1)
        
        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[2]/ul/li[1]/b").text

        # Records found
        self.assertIn('John', response)

    # TC_021
    # Input data and reset
    def test_tc_021(self):
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
        # 2. Click "Directory" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[9]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Name text box and input Name
        browser.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys("lisa") 
        time.sleep(1)
        # 2. Click Job Title drop-down list and select an option
        select = Select(browser.find_element(By.ID,'searchDirectory_job_title')) 
        select.select_by_visible_text('QA Engineer') 
        time.sleep(1)
        # 3. Click Location drop-down list and select an option
        select = Select(browser.find_element(By.ID,'searchDirectory_location')) 
        select.select_by_value('3') # Canadian Regional HQ
        time.sleep(1)
        # 4. Click "Reset" button
        browser.find_element(By.ID,"resetBtn").click() 
        time.sleep(1)
        
        # validation
        validation = browser.find_element(By.ID,"searchDirectory_emp_name_empName").get_attribute("value")

        # Name text box is empty and Job Title drop-down list and Location drop-down list are set to "All"
        self.assertIn('', validation)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()