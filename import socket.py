"""
Script for checking network connectivity by attempting to connect to a well-known IP address and port.

Usage:
    - Define the function `is_network_safe()` to create a TCP socket, attempt to connect to a well-known
      IP address and port (in this case, '8.8.8.8' on port 53), and return True if the connection succeeds.
      Otherwise, return False.

Note:
    - This function uses socket programming to check network connectivity.
    - It tries to connect to a well-known DNS server IP ('8.8.8.8') on port 53 commonly used for DNS queries.
    - If the connection attempt times out or encounters an error, it returns False indicating potential network issues.
"""

import socket

def is_network_safe():
    """
    Attempts to connect to a well-known IP address and port to check network connectivity.

    Returns:
        bool: True if the connection attempt succeeds, False otherwise.
    """
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        sock.settimeout(5)
        
        # Attempt to connect to a well-known IP address and port
        sock.connect(('8.8.8.8', 53))
        
        # Close the socket
        sock.close()
        
        return True
    except socket.error:
        return False

if __name__ == "__main__":
    network_safe = is_network_safe()
    if network_safe:
        print("Network is safe.")
    else:
        print("Network might have issues.")
