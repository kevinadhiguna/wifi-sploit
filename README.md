<br />
<div align="center">
  <img src="https://github.com/kevinadhiguna/wifi-sploit/blob/master/assets/wifi-sploit.png" />
  <h3 align="center">Wi-Fi Sploit</h3>

  <p align="center">
   🔒 A password cracker for an admin page of a Wi-Fi router
  </p>
</div>

<br />

## Status

🚧 Currently under development, originally created using Python 2.7 but trying to make it compatible with Python 3.

<br />

## Prerequisites

1. Your laptop/computer must be **connected to Wi-Fi** whose router will be pentested.
2. A laptop/computer that has `python` or `python3` installed.

### How to install Python/Python3

- [Windows](https://www.python.org/downloads/windows/)
- [MacOS](https://www.python.org/downloads/macos/)
- Linux/Unix (Well.. python comes preinstalled on most Linux distributions. Otherwise you can download it here: https://www.python.org/downloads/source/)

<br />

## Before running the program..

- It is recommended to have a look at [address.md](https://github.com/kevinadhiguna/wifi-sploit/blob/master/address.md) to check Wi-Fi router's IP address.
- Some default Wi-Fi router's usernames : [username.txt](https://github.com/kevinadhiguna/wifi-sploit/blob/master/username.txt)
- Some default Wi-Fi router's passwords : [password.txt](https://github.com/kevinadhiguna/wifi-sploit/blob/master/password.txt)

<br />

## How to Run :
1. Clone this repository :
```bash
git clone https://github.com/kevinadhiguna/wifi-sploit.git
```

<br />

2. Change directory to `wifi-sploit` : 
```bash
cd wifi-sploit
```

<br />

3. Install dependencies :
```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```

<br />

4. Run this program.

<br />

If you are sure about `Wi-Fi router's IP address` and `username`, try running :
```bash
python wfs.py
```

Note: You can also run it with python3. In case of that, just replace `python` with `python3`.

<br/>

5. You will see the appropriate password. Otherwise, the correct password may not be listed in the `password.txt`. In that case, you can add the most commonly used password in the `password.txt`.

<br />
<hr />

## Disclaimer

<b>I am not responsible for any misuse. This tool is only for educational purpose.</b>

![Hello !](https://api.visitorbadge.io/api/VisitorHit?user=kevinadhiguna&repo=wifi-sploit&label=thanks%20for%20dropping%20in%20!&labelColor=%23000000&countColor=%23FFFFFF)
