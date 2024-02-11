import threading
import socket

def enumerate_subdomains(domain, subdomain):
    full_domain = f"{subdomain}.{domain}"
    try:
        ip_address = socket.gethostbyname(full_domain)
        print(f"{full_domain}: {ip_address}")
    except socket.error:
        pass

def threaded_subdomain_enumeration(domain, subdomains):
    threads = []

    for subdomain in subdomains:
        thread = threading.Thread(target=enumerate_subdomains, args=(domain, subdomain))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_domain = "example.com"  # Change this to your target domain
    common_subdomains = ["www", "mail", "ftp", "admin"]

    threaded_subdomain_enumeration(target_domain, common_subdomains)
