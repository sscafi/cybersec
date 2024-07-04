import socket

def enumerate_subdomains(domain):
    """
    Enumerate common subdomains for a given domain.

    Args:
        domain (str): The target domain to enumerate subdomains for.

    Returns:
        list: A list of tuples containing subdomain names and their corresponding IP addresses.
              Each tuple is in the format (subdomain, ip_address).

    This function attempts to resolve common subdomains (e.g., www, mail, ftp, admin)
    for the given domain. It collects subdomain names and their IP addresses into a list
    of tuples. Additional subdomains can be added based on specific requirements.

    Example:
        target_domain = "example.com"
        result = enumerate_subdomains(target_domain)
        for subdomain, ip_address in result:
            print(f"{subdomain}: {ip_address}")
    """
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
