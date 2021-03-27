import serial
PORT = '/dev/ttyUSB0'
BAUD = 115200

NEWLINE_FEED = 10

def main():
    data_string = ""
    serialport = serial.Serial(PORT, BAUD, timeout=None)

    while True:
        rx_data = serialport.read()
        try:
            byte_character = rx_data.decode('utf-8')        #convert to a single string character
            decimal_value = ord(rx_data)                    #convert same data to decimal value

            if(decimal_value == NEWLINE_FEED):
                print(data_string)                          #print to terminal
                data_string = ""                            #start a new line of text
            else:
                data_string = data_string + byte_character  #concat string characters till you get to a line feed,
        except:
            print("an exception occurred")

if __name__ == '__main__':
    main()
