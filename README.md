
# Cybersec

Welcome to my journey as i dive into the vast depths of cybsercurity, I developing scripts to mimic already existing cybsercurity tools such as nmap , wireshark and manymore . The purpose is to understand how they work.


## Script Type 
IP_address_phising:

This  provides clarity on how IP access levels are managed and how intrusion attempts are detected and logged based on defined criteria.

Brute_force_enum:

 This is designed to test each candidate_password against a target
system to determine if it is the correct password. In a real-world scenario,
this function would include logic to interact with the target system.

Subdomain_enumerator:

This script attempts to resolve common subdomains (e.g., www, mail, ftp, admin)
for the given domain. It collects subdomain names and their IP addresses into a list
of tuples. Additional subdomains can be added based on specific requirements.

Request_fetch:

this script enhances the performance and offline capabilities of a web application by setting up a service worker to intercept network requests. It caches responses to GET requests in a specified cache storage ('my-cache') and serves cached responses when available, thereby reducing latency and improving the application's responsiveness, especially in low-connectivity scenarios.

Cryptography :

The cryptography library is imported, which is required for using Fernet for encryption and decryption.
Documentation at the beginning explains the purpose, requirements, usage, and notes about the script and the Fernet encryption.
The script demonstrates the complete process: generating a key, creating a Fernet instance, encrypting a message, and decrypting it, followed by printing out the results.

Grab_banners_from_ports:

Script for grabbing banners from specified ports on a target host using sockets.

Usage:
    - Define the function `grab_banner(target, port)` to connect to a specified target on a port,
      retrieve the banner, and print it.
    - Define the function `scan_target(target, ports)` to iterate through a list of ports,
      calling `grab_banner()` for each port.
    - Set the `target_host` variable to specify the target host.
    - Set the `target_ports` list to specify the ports to scan.
"""

Import_socket_for_connectivity:

Script for checking network connectivity by attempting to connect to a well-known IP address and port.

Usage:
    - Define the function `is_network_safe()` to create a TCP socket, attempt to connect to a well-known
      IP address and port (in this case, '8.8.8.8' on port 53), and return True if the connection succeeds.
      Otherwise, return False.


Js_library_download:

"""
Script for downloading JavaScript libraries referenced in the HTML of a given URL.

Usage:
    - Define the function `download_js_libraries(url, save_directory)` to retrieve the HTML content
      from the specified URL, parse it using BeautifulSoup to find all script tags with a 'src' attribute,
      download each JavaScript library referenced by these tags, and save them to the specified directory.
    - Set the `target_url` variable to specify the URL from which to download JavaScript libraries.
    - Set the `save_directory` variable to specify the directory where the downloaded JavaScript files will be saved.

Requirements:
    - requests library: `pip install requests`
    - BeautifulSoup library: `pip install beautifulsoup4`

Wifi_scanner:

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


 Radio Frequency Scanner:   

This script generates and processes a synthetic radio frequency (RF) signal
spanning a wide range of frequencies. It simulates the capture and analysis
of RF signals using Python, without the need for actual hardware like an
RTL-SDR dongle. The script generates a composite signal containing multiple
sinusoidal components and adds Gaussian noise to simulate a real-world scenario.
The signal is then visualized in both time and frequency domains, and peaks
in the frequency spectrum are detected and annotated.
