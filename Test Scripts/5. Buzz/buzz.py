import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"

# Test Scenario: Verify the Update Status tab
class Test1VerifyTheUpdateStatusTab(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_022
    # Post without input characters
    def test_tc_022(self):
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
        # 2. Click "Buzz" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[11]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Status text box
        browser.find_element(By.ID,"createPost_content").click() 
        time.sleep(1)
        # 2. Click "Post" button
        browser.find_element(By.ID,"postSubmitBtn").click() 
        time.sleep(1)

        # validation
        post = browser.find_element(By.ID,"buzz").text

        # Cannot post
        self.assertIn('2021', post)

    # TC_023
    # Post with input characters
    def test_tc_023(self):
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
        # 2. Click "Buzz" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[11]/a/b").click()
        time.sleep(1)
        # Test Steps
        # 1. Click Status text box and input characters
        browser.find_element(By.ID,"createPost_content").send_keys("Hello Orange") 
        time.sleep(1)
        # 2. Click "Post" button
        browser.find_element(By.ID,"postSubmitBtn").click() 
        time.sleep(3)

        # validation
        post = browser.find_element(By.ID,"buzz").text
        
        # Successfully posted
        self.assertIn('Hello Orange', post)

    def tearDown(self): 
        self.browser.close()

# Test Scenario: Verify the Upload Images tab
class Test2VerifyTheUploadImagesTab(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_024
    # Input characters without upload an image
    def test_tc_024(self):
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
        # 2. Click "Buzz" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[11]/a/b").click()
        time.sleep(1)
        # 3. Click "Upload Images" tab
        browser.find_element(By.ID,"tabLink2").click()
        time.sleep(1)
        # Test Steps
        # 1. Click text box and input characters
        browser.find_element(By.ID,"phototext").send_keys("Bon Appetit") 
        time.sleep(1)
        # 2. Click "Post" button
        browser.find_element(By.ID,"imageUploadBtn").click() 
        time.sleep(1)

        # validation
        post = browser.find_element(By.ID,"buzz").text

        # Cannot post
        self.assertIn('Hello Orange', post)

    def tearDown(self): 
        self.browser.close()

# Test Scenario: Verify the Share Video tab
class Test3VerifyTheShareVideoTab(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # Test Cases:

    # TC_025
    # Input an invalid URL
    def test_tc_025(self):
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
        # 2. Click "Buzz" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[11]/a/b").click()
        time.sleep(1)
        # 3. Click "Share Video" tab
        browser.find_element(By.ID,"tabLink3").click()
        time.sleep(1)
        # Test Steps
        # 1. Click text box and paste an invalid URL
        browser.find_element(By.ID,"createVideo_content").send_keys("https://www.youtube.com/") 
        time.sleep(1)
        browser.find_element(By.ID,"createVideo_content").send_keys(Keys.COMMAND, 'a') # all
        time.sleep(1)
        browser.find_element(By.ID,"createVideo_content").send_keys(Keys.COMMAND, 'c') # copy
        time.sleep(1)
        browser.find_element(By.ID,"createVideo_content").send_keys(Keys.COMMAND, 'v') # paste
        time.sleep(3)

        # validation
        post = browser.find_element(By.ID,"buzz").text

        # Cannot post
        self.assertIn('Hello Orange', post)

    # TC_026
    # Input a valid URL
    def test_tc_026(self):
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
        # 2. Click "Buzz" menu
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[11]/a/b").click()
        time.sleep(1)
        # 3. Click "Share Video" tab
        browser.find_element(By.ID,"tabLink3").click()
        time.sleep(1)
        # Test Steps
        # 1. Click text box and paste the valid URL
        browser.find_element(By.ID,"createVideo_content").send_keys("https://www.youtube.com/watch?v=5FQWAFaC-tY") 
        time.sleep(1)
        browser.find_element(By.ID,"createVideo_content").send_keys(Keys.COMMAND, 'a')
        time.sleep(1)
        browser.find_element(By.ID,"createVideo_content").send_keys(Keys.COMMAND, 'c')
        time.sleep(1)
        browser.find_element(By.ID,"createVideo_content").send_keys(Keys.COMMAND, 'v')
        time.sleep(1)
        # 2. Click "Save Video" button
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[6]/div[2]/div[1]/div[3]/div[2]/div/div/p/input").click() 
        time.sleep(3)
        
        # validation
        post = browser.find_element(By.ID,"buzz").text

        # Successfully posted
        self.assertIn('https://www.youtube.com/watch?v=5FQWAFaC-tY', post)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()