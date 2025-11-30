# TPRG-2131-ASSIGNMENT-2---SERVER-and-CLIENT-on-RPi
This repository will contain the code for the TPRG 2131 assignment 2 server and client. additionally it will contain a description of each of the functions used to compose the Server side.


Function 1:
call to VCgen and get the temperature. this is the example given in the starter file. it is refactored into the function:

def get_core_temperature():
    # Command: vcgencmd measure_temp
    t = os.popen('vcgencmd measure_temp').readline().strip()
    return t.replace('temp=', '').replace('\'C', '')
    # strip is used to remove huge strings of blank spaces. solution wassuggested by Google gemini

    


    
 
