def install():    
    # Install a Selenium library first (https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Browser services imports
    from selenium.webdriver.chrome.service import Service as ChromeService

    # Browser options imports
    from selenium.webdriver.chrome.options import Options as ChromeOptions

    # Installing browser drivers (https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#1-driver-management-software)
    from webdriver_manager.chrome import ChromeDriverManager
    # New syntx (https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python)
    service = ChromeService(ChromeDriverManager().install())

    # Test install driver (https://github.com/SeleniumHQ/seleniumhq.github.io/blob/dev/examples/python/tests/getting_started/test_install_drivers.py)
    #def test_chrome_session():
    #   service = ChromeService(executable_path=ChromeDriverManager().install())
    #  driver = webdriver.Chrome(service=service)
    # driver.quit()

    # Open and close a browser with Selenium
    options = ChromeOptions()

    def test_chrome_session():
        driver = webdriver.Chrome(options=options)
        driver.quit()

    # Defining browser
    driver = webdriver.Chrome(service=service)

    # Maximize window
    driver.maximize_window()

    # Going to webpage
    driver.get("http://localhost/")