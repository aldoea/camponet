import serial, string, time, logging, datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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
    return (sum(lst) / len(lst)) 

def triggerDataPost(tempBuffer, humidityBuffer, illuminationBuffer):
    print("Trigger actioned")
    tempAvg = average(tempBuffer)
    humidityAvg = average(humidityBuffer)
    illuminationAvg = average(illuminationBuffer)
    print(f"=>DATA TO SEND: Temperatura: {tempAvg}, Humedad: {humidityAvg}, Iluminacion: {illuminationAvg}")
    # Use a service account
    cred = credentials.Certificate('./campo-net2020-firebase-adminsdk-2tn9u-1c82cf5402.json')
    firebase_admin.initialize_app(cred)
    
    current_time = datetime.datetime.now(datetime.timezone.utc)
    unix_timestamp = current_time.timestamp()
    data = {
        u'temperature': tempAvg,
        u'humidity': humidityAvg,
        u'illumination': illuminationAvg,
        u'timestamp': unix_timestamp
    }
    
    db = firestore.client()
    doc_ref = db.collection(u'datapoints').document(u'{}'.format(unix_timestamp))
    doc_ref.set(data)

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
                print('->Serial signal recived...')
                rawserial = ser.readline()
                cookedserial = rawserial.decode('utf-8').strip('\r\n')
                print("Serial input:", cookedserial)
                datasplit = cookedserial.split(',')
                if len(datasplit) != 3: continue
                temperature = float(datasplit[0].strip('<'))
                print("TEMP:", temperature)
                humidity = float(datasplit[1])
                print("HUM:", humidity)
                illumination = float(datasplit[2].strip('>'))
                print("ILL:", illumination)
                tempBuffer.append(temperature)
                humidityBuffer.append(humidity)
                illuminationBuffer.append(illumination)
                recordCounter+=1
                print(f"=>RecordCounter: {recordCounter} Temperatura: {len(tempBuffer)}, Humedad: {len(humidityBuffer)}, Iluminacion: {len(illuminationBuffer)}")
                if recordCounter == 5 and len(tempBuffer) == 5 and len(humidityBuffer) == 5 and len(illuminationBuffer) == 5:
                    triggerDataPost(tempBuffer, humidityBuffer, illuminationBuffer)
                    print('Debuggin in production')
                    tempBuffer = []
                    humidityBuffer = []
                    illuminationBuffer = []
                    recordCounter = 0
        except Exception as e:
                # Wait for 5 seconds
                print("=========== ERROR ===========")
                logging.exception(e)
                sleep(5)
    ser.close()

if __name__ == "__main__":
    main()