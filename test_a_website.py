#!/usr/bin/python3

import argparse
from pickle import FALSE
import web_driver_configuration_firefox

def main(): #https://stackoverflow.com/questions/39256977/call-a-python-function-in-a-file-with-command-line-argument
    # Parse arguments from command line
    parser = argparse.ArgumentParser()

    # Set up required arguments for this script
    #parser.add_argument('function', type=str, help='function to call')
    parser.add_argument('test_url', type=str, help='test url (example: https://google.com)')
    parser.add_argument('browser_name', type=str, default="firefox", help='browser name, only accepts "firefox" or "chrome" default (default: %(default)s)')

    # Parse the given arguments
    args = parser.parse_args()

    # Get the function based on the command line argument and 
    # call it with the other two command line arguments as 
    # function arguments
    #eval(args.function)(args.url, args.browser)
    args.function = "startTest"
    eval(args.function)(args.test_url, args.browser_name)

def startTest(url, browser):
    # Call driver passing the url and web browser name (firefox or chrome only) as arguemnts
    #driver = web_driver_configuration_firefox.define_driver("http://localhost/", "chrome")
    driver = web_driver_configuration_firefox.define_driver(url, browser)
    driver.minimize_window

if __name__ == '__main__':
    main()    