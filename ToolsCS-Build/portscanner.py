import socket # to communicate with other devices over TCP/UDP protocol
import termcolor # to print any statement in colors

# Function to call scan_port with one Port
def scan(targets, ports):
	print('\n' + 'Starting Scan for ' + str(targets))
	for  port in range(1, ports):
		scan_port(targets, port)

# Function to scan  Ports of Target
def scan_port(ip, port):
	try:
		# create Objects
		sock = socket.socket() # calling method from socket lib
		sock.connect((ip, port))  # to connect to target IP, port

		print("[+] Port Opened" + str(port))
		sock.close()
	except:
		pass # exclude the Closed  ports
		# print("[-] Port Closed" + str(port))


targets = input("[*] Enter Targets IP addres (split the IPs by comma ,): ")
ports = int(input("[*] Enter Number of Ports to be scanned: "))

# Check for the multiple or single IP
if ',' in targets:
	print(termcolor.colored(("[*] Scanning multiple  Targets:"), 'green')) #Using termcolor to print the statement in green color.
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports) #strip/cut out any blank space
else:
	print("[*] Scanning single Target")
	scan(targets,ports) # for only one target

