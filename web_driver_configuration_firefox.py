from selenium import webdriver
# Install a Selenium library first (https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)


def installFirefoxDriver():
    # Browser services imports
    from selenium.webdriver.firefox.service import Service as FirefoxService

    # Installing browser driver (https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#1-driver-management-software)
    from webdriver_manager.firefox import GeckoDriverManager
    # New syntx (https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python)

    service = FirefoxService(GeckoDriverManager().install())

    # Test install driver (https://github.com/SeleniumHQ/seleniumhq.github.io/blob/dev/examples/python/tests/getting_started/test_install_drivers.py)
    #def test_firefox_session():
    #   service = FirefoxService(executable_path=GeckoDriverManager().install())
    #  driver = webdriver.Firefox(service=service)
    # driver.quit()

    return service


def installChromeDriver():
    # Browser services imports
    from selenium.webdriver.chrome.service import Service as ChromeService

    # Installing browser drivers
    from webdriver_manager.chrome import ChromeDriverManager
    service = ChromeService(ChromeDriverManager().install())

    # Test install driver (https://github.com/SeleniumHQ/seleniumhq.github.io/blob/dev/examples/python/tests/getting_started/test_install_drivers.py)
    #def test_chrome_session():
     #   service = ChromeService(executable_path=ChromeDriverManager().install())
      #  driver = webdriver.Chrome(service=service)
       # driver.quit()

    return service


def define_driver(url, browser):
    # Defining browser
    if browser == "firefox":
        driver = webdriver.Firefox(service=installFirefoxDriver())
    elif browser == "chrome":
        driver = webdriver.Chrome(service=installChromeDriver())
    else:
        print("Invalid browser name, please use the words firefox or chrome as arguments")
        input("press any key to exit")

    # Maximize window
    driver.maximize_window()

    # Going to webpage
    driver.get(url)

    return driver
