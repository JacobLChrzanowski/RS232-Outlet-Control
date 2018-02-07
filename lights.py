###################################
##                              ##
##   Jacob L Chrzanowski's     ##
##      JSON Thing v1.0.1     ##
##                          ##
#############################

import random
import time             # for time stuff
import threading        # for parallel computing
import serial          # for communication with serial port
import signal
import sys

ser = serial.Serial()
ser.port = 'COM10'
ser.baudrate = 115200
ser.open()

ports = [1,2,3,11,15,16]
state = [True, True, True, True]

def open():
    time.sleep(1)
    ser.write(b'\r')
    ser.flush()

    time.sleep(1)
    print(ser.read(ser.inWaiting()).decode())
    ser.write('admn\r'.encode())
    ser.flush()

    time.sleep(1)
    print(ser.read(ser.inWaiting()).decode())
    ser.write('admn\r'.encode())
    ser.flush()


def run_program():
    
    open()   

    while(1):
        time.sleep(1)
        index = random.randrange(0,4)
        print('index is ' + str(index))
        decided = ports[index]
        print(decided)

        if state[index]:
            ser.write(('Off .a' + str(ports[index]) + '\r').encode())
        else:
            ser.write(('On .a' + str(ports[index]) + '\r').encode())


        state[index] = not state[index]
        ser.flush()

def Exit_gracefully(signal, frame):
    lightsOn()

def ensClear():
    time.sleep(.25)
    ser.write('\r\r'.encode())
    ser.flush()
    time.sleep(.25)
    ser.write('\r\r'.encode())
    ser.flush()
    time.sleep(.25)

def lightsOn():
    open() 

    ensClear()

    for x in range(5):
        time.sleep(1)
        ser.write(('On .a' + str(ports[x]) + '\r').encode())
        ser.flush()

    ser.close()
    sys.exit(0)

def lightsOff():
    open() 

    ensClear()

    for x in range(5):
        time.sleep(1)
        ser.write(('Off .a' + str(ports[x]) + '\r').encode())
        ser.flush()

    ser.close()
    sys.exit(0)

def lightsTopOn(port):
    open() 

    ensClear()

    ser.write(('On .a' + str(port) + '\r').encode())
    ser.flush()

    ser.close()
    sys.exit(0)

def lightsTopOff(port):
    open() 

    ensClear()

    ser.write(('Off .a' + str(port) + '\r').encode())
    ser.flush()

    ser.close()
    sys.exit(0)



if __name__ == '__main__':
    signal.signal(signal.SIGINT, Exit_gracefully)
    if (len(sys.argv) == 1):
        run_program()
    elif (len(sys.argv) == 2):
        if (sys.argv[1] == '-o'):
            lightsOn()
        elif (sys.argv[1] == '-c'):
            lightsOff()
        elif (sys.argv[1] == '-to'):
            lightsTopOn(16)
        elif (sys.argv[1] == '-tc'):
            lightsTopOff(16)
    else:
        print("Unsupported cmd line function")
    ser.close()
    sys.exit()





# time.sleep(1)
# print(ser.read(ser.inWaiting()).decode())
# ser.write('Off .a1\rOff .a3\r'.encode())
# ser.flush()

# time.sleep(4)
# print(ser.read(ser.inWaiting()).decode())

# time.sleep(1)
# print(ser.read(ser.inWaiting()).decode())
# ser.write('On .a1\rOn .a3\r'.encode())
# ser.flush()