import time
import random

# Define list of known IP addresses and their corresponding access levels
ip_access_levels = {
    "192.168.1.100": 0,
    "192.168.1.101": 1,
    "192.168.1.102": 2,
    "192.168.1.103": 3
}

def check_access_level(ip_address):
    """
    Check the access level for a given IP address.

    Args:
        ip_address (str): The IP address to check.

    Returns:
        int: The access level (0-3) if the IP address is known,
             -1 if the IP address is not found in the database.
    """
    if ip_address in ip_access_levels:
        return ip_access_levels[ip_address]
    else:
        return -1

def log_intrusion_attempt(ip_address):
    """
    Log an intrusion attempt to a file.

    Args:
        ip_address (str): The IP address from which the intrusion attempt was detected.
    """
    timestamp = time.time()
    with open("intrusion.log", "a") as f:
        f.write(f"Intrusion attempt detected at {timestamp} from IP address {ip_address}\n")

# Main loop to monitor incoming network traffic
while True:
    # Simulate incoming network traffic by randomly generating IP addresses
    incoming_ip_address = "192.168.1." + str(random.randint(1, 254))
    
    # Check access level for incoming IP address
    access_level = check_access_level(incoming_ip_address)
    
    # If access level is below 0, log an intrusion attempt
    if access_level < 0:
        log_intrusion_attempt(incoming_ip_address)
