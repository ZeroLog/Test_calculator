import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOnlineSchool(unittest.TestCase):
    def setUp(self):
        self.sitetest = "https://ru.onlinemschool.com/"
        self.file_path = r"C:\Users\ZeroLog\Documents\testlog\test.log"
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        self.driver.quit()

    def to_file(self, text):
        try:
            with open(self.file_path, 'a') as file:
                file.write(text + '\n')
            print(f"Text appended to {self.file_path}")
        except FileNotFoundError:
            with open(self.file_path, 'w') as file:
                file.write(text + '\n')
            print(f"File {self.file_path} created, and text appended")

    def test1(self):
        self.to_file("Test 1 start")
        self.driver.get(self.sitetest)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[3]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/div[1]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[4]/a[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_kilotonne"]'))).send_keys(1)
        element = self.wait.until(EC.visibility_of_element_located((By.ID, 'oms_tonne')))
        value = int(element.get_attribute('value'))
        if value == 1000:
            self.to_file("Test 1 passed")
        else:
            self.to_file("Test 1 failed")
#Find X percentage of number Y.
    def test2(self):
        self.to_file("Test 2 start")
        self.driver.get(self.sitetest)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[3]/a/div/div[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/div[4]/img'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/a[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_c1"]'))).send_keys(10)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_c2"]'))).send_keys(10)
        time.sleep(3)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@onclick="percent1(\'oms_c\')"]'))).click()
        result_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="res_main_t"]/center/div')))
        result_text = result_element.text
        last_digit = result_text[-1]
        if last_digit == "1":
            self.to_file("Test 2 passed")
        else:
            self.to_file("Test 2 failed")
 #standart calc           
    def test3(self):
        self.to_file("Test 3 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_rgh1t"]/div[1]/table/tbody/tr[3]/td[2]/input'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_rgh1t"]/div[1]/table/tbody/tr[6]/td[3]/input'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_rgh1t"]/div[1]/table/tbody/tr[3]/td[2]/input'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_rgh1t"]/div[1]/table/tbody/tr[6]/td[4]/input'))).click()
        element=self.wait.until(EC.visibility_of_element_located((By.ID, 'oms_calc_res')))
        value = element.text
        if value =="16":
            self.to_file("Test 3 passed")
        else:
            self.to_file("Test 3 failed")
#search test
    def test4(self):
        self.to_file("Test 4 start")
        self.driver.get(self.sitetest) 
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[1]/div/div[1]/div/div/div'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gsc-i-id1"]'))).send_keys("Минор и алгебраическое дополнение матрицы.")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="___gcse_0"]/div/form/table/tbody/tr/td[2]/button'))).click()
        time.sleep(1)
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="___gcse_1"]/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div/div[1]/div/a/b')))
        value=element.text
        print(value)
        if value =="Минор и алгебраическое дополнение матрицы":
            self.to_file("Test 4 passed")
        else:
            self.to_file("Test 4 failed")
            
        

        


    
        

if __name__ == "__main__":
    suite = unittest.TestSuite()

   
    suite.addTest(TestOnlineSchool('test1'))
    suite.addTest(TestOnlineSchool('test2'))
    suite.addTest(TestOnlineSchool('test3'))
    suite.addTest(TestOnlineSchool('test4'))

    unittest.TextTestRunner().run(suite)
