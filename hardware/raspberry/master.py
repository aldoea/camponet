import serial, time

arduino=serial.Serial('/dev/ttyACM0', 9600)
txt=''

while True:
      palabra=arduino.readline()
      if(palabra.decode() != ''):
            print (palabra)
      time.sleep(1)
arduino.close()