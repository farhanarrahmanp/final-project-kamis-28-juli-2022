import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Manage Reviews sub-menu
class Test1VerifyTheManageReviewsSubMenu(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_039
    # Search an Employee Name
    def test_tc_039(self):
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
        # 2. Click "Performance" menu
        hover = ActionChains(browser).move_to_element(browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[7]/a/b"))
        hover.perform()
        time.sleep(1)
        hover = ActionChains(browser).move_to_element(browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[7]/ul/li[2]/a"))
        hover.perform()
        time.sleep(1)
        # 3. Click "Manage Reviews" sub-menu
        browser.find_element(By.ID,"menu_performance_searchPerformancReview").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Employee Name text box and input characters and 
        # 2. Click the available option
        browser.find_element(By.ID,"performanceReview360SearchForm_employeeName").send_keys("Fiona Grace") 
        time.sleep(1)
        # 3. Click "Search" button
        browser.find_element(By.ID,"btnSearch").click()
        time.sleep(3)

        # validation
        validation = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/div[4]/table/tbody").text

        # Employee found
        self.assertIn('Fiona Grace', validation)

    # TC_040
    # Input data and reset
    def test_tc_040(self):
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
        # 2. Click "Performance" menu
        hover = ActionChains(browser).move_to_element(browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[7]/a/b"))
        hover.perform()
        time.sleep(1)
        hover = ActionChains(browser).move_to_element(browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[7]/ul/li[2]/a"))
        hover.perform()
        time.sleep(1)
        # 3. Click "Manage Reviews" sub-menu
        browser.find_element(By.ID,"menu_performance_searchPerformancReview").click()
        time.sleep(1)
        # Test Steps
        # 1. Click drop-down lists (Job Title and Status) and choose an option
        select = Select(browser.find_element(By.ID,'performanceReview360SearchForm_jobTitleCode'))
        select.select_by_visible_text('Automation Tester')
        time.sleep(1)
        select = Select(browser.find_element(By.ID,'performanceReview360SearchForm_status'))
        select.select_by_visible_text('All')
        time.sleep(1)
        # 2. Click Employee Name text box, input characters, and click the available option
        browser.find_element(By.ID,"performanceReview360SearchForm_employeeName").send_keys("Fiona Grace")
        time.sleep(1)
        # 3. Click date pickers (From Date and To Date) and choose a date
        browser.find_element(By.ID,"toDate").click()
        time.sleep(1)
        browser.find_element(By.ID,"toDate").send_keys("2022-07-29")
        time.sleep(1)
        browser.find_element(By.ID,"fromDate").click()
        time.sleep(1)
        browser.find_element(By.ID,"fromDate").send_keys("2022-07-01")
        time.sleep(1)
        # 4. Click "Reset" button
        browser.find_element(By.ID,"btnReset").click()
        time.sleep(3)

        # validation
        validation = browser.find_element(By.ID,"performanceReview360SearchForm_employeeName").get_attribute("value")

        # Text box is empty, drop-down lists are set to "All," and date pickers are empty
        self.assertIn('', validation)

    def tearDown(self): 
        self.browser.close()

# Test Scenario: Verify the Add Performance Review page
class Test2VerifyTheAddPerformanceReviewPage(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_041
    # Input a listed Employee
    def test_tc_041(self):
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
        # 2. Click "Performance" menu
        hover = ActionChains(browser).move_to_element(browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[7]/a/b"))
        hover.perform()
        time.sleep(1)
        hover = ActionChains(browser).move_to_element(browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[7]/ul/li[2]/a"))
        hover.perform()
        time.sleep(1)
        # 3. Click "Manage Reviews" sub-menu
        browser.find_element(By.ID,"menu_performance_searchPerformancReview").click()
        time.sleep(1)
        # 4. Click "Add" button
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Employee text box and input characters
        browser.find_element(By.ID,"saveReview360Form_employee").send_keys("Fiona Grace") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[5]/ul/li").click()
        time.sleep(1)
        # validation
        validation = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/div/h4").text
        
        # Another input form is expanded
        self.assertIn('Reviewers', validation)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()