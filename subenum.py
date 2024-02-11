import requests
import sys



sub_list = open("wordlist2.txt").read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)

    except requests.RequestException:
        pass

    else:
        print("Valid domain:", sub_domains)
