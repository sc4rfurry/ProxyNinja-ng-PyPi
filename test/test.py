#!/usr/bin/python3
from proxy_ninja_ng import fetch_proxies, fetch_proxies_json, fetch_proxies_list


print("fetch_proxies()")
fetch_proxies("https", "abc", "json")
print("fetch_proxies_json()")
jsn = fetch_proxies_json("https")
print(jsn)
print("fetch_proxies_list()")
lt = fetch_proxies_list("https")
print(lt)