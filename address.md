## Router's IP address

This tool requires one to connect to a Wi-Fi whose router is pentested. Therefore, figuring out the router's IP address in the network (Local Area Network) is a must. 

<br />

### Windows

In Windows, you can open Command Prompt (CMD) then execute `ipconfig` to see router's IP address.

<br />

### MacOS

1. Click the Wi-Fi symbol on the menu bar.
2. Click **Network Preferences**.
3. On the **Wi-Fi** tab, click **Advanced** button.
4. Press on **TCP/IP** tab, your Wi-Fi router IP address will be listed under the Router.

<br />

### Linux

Based on [this answer on StackOverflow](https://askubuntu.com/a/605476), try one of these commands : 

```bash
netstat -nr | awk '$1 == "0.0.0.0"{print$2}'
```

```bash
ip route show | grep -i 'default via'| awk '{print $3 }'
```

The output should look like `192.168.1.1` that indicates the Internet Gateway of your Local Area Network (Wi-Fi).

<br />
<hr />

<br />

## Default router's IP address

Here is some routers' IP addresses :

|    <br>Router Brand<br>   |                                                                                           <br>Login IP<br>                                                                                          |
|:-------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 2Wire                     | 192.168.1.1<br>192.168.0.1<br>192.168.1.254<br>10.0.0.138                                                                                                                                           |
| 3Com                      | 192.168.1.1<br>192.168.1.10.1                                                                                                                                                                       |
| Actiontec                 | 192.168.1.1<br>192.168.0.1<br>192.168.2.1<br>192.168.254.254                                                                                                                                        |
| Airlink                   | 192.168.1.1<br>192.168.2.1                                                                                                                                                                          |
| Airlive                   | 192.168.2.1                                                                                                                                                                                         |
| Airties                   | 192.168.2.1                                                                                                                                                                                         |
| Apple                     | 10.0.1.1                                                                                                                                                                                            |
| Amped Wireless            | 192.168.3.1                                                                                                                                                                                         |
| Asus                      | 192.168.1.1<br>192.168.2.1<br>10.10.1.1                                                                                                                                                             |
| Aztech                    | 192.168.1.1<br>192.168.2.1<br>192.168.1.254<br>192.168.254.254                                                                                                                                      |
| Belkin                    | 192.168.1.1<br>192.168.2.1<br>10.0.0.2<br>10.1.1.1                                                                                                                                                  |
| Billion                   | 192.168.1.254<br>10.0.0.2                                                                                                                                                                           |
| Buffalo                   | 192.168.1.1<br>192.168.11.1                                                                                                                                                                         |
| Dell                      | 192.168.1.1                                                                                                                                                                                         |
| Cisco                     | 192.168.1.1<br>192.168.0.30<br>192.168.0.50<br>10.0.0.1<br>10.0.0.2                                                                                                                                 |
| D-Link                    | 192.168.1.1<br>192.168.0.1<br>192.168.0.10<br>192.168.0.101<br>192.168.0.30<br>192.168.0.50<br>192.168.1.254<br>192.168.15.1<br>192.168.254.254<br>10.0.0.1<br>10.0.0.2<br>10.1.1.1<br>10.90.90.90  |
| Edimax                    | 192.168.2.1                                                                                                                                                                                         |
| Eminent                   | 192.168.1.1<br>192.168.0.1<br>192.168.8.1                                                                                                                                                           |
| Gigabyte                  | 192.168.1.254                                                                                                                                                                                       |
| Hawking                   | 192.168.1.200<br>192.168.1.254                                                                                                                                                                      |
| Huawei                    | 192.168.1.1<br>192.168.0.1<br>192.168.3.1<br>192.168.8.1<br>192.168.100.1<br>10.0.0.138                                                                                                             |
| Indihome                  | 192.168.1.1<br>192.168.1.254<br>192.168.1.253<br>192.168.100.1                                                                                                                                      |
| LevelOne                  | 192.168.0.1<br>192.168.123.254                                                                                                                                                                      |
| Linksys                   | 192.168.1.1<br>192.168.0.1<br>192.168.1.10<br>192.168.1.210<br>192.168.1.254<br>192.168.1.99<br>192.168.15.1<br>192.168.16.1<br>192.168.2.1                                                         |
| Microsoft                 | 192.168.2.1                                                                                                                                                                                         |
| Motorola                  | 192.168.0.1<br>192.168.10.1<br>192.168.15.1<br>192.168.20.1<br>192.168.30.1<br>192.168.62.1<br>192.168.100.1<br>192.168.102.1<br>192.168.1.254                                                      |
| MSI                       | 192.168.1.254                                                                                                                                                                                       |
| Netgear                   | 192.168.0.1<br>192.168.0.227                                                                                                                                                                        |
| NetComm                   | 192.168.1.1<br>192.168.10.50<br>192.168.20.1<br>10.0.0.138                                                                                                                                          |
| Netopia                   | 192.168.0.1<br>192.168.1.254                                                                                                                                                                        |
| Planet                    | 192.168.1.1<br>192.168.0.1<br>192.168.1.254                                                                                                                                                         |
| Repotec                   | 192.168.1.1<br>192.168.10.1<br>192.168.16.1<br>192.168.123.254                                                                                                                                      |
| Senao                     | 192.168.0.1                                                                                                                                                                                         |
| Siemens                   | 192.168.1.1<br>192.168.0.1<br>192.168.1.254<br>192.168.2.1<br>192.168.254.254<br>10.0.0.138<br>10.0.0.2                                                                                             |
| Sitecom                   | 192.168.0.1<br>192.168.1.254<br>192.168.123.254<br>10.0.0.1                                                                                                                                         |
| SMC Networks              | 192.168.1.1<br>192.168.0.1<br>192.168.2.1<br>10.0.0.1<br>10.1.10.1                                                                                                                                  |
| Sonicwall                 | 192.168.0.3<br>192.168.168.168                                                                                                                                                                      |
| SpeedTouch                | 10.0.0.138<br>192.168.1.254                                                                                                                                                                         |
| Sweex                     | 192.168.15.1<br>192.168.50.1<br>192.168.55.1<br>192.168.251.1                                                                                                                                       |
| Tenda                     | 192.168.1.1<br>192.168.0.1                                                                                                                                                                          |
| Thomson                   | 192.168.0.1<br>192.168.1.254<br>192.168.100.1                                                                                                                                                       |
| TP-Link                   | 192.168.1.1<br>192.168.0.1<br>192.168.0.254                                                                                                                                                         |
| Trendnet                  | 192.168.1.1<br>192.168.0.1<br>192.168.0.30<br>192.168.0.100<br>192.168.1.100<br>192.168.1.254<br>192.168.10.1<br>192.168.10.10<br>192.168.10.100<br>192.168.2.1<br>192.168.223.100<br>200.200.200.5 |
| U.S. Robotics             | 192.168.1.1<br>192.168.2.1<br>192.168.123.254                                                                                                                                                       |
| Zoom                      | 192.168.1.1<br>192.168.2.1<br>192.168.4.1<br>192.168.10.1<br>192.168.1.254<br>10.0.0.2<br>10.0.0.138                                                                                                |
| ZTE                       | 192.168.1.1<br>192.168.0.1<br>192.168.100.100<br>192.168.1.254<br>192.168.2.1<br>192.168.2.254                                                                                                      |
| Zyxel                     | 192.168.1.1<br>192.168.0.1<br>192.168.2.1<br>192.168.4.1<br>192.168.10.1<br>192.168.1.254<br>192.168.254.254<br>10.0.0.2<br>10.0.0.138                                                              |
<br />

>"Why most of them starts with 192.168.XXX.XXX ?", "Also why 10.XXX.XXX.XXX ?"

<br />

According to [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918#section-3), The Internet Assigned Numbers Authority (IANA), an organization that controls global IP address allocation, DNS management, and other Internet-related things, has reserved the following three blocks of the IP address space for private internets:
- **10.0.0.0    - 10.255.255.255**  (10/8 prefix)
- **172.16.0.0  - 172.31.255.255**  (172.16/12 prefix)
- **192.168.0.0 - 192.168.255.255** (192.168/16 prefix)

By the way, RFC that stands for Request for Comments, is simply a kind of a standard of the Internet published by IETF.

<br />

Sources :
- [iana.org](https://www.iana.org/)
- [What is RFC ? - Wikipedia](https://en.wikipedia.org/wiki/Request_for_Comments)
