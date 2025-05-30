import re

# Define the regex pattern for IPv4 addresses
# ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
ip_pattern = re.compile(r'\b(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})(?:\.(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})){3}\b')
# Enter the filepath with its name.
filename = input("Enter the filename [default file: ipaddress.txt if not provided]: ") or "ipaddress.txt"

try:
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            matches = ip_pattern.findall(line)
            if matches:
                for ip in matches:
                    print(f"Line {line_number}: {ip}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
