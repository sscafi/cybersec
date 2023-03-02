import socket

def is_network_safe():
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
