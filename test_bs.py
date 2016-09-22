from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class BsTest(unittest.TestCase):
    def setUp(self):
        desired_cap = {'os': 'Windows', 'os_version': 'xp', 'browser': 'IE', 'browser_version': '7.0'}
        self.driver = webdriver.Remote(
            command_executor='http://cibsghtest1:gzufnHpxygmoBR9Y7Qki@hub.browserstack.com:80/wd/hub',
            desired_capabilities=desired_cap)

    def test_bs(self):
        self.driver.get("http://www.google.com")
        if not "Google" in self.driver.title:
            raise Exception("Unable to load google page!")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("BrowserStack")
        elem.submit()
        print self.driver.title

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
