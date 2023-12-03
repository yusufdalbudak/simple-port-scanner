Python Port Scanner

A simple Python script for network port scanning using sockets.
Description

This script allows you to perform a basic network port scan on a specified IP address within a given port range. It utilizes Python's socket module to check for open ports and reports their status.
Features

Scans a range of ports on a specified IP address
Detects open and closed ports
Easy to use and modify

Usage
Clone the repository:

    
     $ git clone https://github.com/yusufdalbudak/simple-port-scanner.git
     $ cd python-port-scanner
  
Update the ip variable in the script with the target IP address.

Run the script:

    $ python port_scanner.py

Example:
$ python port_scanner.py
1 : closed
2 : closed
3 : closed
...
80 : open
81 : closed
...

