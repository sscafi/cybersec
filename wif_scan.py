import subprocess

def scan_all_wifi_interfaces():
    try:
        # Run netsh command to list wireless interfaces and scan for networks
        result = subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=Bssid'], capture_output=True, text=True)

        # Print the output
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    scan_all_wifi_interfaces()
