"""
TPRG assignment #2:
Server/Client vcgencmd and json file

Sebastian Azevedo
100996889

SERVER side script, based on starter file... 
"""
#This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.
#details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
#more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
#more of these at https://www.nicm.dev/vcgencmd/


import socket
import os
import json
import time

#vcgencmd Functions

def get_core_temperature():
    # Command: vcgencmd measure_temp
    t = os.popen('vcgencmd measure_temp').readline().strip()
    return t.replace('temp=', '').replace('\'C', '')

def get_core_voltage():
    # Command: vcgencmd measure_volts core
    v = os.popen('vcgencmd measure_volts core').readline().strip()
    return v.replace('volt=', '').replace('V', '')

def get_arm_frequency():
    # Command: vcgencmd measure_clock arm
    f = os.popen('vcgencmd measure_clock arm').readline().strip()
    # Convert from Hz to MHz and return as string
    try:
        frequency_hz = int(f.split('=')[1])
        return str(frequency_hz / 1000000)
    except (IndexError, ValueError):
        return "Error"

def get_firmware_version():
    # Command: vcgencmd version
    v = os.popen('vcgencmd version').read().strip()
    # Return the first line which contains the version string
    return v.split('\n')[0]

def get_ext5v_voltage():
    # Command: vcgencmd pmic_read_adc EXT5V_V
    v = os.popen('vcgencmd pmic_read_adc EXT5V_V').readline().strip()
    return v

# Server Setup 

s = socket.socket()
host = '' #Listens to all, dont change this line
port = 5000
s.bind((host, port)) #configure I.P. adress and stuff
s.listen(5)

#combine the calls to vcgen into a function

def collect_pi_data():    
    #list
    data_dict = {
        "Temperature_C": get_core_temperature(),
        "Core_Voltage_V": get_core_voltage(),
        "ARM_Frequency_MHz": get_arm_frequency(),
        "Firmware_Version": get_firmware_version(),
        "PMIC_EXT5V_Voltage": get_ext5v_voltage()
    }
    
    return data_dict

#Main Loop
while True:
    # Accept a connection from a client
    c, addr = s.accept()
    print (f'\nGot connection from {addr}')
    f_dict = collect_pi_data()
    print("Data Collected:\n", json.dumps(f_dict, indent=2))
    
    # Convert to a JSON string,  then encode it for sending.
    json_string = json.dumps(f_dict)
    res = json_string.encode('utf-8')
    
    # Send the data
    c.send(res) 
    
    # Close the connection
    c.close()