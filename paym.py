import time
import random
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass

def stealth_delay():
    time.sleep(random.uniform(2, 5))

def browser_automation_attack(email, password):
    print("Initializing browser automation...")  # Debugging line
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    try:
        # Make sure ChromeDriver installs and the correct version is used
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        print("WebDriver initialized.")  # Debugging line
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return
    
    driver.get("https://www.paypal.com/signin")
    stealth_delay()

    try:
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

        # Check if login was successful
        if "summary" in driver.current_url:
            print("Login successful! Launching Chrome with session...")
            cookies = driver.get_cookies()
            driver.quit()
            launch_chrome_with_session(email, cookies)
        else:
            print("Login failed or 2FA required.")
            driver.quit()
    except Exception as e:
        print(f"Error during login automation: {e}")
        driver.quit()

def launch_chrome_with_session(email, cookies):
    chrome_command = f"google-chrome --new-tab 'https://www.paypal.com/signin?email={email}'"
    subprocess.Popen(chrome_command, shell=True)
    print("Chrome launched with PayPal session.")

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
            print("Network interception attack is not yet implemented.")
        elif choice == '3':
            print("Exiting script.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
