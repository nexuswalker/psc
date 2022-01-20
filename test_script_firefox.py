# Install a Selenium library first (https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)
from selenium import webdriver
from selenium.webdriver.common.by import By

# Browser services imports
from selenium.webdriver.firefox.service import Service as FirefoxService

# Browser options imports
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Installing browser driver (https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#1-driver-management-software)
from webdriver_manager.firefox import GeckoDriverManager
# New syntx (https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python)
service = FirefoxService(GeckoDriverManager().install())

# Test install driver (https://github.com/SeleniumHQ/seleniumhq.github.io/blob/dev/examples/python/tests/getting_started/test_install_drivers.py)
#def test_firefox_session():
#   service = FirefoxService(executable_path=GeckoDriverManager().install())
#  driver = webdriver.Firefox(service=service)
# driver.quit()

# Open and close a browser with Selenium
options = FirefoxOptions()


def test_firefox_session():
    driver = webdriver.Firefox(options=options)
    driver.quit()


# Defining browser
driver = webdriver.Firefox(service=service)

# Maximize window
driver.maximize_window()

# Going to webpage
driver.get("http://localhost/")

# Print driver title to the terminal
driver.title
print (driver.title)

destination_box = driver.find_element(By.ID, "destination")

destination_box.send_keys("Test")
