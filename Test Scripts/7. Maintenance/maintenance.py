import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Purge Employee Records sub-menu
class TestVerifyThePurgeEmployeeRecordsSubMenu(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_030
    # No input Password
    def test_tc_030(self):
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
        # 2. Click "Maintenance" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[10]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Verify Password text box
        browser.find_element(By.ID,"confirm_password").click() 
        time.sleep(1)
        # 2. Click "Verify" button
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/div/div/input").click() 
        time.sleep(1)

        # validation
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/div/fieldset/div/ol/li/span").text

        # Cannot verify
        self.assertIn('Required', response_message)

    # TC_031
    # Input invalid Password
    def test_tc_031(self):
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
        # 2. Click "Maintenance" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[10]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Verify Password text box and input Password
        browser.find_element(By.ID,"confirm_password").send_keys("orangexyz") 
        time.sleep(1)
        # 2. Click "Verify" button
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/div/div/input").click() 
        time.sleep(3)

        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/div/fieldset/div/ol/li/label").text
    
        # Cannot verify
        self.assertIn('Verify', response)

    # TC_032
    # Input valid Password
    def test_tc_032(self):
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
        # 2. Click "Maintenance" menu and
        # 3. A valid Password for running TC_007
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[10]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Verify Password text box and input Password
        browser.find_element(By.ID,"confirm_password").send_keys("admin123") 
        time.sleep(1)
        # 2. Click "Verify" button
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/div/div/input").click() 
        time.sleep(3)

        # validation
        response = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[2]/fieldset/div/ol/li/label").text
        
        # Successfully verified
        self.assertIn('Past', response)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()