import serial, string, time, logging
#The following block of code works like this:
#If serial data is present, read the line, decode the UTF8 data,
#...remove the trailing end of line characters
#...split the data into temperature and humidity
#...remove the starting and ending pointers (< >)
#...print the output
def sleep(secs):
    time.sleep(secs)

# Python program to get average of a list 
def average(lst): 
	return sum(lst) / len(lst) 

def triggerDataPost(tempBuffer, humidityBuffer, illuminationBuffer):
    print("Trigger actioned")
    tempAvg = average(tempBuffer)
    humidityAvg = average(humidityAvg)
    illuminationAvg = average(illuminationBuffer)
    print(f"=> Temperatura: {tempAvg}, Humedad: {humidityAvg}, Iluminacion: {illuminationAvg}")

def main():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    recordCounter = 0
    serialConnectionAttemps = 0
    tempBuffer = []
    humidityBuffer = []
    illuminationBuffer = []
    while True:
        try:
            if ser.in_waiting > 0:
                print('->Starting reading...')
                serialConnectionAttemps = 0
                rawserial = ser.readline()
                cookedserial = rawserial.decode('utf-8').strip('\r\n')
                datasplit = cookedserial.split(',')
                temperature = datasplit[0].strip('<')
                humidity = datasplit[1]
                illumination = datasplit[2].strip('>')
                tempBuffer.append(temperature)
                humidityBuffer.append(humidity)
                illuminationBuffer.append(illumination)
                if recordCounter == 5 and len(tempBuffer) == 5 and len(humidityBuffer) == 5 and len(illuminationBuffer) == 5:
                    triggerDataPost()
                    tempBuffer = []
                    humidityBuffer = []
                    illuminationBuffer = []
                    recordCounter = 0
                else:
                    recordCounter+=1
            # else:
            #     print('=> No serial stream detected, waiting 3 secs...')
            #     sleep(3)
            #     serialConnectionAttemps+=1
            #     if serialConnectionAttemps > 100: break
        except Exception as e:
                # Wait for 5 seconds
                print("=========== ERROR ===========")
                logging.exception(e)
                sleep(5)

if __name__ == "__main__":
    main()