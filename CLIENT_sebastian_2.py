"""
TPRG assignment #2:
Server/Client vcgencmd and json file

Sebastian Azevedo
100996889

Client side script, currently configured to us the localhost for easy testing purposes...




Moderate and responsible use of Google gemini to evade some problems, as detailed in the Github repository Readme
"""

import socket
import json


HOST = '127.0.0.1' #localhost use it to test the server and client scripts on one Pi
#HOST = 'PI IP'    #real Pi I.P. adress is used if a different device on the network is used.

PORT = 5000

print(f"Attempting to connect to {HOST} on port {PORT}...\n")

#try except loop to manage connectivity and troubleshooting, and to quit "gracefully" as per the assignment instructions:
try:
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connection successful! Waiting for data...\n")
    
    #Receive the data
    data_bytes = client_socket.recv(4096)
    client_socket.close()
    
    #Decode the data
    json_string = data_bytes.decode('utf-8')
    print("\n Data Received \n ")
    print(json_string)
    pi_data = json.loads(json_string)
    
    #Print the vcgen data
    print("\n Raspberry Pi Data \n")
    for key, value in pi_data.items():
        print(f"{key}:   {value}")

except ConnectionRefusedError:
    print("\n ERROR: Connection Refused.\n")
    print(f"You must start the server script on the Pi at {HOST}:{PORT}.\n")
except TimeoutError:
    print("\n ERROR: Connection Timeout.\n")
    print(f"Ensure the IP address ({HOST}) is correct and the Pi is on the network.\n")
except Exception as e:
    print(f"\n An unexpected error occurred: {e}\n")