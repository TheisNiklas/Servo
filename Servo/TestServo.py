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

# Create templates of command packets 
__pktAction = [255, 255, 0, 2, 5, 0]                                        # Packet to invoke action
__pktReadData = [255, 255, 0, 4, 2, 0, 0, 0]                                # Packet to request date
__pktWriteByte = [255, 255, 0, 5, 4, 0, 0, 0, 0]                            # Packet to write byte (changed to REG WRITE)
__pktWriteNByte = [255, 255, 0, 0, 3, 0]                                    # Base-packet to write n-bytes
__pktWriteWord = [255, 255, 0, 5, 3, 0, 0, 0, 0]                            # Packet to write word

# Konstanten
SERVO_A = 4     # const value
SERVO_B = 10    # const value

#--------------------------
# Erster Servo (A)
# Erste Drehung
#--------------------------

# servoId = 4                                        # Id of Servo
# command = [255, 255, servoId, 5, 3, 30, 0, 0, 0]    # command list

# Set to position 300
position = 300                                      # define position
__pktWriteByte[2] = SERVO_A
__pktWriteByte[5] = 30                              # GoalPosition
__pktWriteByte[6] = position & 255
__pktWriteByte[7] = position >> 8
sendCommand(__pktWriteByte)                         # send command
'''
command[6] = position & 255                         # set data low byte in command list
command[7] = position >> 8                          # set data high byte in command list
sendCommand(command)                                # send command
'''      

#--------------------------
# Zweiter Servo (B)
# Erste Drehung
#--------------------------  

__pktWriteByte[2] = SERVO_B 
sendCommand(__pktWriteByte)    
sendCommand(__pktAction)                            # Beide Drehungen gleichzeitig ausführen          

# wait for 3 seconds before moving to next position
time.sleep(3)                                      

#--------------------------
# Erster Servo (A)
# Zweite Drehung
#--------------------------

# Set to position 200
position = 200
__pktWriteByte[2] = SERVO_A
__pktWriteByte[5] = 30                              # GoalPosition
__pktWriteByte[6] = position & 255
__pktWriteByte[7] = position >> 8
sendCommand(__pktWriteByte)                         # send command
'''
command[6] = position & 255
command[7] = position >> 8
sendCommand(command)
'''

#--------------------------
# Zweiter Servo (B)
# Zweite Drehung
#-------------------------- 

__pktWriteByte[2] = SERVO_B 
sendCommand(__pktWriteByte)    
sendCommand(__pktAction)                            # Beide Drehungen gleichzeitig ausführen 

# wait for 1 second before finishing
time.sleep(1)
