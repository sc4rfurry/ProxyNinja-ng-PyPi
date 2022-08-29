[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
##
# ProxyNinja-ng
Python3 Module to get https or socks(4/5) proxies by scraping the web.
##
### 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=kali-linux&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.10-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

##

### 📚 Requirements
> - Python 3.9+
> - pip3

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the module.
if not installed, install it using the following command.
```bash
    sudo apt-get install python3-pip
```

> It is advised to install the python requirements in a virtual environment, for that install the venv package.

```bash
    python3 -m pip install venv
    python3 -m venv env
    source env/bin/activate
```
After that run the following commands:
```bash
  python3 -m pip install <pkg> -U
```
 **OR**
```bash
  git clone https://github.com/sc4rfurry/ProxyNinja-ng-PyPi.git
  cd ProxyNinja-ng-PyPi
  python3 -m pip install .
```

    
## Usage/Examples
-----------------------------------------
#### Usage:

==> **Download the proxies**

```python
#!/usr/bin/python3
from proxy_ninja_ng import fetch_proxies

fetch_proxies(PROXY_TYPE, OUTPUT_FILENAME, OUTPUT_FORMAT)
```
- PROXY_TYPE: https/socks4/socks5
- OUTPUT_FILENAME: Enter the filename
- OUTPUT_FORMAT: txt/json

> proxies gonna save in parent dir.

#### Example:
```python
#!/usr/bin/python3
from proxy_ninja_ng import fetch_proxies

fetch_proxies("socks", "socks_proxy", "json")
```
##
==> **Get proxies as json**
```python
#!/usr/bin/python3
from proxy_ninja_ng import fetch_proxies_json

json_list = fetch_proxies_json(PROXY_TYPE)
print(json_list)
```
- PROXY_TYPE: https/socks4/socks5

> This will gonna return a json list.

#### Example:
```python
#!/usr/bin/python3
from proxy_ninja_ng import fetch_proxies_json

json_list = fetch_proxies_json("https")
print(json_list)
```
##
==> **Get proxies List**
```python
#!/usr/bin/python3
from proxy_ninja_ng import fetch_proxies_list

_list = fetch_proxies_list(PROXY_TYPE)
print(_list)
```
- PROXY_TYPE: https/socks4/socks5

> This will gonna return a list.

#### Example:
```python
#!/usr/bin/python3
from proxy_ninja_ng import fetch_proxies_list

lst = fetch_proxies_list("https")
print(lst)
```

## Features

- Fetch proxies from different url's and api's.
- Fast, using request lib. 
- save output in txt or json format.
- User Friendly. :D
##
> **Note:** If you are interested in implementing this using **Selenium/ChromiumDriver**, please check this [Project](https://github.com/sc4rfurry/ProxyNinja---PyPi)
## 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

##

## Feedback

If you have any feedback, please reach out to us at akalucifr@protonmail.ch
