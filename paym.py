import time
import random
import requests
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from mitmproxy.tools.main import mitmweb
from getpass import getpass

def stealth_delay():
    time.sleep(random.uniform(2, 5))

def browser_automation_attack(email, password):
    options = FirefoxOptions()
    # Remove headless mode for debugging (enable it later for stealth)
    # options.add_argument("--headless")
    
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.get("https://www.paypal.com/signin")
    stealth_delay()
    
    email_input = driver.find_element(By.NAME, "login_email")
    email_input.send_keys(email)
    stealth_delay()
    
    next_button = driver.find_element(By.ID, "btnNext")
    next_button.click()
    stealth_delay()
    
    password_input = driver.find_element(By.NAME, "login_password")
    password_input.send_keys(password)
    stealth_delay()
    
    login_button = driver.find_element(By.ID, "btnLogin")
    login_button.click()
    stealth_delay()
    
    if "summary" in driver.current_url:
        print("Login successful! Launching Firefox with session...")
        cookies = driver.get_cookies()
        driver.quit()
        launch_firefox_with_session(email, cookies)
    else:
        print("Login failed or 2FA required.")
        driver.quit()

def launch_firefox_with_session(email, cookies):
    firefox_command = f"firefox --new-tab 'https://www.paypal.com/signin?email={email}'"
    subprocess.Popen(firefox_command, shell=True)
    print("Firefox launched with PayPal session.")

def network_interception_attack():
    print("Starting network interception attack...")
    subprocess.Popen(["mitmproxy", "-w", "paypal_traffic.log"])

def main():
    print("PayPal Security Testing Script")
    email = input("Enter PayPal email: ")
    password = getpass("Enter PayPal password: ")
    
    while True:
        print("\nSelect an attack method:")
        print("1. Browser Automation Attack")
        print("2. Network Interception Attack")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            browser_automation_attack(email, password)
        elif choice == '2':
            network_interception_attack()
        elif choice == '3':
            print("Exiting script.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
