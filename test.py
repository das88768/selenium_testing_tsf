import os
import unittest
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options   
from selenium.webdriver.support.select import Select  
from selenium.common.exceptions import NoSuchElementException 


class TheSparksFoundation(unittest.TestCase):
    
    # Setup the selenium driver to control the browser by the Robot.
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        url = "https://www.thesparksfoundationsingapore.org/"
        self.driver.get(url)

    # # Test the Title of the website.
    # def test_1_verify_title(self):
    #     self.driver.find_element(By.XPATH, '//*[@id="home"]/div/div[1]/h1/a').click()
    #     assert True

    # # Test the Logo the website.
    # def test_2_verify_logo(self):
    #     self.driver.find_element(By.CLASS_NAME, 'navbar-brand')
    #     assert True

    # # Test the NavBar of the website.
    # def test_3_verify_navbar(self):
    #     self.driver.find_element(By.XPATH, '//*[@id="home"]/div/div[1]')
    #     assert True


    # # Test to Verify About Us page.
    # def test_4_verify_AboutUs_page(self):
    #     self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[1]/a').click()
    #     time.sleep(2)

    #     elements = self.driver.find_elements(By.XPATH, '//*[@id="link-effect-3"]/ul/li[1]/ul')

    #     # Collect all the elements present in the About Us drop down menu.
    #     elm_list = []
    #     for element in elements:
    #         elm_list.append(element.text.split('\n'))

    #     elm_list = elm_list[0]

    #     # Navigate through all the links present in the About Us drop down menu.
    #     for elm in elm_list:
    #         self.driver.find_element(By.LINK_TEXT, f'{elm}').click()
    #         time.sleep(3)

    #         self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[1]/a').click()
    #         time.sleep(2)
        
    #     assert True


    # # Test to verify Policies and Code page.
    # def test_5_verify_Policies_and_Code_page(self):
    #     self.driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[2]/a').click()
    #     time.sleep(2)

    #     elements = self.driver.find_elements(By.XPATH, '//*[@id="link-effect-3"]/ul/li[2]/ul')

    #     # Collect all the elements present in the Policies and Code drop down menu.
    #     elm_list = []
    #     for element in elements:
    #         elm_list.append(element.text.split('\n'))

    #     elm_list = elm_list[0]

    #     # Navigate through all the links present in the Policies and Code drop down menu.
    #     for elm in elm_list:
    #         self.driver.find_element(By.LINK_TEXT, f'{elm}').click()
    #         time.sleep(3)

    #         self.driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[2]/a').click()
    #         time.sleep(2)
        
    #     assert True

    # # Test to verify Programs page.
    # def test_6_verify_Programs_page(self):
    #     self.driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[3]/a').click()
    #     time.sleep(2)

    #     elements = self.driver.find_elements(By.XPATH, '//*[@id="link-effect-3"]/ul/li[3]/ul')

    #     # Collect all the elements present in the Programs drop down menu.
    #     elm_list = []
    #     for element in elements:
    #         elm_list.append(element.text.split('\n'))

    #     elm_list = elm_list[0]

    #     # Navigate through all the links present in the Programs drop down menu.
    #     for elm in elm_list:
    #         self.driver.find_element(By.LINK_TEXT, f'{elm}').click()
    #         time.sleep(3)

    #         self.driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[3]/a').click()
    #         time.sleep(2)
        
    #     assert True


    # # Test to verify Links page.
    # def test_7_verify_Links_page(self):
    #     self.driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[4]/a').click()
    #     time.sleep(2)

    #     elements = self.driver.find_elements(By.XPATH, '//*[@id="link-effect-3"]/ul/li[4]/ul')

    #     # Collect all the elements present in the Links drop down menu.
    #     elm_list = []
    #     for element in elements:
    #         elm_list.append(element.text.split('\n'))

    #     elm_list = elm_list[0]

    #     # Navigate through all the links present in the Links drop down menu.
    #     for elm in elm_list:
    #         self.driver.find_element(By.LINK_TEXT, f'{elm}').click()
    #         time.sleep(3)

    #         self.driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[4]/a').click()
    #         time.sleep(2)
        
    #     assert True
    

    # # Test to verify Join Us page.
    # def test_8_verify_JoinUs_page(self):
    #     self.driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[5]/a').click()
    #     time.sleep(2)

    #     elements = self.driver.find_elements(By.XPATH, '//*[@id="link-effect-3"]/ul/li[5]/ul')

    #     # Collect all the elements present in the Join Us drop down menu.
    #     elm_list = []
    #     for element in elements:
    #         elm_list.append(element.text.split('\n'))

    #     elm_list = elm_list[0]

    #     # Navigate through all the links present in the Join Us drop down menu.
    #     for elm in elm_list:
    #         self.driver.find_element(By.LINK_TEXT, f'{elm}').click()
    #         time.sleep(3)

    #         self.driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[5]/a').click()
    #         time.sleep(2)
        
    #     assert True


    # # Test to verify Contact Us page.
    # def test_9_verify_ContactUs_page(self):
    #     self.driver.find_element(By.XPATH, '//*[@id="link-effect-3"]/ul/li[6]/a').click()
    #     time.sleep(3)

    #     assert True


    # # Test to verify Join Us Form Fillup.
    # def test_10_Fill_JoinUs_Form(self):
    #     self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[5]/a').click()
    #     time.sleep(2)

    #     self.driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[5]/ul/li[1]/a').click()
    #     time.sleep(2)

    #     # Window scroll down the web page to a specified height.
    #     self.driver.execute_script("window.scrollTo(0, 800)")
    #     time.sleep(3)

    #     # Robot enter the details in the input form.
    #     name = self.driver.find_element(By.NAME, 'Name')
    #     name.send_keys("Akash Das")
    #     time.sleep(2)

    #     email_or_phone = self.driver.find_element(By.NAME, 'Email')
    #     email_or_phone.send_keys("das88764@gmail.com")
    #     time.sleep(2)

    #     # Selects options from the drop down menu in the form.
    #     option = Select(self.driver.find_element(By.CLASS_NAME, 'form-control'))
    #     option.select_by_visible_text('Intern')
    #     time.sleep(2)

    #     self.driver.find_element(By.CLASS_NAME, 'button-w3layouts').click()
    #     time.sleep(4)

    #     assert True


    def test_11_KnowMore_btn(self):
        self.driver.execute_script("window.scrollTo(0, 450)")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/a').click()
        time.sleep(2)

        assert True

    def tearDown(self):
        self.driver.close()
        print("Test Completed!")

if __name__ == "__main__":
    unittest.main()