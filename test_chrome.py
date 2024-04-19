from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class ChromeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_first_pizza(self):
        self.driver.get("http://127.0.0.1:5000/picy")
        text_prvni_pizzy = self.driver.find_element(By.XPATH, "//ol/li[1]").text 
        self.assertEqual(text_prvni_pizzy, "čoky: 123")

    def test_pridat_pizzu(self):
        self.driver.get("http://127.0.0.1:5000/pridej")
        self.driver.find_element(By.NAME, "nazev").clear()
        self.driver.find_element(By.NAME, "nazev").send_keys("Testova")
        self.driver.find_element(By.NAME, "cena").clear()
        self.driver.find_element(By.NAME, "cena").send_keys("200")
        self.driver.find_element(By.TAG_NAME, "button").click()

        self.driver.get("http://127.0.0.1:5000/picy")
        nova_pizza = self.driver.find_element(By.XPATH, "//ol/li[last()]").text 
        self.assertEqual(nova_pizza, "Testova: 200")



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()