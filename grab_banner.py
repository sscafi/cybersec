"""
Script for grabbing banners from specified ports on a target host using sockets.

Usage:
    - Define the function `grab_banner(target, port)` to connect to a specified target on a port,
      retrieve the banner, and print it.
    - Define the function `scan_target(target, ports)` to iterate through a list of ports,
      calling `grab_banner()` for each port.
    - Set the `target_host` variable to specify the target host.
    - Set the `target_ports` list to specify the ports to scan.
"""

import socket

def grab_banner(target, port):
    """
    Connects to the target on the specified port, retrieves the banner,
    and prints it.

    Args:
        target (str): The target host address or IP.
        port (int): The port number to connect to.
    """
    try:
        # Create a socket object
        s = socket.socket()

        # Set a timeout for the connection attempt
        s.settimeout(2)

        # Connect to the target on the specified port
        s.connect((target, port))

        # Receive up to 1024 bytes of data from the socket
        banner = s.recv(1024)

        # Print the banner
        print(f"Banner from {target}:{port} - {banner.decode('utf-8')}")

    except socket.error as e:
        print(f"Error connecting to {target}:{port} - {e}")

    finally:
        # Close the socket connection
        s.close()

def scan_target(target, ports):
    """
    Iterates through a list of ports and calls `grab_banner()` for each port.

    Args:
        target (str): The target host address or IP.
        ports (list): List of port numbers to scan.
    """
    for port in ports:
        grab_banner(target, port)

if __name__ == "__main__":
    target_host = "example.com"  # Replace with your target host
    target_ports = [80, 443, 22, 21]  # Add the ports you want to scan

    scan_target(target_host, target_ports)
