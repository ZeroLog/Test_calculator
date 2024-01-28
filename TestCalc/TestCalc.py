import unittest
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
            #
    def test_test1(self):
        self.to_file("Test 1 start")
        self.driver.get(self.sitetest)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_body1"]/header/nav/div[2]/div[3]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[3]/div[1]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_center_block"]/div[4]/a[2]'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oms_kilotonne"]'))).send_keys(1)
        element = self.wait.until(EC.visibility_of_element_located((By.ID, 'oms_tonne')))
        value = int(element.get_attribute('value'))
        print(value)
        if value == 1000:
            self.to_file("Test 1 passed")
        else:
            self.to_file("Test 1 failed")

if __name__ == "__main__":
    unittest.main()