## TPRG-2131-ASSIGNMENT-2---SERVER-and-CLIENT-on-RPi
# This repository will contain the code for the TPRG 2131 assignment 2 server and client. additionally it will contain a description of each of the functions used to compose the Server side.




# Function 1:
call to VCgen and get the temperature. this is the example given in the starter file. it is refactored into the function:
def get_core_temperature():
    # Command: vcgencmd measure_temp
    t = os.popen('vcgencmd measure_temp').readline().strip()
    
    return t.replace('temp=', '').replace('\'C', '')
    
    # strip is used to remove huge strings of blank spaces. solution wassuggested by Google gemini


# Function 2:
def get_core_voltage():
    # Command: vcgencmd measure_volts core
    
    v = os.popen('vcgencmd measure_volts core').readline().strip()
    
    return v.replace('volt=', '').replace('V', '')


Function 3:

def get_arm_frequency():
    # Command: vcgencmd measure_clock arm
    f = os.popen('vcgencmd measure_clock arm').readline().strip()
    # Convert from Hz to MHz and return as string
    try:
        frequency_hz = int(f.split('=')[1])
        return str(frequency_hz / 1000000)
    except (IndexError, ValueError):
        return "Error"

        #this function has additional logic to again reduce the number of redundant characters on the screen. 

# Function 4:

def get_firmware_version():
    # Command: vcgencmd version
    v = os.popen('vcgencmd version').read().strip()
    return v.split('\n')[0]


# Function 5:

def get_ext5v_voltage():
    # Command: vcgencmd pmic_read_adc EXT5V_V
    v = os.popen('vcgencmd pmic_read_adc EXT5V_V').readline().strip()
    return v
    # ext5V is an argument that pulls only the 5v bus voltage from the huge list of pmic values that are returned by pmic_read_adc. 


# Function 6:

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

 #this function converts all 5 vcgen values into a dictionary (an ordinated list) which is a convenient datastructure for encoding into a JSON string and transmitting.
 it was recommended by Google gemini to replace individual print statemets in each function








    


    
 
