from selenium import __version__
from selenium import webdriver
print('Selenium has been imported')
print(__version__)
import pytest
print('Pytest has been imported')
print(pytest.__version__)

class ChromeDriverMac():
    # Create a function called test where you'll assign webdriver.Chrome(args) to a variable called "driver".
    # Inside the function apply the get(url) method to driver
    # use this following url: https://www.seleniumeasy.com/test/basic-first-form-demo.html
    def test(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


def main():
    cs = ChromeDriverMac()
    cs.test()


main()