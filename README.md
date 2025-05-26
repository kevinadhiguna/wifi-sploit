<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/d4v1-sudo/wifi-sploit/raw/master/assets/router.jpg" style="text-align: left ; height:20%; width:20%" />
    <img src="https://github.com/d4v1-sudo/wifi-sploit/raw/master/assets/slash.png" style="text-align: center ; height:20%; width:20%" />
    <img src="https://github.com/d4v1-sudo/wifi-sploit/raw/master/assets/www.jpg" style="text-align: right ; height:20%; width:20%" />
</div>
<h3 style="text-align:center;">WiFi-Sploit</h3>
<p style="text-align:center;">
   🔒 A login cracker for any login page
</p>

**Checkou the new ```beta``` branch**

## About

 - Originally made for `python2` but now just works using `python3`.
 - Originally it was made for router's login pages but it works fine in any login page site, even on internet.

## Prerequisites

1. Your laptop/computer must be **connected to the Wi-Fi** network whose router or site login page will be pentested.
2. A laptop/computer that has `Python 3.x` installed.

### How to install Python/Python3

- [Windows](https://www.python.org/downloads/windows/)
- [MacOS](https://www.python.org/downloads/macos/)
- Linux/Unix (Well.. python comes preinstalled on most Linux distributions. Otherwise, you can download it [here](https://www.python.org/downloads/source/))

<br />

## About the Scripts

Wifi-Sploit provides three scripts:

### wfs.py

- This script performs password brute-forcing on a login page.
- Initially designed for router login pages but works on any login page of a website.
- Requires Python 3.x
- Usage: `python3 wfs.py`.
- Before running, ensure you have the router's IP address, usernames, and passwords.

### wfs-browser.py

- Utilizes Selenium to interact with login pages through a web browser.
- Also designed for router login pages but adaptable to other websites' login pages.
- Requires Python 3.x and Selenium WebDriver.
- Predefined elements with `name` attributes: `username` for user and `password` for password
- Usage: `python3 wfs-browser.py`.

### wfs-browser-input.py

- Another Selenium-based script but with customizable HTML element names.
- Offers more flexibility in specifying HTML element names for username, password, and submit button.
- Useful when the default element names don't match the target webpage's structure.
- Requires Python 3.x and Selenium WebDriver.
- Usage: `python3 wfs-browser-input.py`.
- Allows users to specify HTML element names for username, password, and submit button.

<br />

## Before Running the `wfs-browser.py` and `wfs-browser-input.py`:

- On linux:
```bash
chmod +x /PATH-TO/selenium/webdriver/common/linux/selenium-manager
```
- On windows: just to be sure, run the scripts as administrator

## Running the Scripts

1. Clone this repository:
```bash
git clone https://github.com/kevinadhiguna/wifi-sploit.git
```

2. Change directory to `wifi-sploit`:
```bash
cd wifi-sploit
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```

4. Run the desired script:
   - For `wfs.py`: `python3 wfs.py`
   - For `wfs-browser.py`: `python3 wfs-browser.py`
   - For `wfs-browser-input.py`: `python3 wfs-browser-input.py`

<br />

## Additional Notes

- It is recommended to check out the `address.md` file for the Wi-Fi router's IP address before running the scripts.
- Default usernames and passwords for Wi-Fi routers can be found in the `username.txt` and `password.txt` files, respectively.
- **Important:** The logic implemented in the codes that tells whether a login was successful or not is the absence of a phrase or word in the "expression" set in the codes, so make sure that the phrase that represents a login error on your login page is there and make sure that there are no conflicts with the HTML code, as some words may persist in the HTML even if the login is successful. See more at [HTML.md](HTML.md)
- Make sure to put the correct inputs in `wfs-browser-input.py` for the code to work correctly, See more at [HTML.md](HTML.md)
- Remember, these tools are for educational purposes only. Misuse is not condoned.

<br />
<hr />

## Disclaimer

<b>I am not responsible for any misuse. These tools are only for educational purposes.</b>

<br />

![Hello !](https://api.visitorbadge.io/api/VisitorHit?user=kevinadhiguna&repo=wifi-sploit&label=thanks%20for%20dropping%20in%20!&labelColor=%23000000&countColor=%23FFFFFF)
