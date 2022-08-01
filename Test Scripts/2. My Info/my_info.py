import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Personal Details
class Test1VerifyThePersonalDetails(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_008
    # Delete all any texts in Full Name text boxes section
    def test_tc_008(self):
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
        # 2. Click "My Info" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[6]/a/b").click()
        time.sleep(1)               
        # Test Steps
        # 1. Click "Edit" button, 
        browser.find_element(By.ID,"btnSave").click() 
        time.sleep(1)
        # click First Name text box, and delete text
        browser.find_element(By.ID,"personal_txtEmpFirstName").clear() 
        time.sleep(1)
        # 2. Click Middle Name text box and delete text (if any)
        browser.find_element(By.ID,"personal_txtEmpMiddleName").clear() 
        time.sleep(1)
        # 3. Click Last Name text box and delete text
        browser.find_element(By.ID,"personal_txtEmpLastName").clear() 
        time.sleep(1)
        # 4. Click "Save" button
        browser.find_element(By.ID,"btnSave").click() 
        time.sleep(1)
        
        # validation
        response_message_FN = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol[1]/li/ol/li[1]/span").text
        response_message_LN = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol[1]/li/ol/li[3]/span").text

        # Cannot save
        self.assertIn('Required', response_message_FN)
        self.assertIn('Required', response_message_LN)

    # TC_009
    # Delete all any deletable values in input elements (including date pickers and check box) (except First Name text box, Last Name text box, radio buttons, and drop-down lists)
    def test_tc_009(self):
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
        # 2. Click "My Info" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[6]/a/b").click()
        time.sleep(1)               
        # Test Steps
        # "1. Click ""Edit"" button, click input elements, and delete values (if any):
        browser.find_element(By.ID,"btnSave").click() 
        time.sleep(1)
        ids = [
                "personal_txtEmpMiddleName", # - Middle Name
                "personal_txtEmployeeId", # - Employee Id
                "personal_txtLicenNo", # - Driver's License Number
                "personal_txtNICNo", # - SSN Number
                "personal_txtOtherID", # - Other Id
                "personal_txtLicExpDate", # - License Expiry Date
                "personal_txtSINNo", # - SIN Number
                "personal_DOB", # - Date of Birth
                "personal_txtEmpNickName", # - Nick Name
                "personal_txtMilitarySer" # - Military Service
        ]
        for anid in ids:
            browser.find_element(By.ID,anid).clear()
            time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol[4]").click()
        time.sleep(1)
        x = browser.find_element(By.ID,"personal_chkSmokeFlag").is_selected() # - Smoker" 
        if x == True:
            browser.find_element(By.ID,"personal_chkSmokeFlag").click()
            time.sleep(1)
        # 2. Click "Save" button
        browser.find_element(By.ID,"btnSave").click() 
        time.sleep(1)
        
        # validation
        validation = browser.find_element(By.ID,"btnSave").get_attribute("value")

        # Successfully saved
        self.assertIn('Edit', validation)

    def tearDown(self): 
        self.browser.close()

# Test Scenario: Verify the Attachments
class Test2VerifyTheAttachments(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_010
    # Add Description in an attachment
    def test_tc_010(self):
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
        # 2. Click "My Info" menu and 3. File Name "jmeter.log" is attached
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[6]/a/b").click()
        time.sleep(1)               
        # Test Steps
        # 1. Click "Edit" link
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[5]/div[2]/form/table/tbody/tr[3]/td[8]/a").click() 
        time.sleep(1)
        # 2. Add text
        browser.find_element(By.ID,"txtAttDesc").send_keys("hello orange") 
        time.sleep(1)
        # 3. Click "Save Comment Only" button
        browser.find_element(By.ID,"btnCommentOnly").click() 
        time.sleep(1)

        # validation
        file_name = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[5]/div[2]/form/table/tbody/tr[3]/td[2]/a").text
        description = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[5]/div[2]/form/table/tbody/tr[3]/td[3]").text

        # Successfully saved
        self.assertIn('jmeter', file_name)
        self.assertIn('hello orange', description)

    # TC_011
    # Delete attachments
    def test_tc_011(self):
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
        # 2. Click "My Info" menu and 3. There is an attachment
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[6]/a/b").click()
        time.sleep(1)               
        # Test Steps
        # 1. Click attachments check box
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[5]/div[2]/form/table/tbody/tr[1]/td[1]/input").click() 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[5]/div[2]/form/table/tbody/tr[2]/td[1]/input").click()
        time.sleep(1)
        # 2. Click "Delete" button
        browser.find_element(By.ID,"btnDeleteAttachment").click() 
        time.sleep(1)

        # validation
        file_name = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[5]/div[2]/form/table/tbody/tr[1]/td[2]/a").text
        description = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[5]/div[2]/form/table/tbody/tr[1]/td[3]").text

        # Successfully deleted
        self.assertIn('jmeter', file_name)
        self.assertIn('hello orange', description)

    # TC_012
    # Add an empty attachment
    def test_tc_012(self):
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
        # 2. Click "My Info" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[6]/a/b").click()
        time.sleep(1)               
        # Test Steps
        # 1. Click "Add" button
        browser.find_element(By.ID,"btnAddAttachment").click()
        time.sleep(1)
        # 2. Click "Upload" button
        browser.find_element(By.ID,"btnSaveAttachment").click() 
        time.sleep(1)

        # validation
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[4]/div[2]/form/fieldset/ol/li[2]/span").text

        # Cannot upload
        self.assertIn('Required', response_message)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()