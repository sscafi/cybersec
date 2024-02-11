import socket

def enumerate_subdomains(domain):
    subdomains = []

    try:
        # Resolve common subdomains
        common_subdomains = ["www", "mail", "ftp", "admin"]

        for subdomain in common_subdomains:
            full_domain = f"{subdomain}.{domain}"
            ip_address = socket.gethostbyname(full_domain)
            subdomains.append((full_domain, ip_address))

        # Additional subdomains can be added based on your requirements

    except socket.error:
        pass

    return subdomains

if __name__ == "__main__":
    target_domain = "example.com"  # Change this to your target domain
    result = enumerate_subdomains(target_domain)

    if result:
        print("Enumerated Subdomains:")
        for subdomain, ip_address in result:
            print(f"{subdomain}: {ip_address}")
    else:
        print("No subdomains found.")
