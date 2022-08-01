import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Candidates sub-menu
class Test1VerifyTheCandidatesSubMenu(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_027
    # Search a Candidate Name
    def test_tc_027(self):
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
        # 2. Click "Recruitment" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[5]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Candidate Name text box and input characters and 
        # 2. Click the available option
        browser.find_element(By.ID,"candidateSearch_candidateName").send_keys("Charles Hayware") 
        time.sleep(1)
        # 3. Click "Search" button
        browser.find_element(By.ID,"btnSrch").click() 
        time.sleep(3)

        # validation
        validation = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody").text

        # Candidate found
        self.assertIn('Charles Hayware', validation)

    # TC_028
    # Input data and reset
    def test_tc_028(self):
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
        # 2. Click "Recruitment" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[5]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click drop-down lists (Job Title, Vacancy, Hiring Manager, Status, and Method of Application) and choose an option
        select = Select(browser.find_element(By.ID,'candidateSearch_jobTitle'))
        select.select_by_visible_text('Automation Tester')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'candidateSearch_jobVacancy'))
        select.select_by_visible_text('All')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'candidateSearch_hiringManager'))
        select.select_by_visible_text('All')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'candidateSearch_status'))
        select.select_by_visible_text('Hired')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'candidateSearch_modeOfApplication'))
        select.select_by_visible_text('Online')
        time.sleep(1)
        # 2. Click Candidate Name text box, input characters, and click the available option
        browser.find_element(By.ID,"candidateSearch_candidateName").send_keys("Peter Smith")
        time.sleep(1)
        # 3. Click date pickers (Date of Application: From and To) and choose a date
        browser.find_element(By.ID,"candidateSearch_fromDate").click()
        time.sleep(1)
        browser.find_element(By.ID,"candidateSearch_fromDate").send_keys("2022-07-01")
        time.sleep(1)
        browser.find_element(By.ID,"candidateSearch_toDate").click()
        time.sleep(1)
        browser.find_element(By.ID,"candidateSearch_toDate").send_keys("2022-07-29")
        time.sleep(1)
        # 4. Click "Reset" button
        browser.find_element(By.ID,"btnRst").click()
        time.sleep(3)

        # validation
        validation = browser.find_element(By.ID,"candidateSearch_candidateName").get_attribute("value")

        # Text boxes are empty, drop-down lists are set to "All," and date pickers are empty
        self.assertIn('', validation)

    def tearDown(self): 
        self.browser.close()

# Test Scenario: Verify the Add Candidate page
class Test2VerifyTheAddCandidatePage(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_029
    # Input data only in Required text box
    def test_tc_029(self):
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
        # 2. Click "Recruitment" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[5]/a/b").click()
        time.sleep(1)
        # 3. Click "Add" button
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        # Test Steps
        # 1. Click First Name text box and input characters
        browser.find_element(By.ID,"addCandidate_firstName").send_keys("Sanbercode") 
        time.sleep(1)
        # 2. Click Last Name text box and input characters
        browser.find_element(By.ID,"addCandidate_lastName").send_keys("QA") 
        time.sleep(1)
        # 3. Click Email text box and input Email
        browser.find_element(By.ID,"addCandidate_email").send_keys("sqa@gmail.com") 
        time.sleep(1)
        # 4. Click "Save" button
        browser.find_element(By.ID,"btnSave").click() 
        time.sleep(3)
        
        # validation
        browser.find_element(By.ID,"menu_recruitment_viewCandidates").click()
        time.sleep(3)
        validation = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody").text
        
        # Successfully saved
        self.assertIn('Sanbercode QA', validation)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()