import time
import serial
import serialPorts

# create serial port connection
l = serialPorts.serialPortList()
print(l)
port = serial.Serial(port=str(l[2]), baudrate=1000000)


# auxiliary methods
def calcCheckSum(pkt):
    s = sum(pkt[2:-1])                              # add all values from servo-id to last parameter
    return (~s) & 0xFF                              # invert sum bit-wise and limit to byte range

def sendCommand(command):
    command[-1] = calcCheckSum(command)             # calculate check sum and store it into last command entry
    port.write(bytearray(command))                  # send command to serial line 
    print("send:", command)


# main programm
servoId = 14                                      # Id of Servo

command = [255, 255, servoId, 5, 3, 30, 0, 0, 0]    # command list

# Set to position 300
position = 300                                      # define position
command[6] = position & 255                         # set data low byte in command list
command[7] = position >> 8                          # set data high byte in command list
sendCommand(command)                                # send command

# wait for 3 seconds before moving to next position
time.sleep(3)                                      

# Set to position 200
position = 200
command[6] = position & 255
command[7] = position >> 8
sendCommand(command)

# wait for 1 second before finishing
time.sleep(1)

