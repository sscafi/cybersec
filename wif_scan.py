"""
Script for scanning all WiFi interfaces and networks using the netsh command.

Usage:
    - Define the function `scan_all_wifi_interfaces()` to execute the netsh command to list wireless interfaces
      and scan for networks.
    - Ensure the script is run in an environment where the `netsh` command is available and accessible.
    - The output of the scan is printed directly to the console.

Requirements:
    - This script requires the netsh command-line utility, which is typically available on Windows systems.

Note:
    - Ensure that the script is executed with appropriate permissions to access and execute the `netsh` command.
    - The output format and content may vary based on the network interfaces and networks available.

"""

import subprocess

def scan_all_wifi_interfaces():
    """
    Executes the netsh command to scan all WiFi interfaces and networks.

    Raises:
        subprocess.CalledProcessError: If the netsh command fails to execute.
    """
    try:
        # Run netsh command to list wireless interfaces and scan for networks
        result = subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=Bssid'], capture_output=True, text=True)

        # Print the output
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    scan_all_wifi_interfaces()
