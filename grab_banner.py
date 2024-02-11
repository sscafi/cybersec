import socket

def grab_banner(target, port):
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
    for port in ports:
        grab_banner(target, port)

if __name__ == "__main__":
    target_host = "example.com"  # Replace with your target host
    target_ports = [80, 443, 22, 21]  # Add the ports you want to scan

    scan_target(target_host, target_ports)
