import time

# Define list of known IP addresses and their corresponding access levels
ip_access_levels = {
    "192.168.1.100": 0,
    "192.168.1.101": 1,
    "192.168.1.102": 2,
    "192.168.1.103": 3
}

# Define function to check access level for a given IP address
def check_access_level(ip_address):
    if ip_address in ip_access_levels:
        return ip_access_levels[ip_address]
    else:
        return -1

# Define function to log potential intrusion attempts
def log_intrusion_attempt(ip_address):
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



This code defines a list of known IP addresses and their corresponding access levels, and a function to check the access level for a given IP address. It also defines a function to log potential intrusion attempts.

In the main loop, the code simulates incoming network traffic by randomly generating IP addresses. It then checks the access level for each incoming IP address and logs an intrusion attempt if the access level is below 0 (indicating that the IP address is not a known and authorized user).

This code provides a basic framework for detecting potential hacker activity, but it is by no means a comprehensive or foolproof method for detecting all types of hacking attempts. To create a more effective intrusion detection system, you would need to incorporate additional security measures and techniques, such as machine learning algorithms and behavior-based analysis of network traffic.