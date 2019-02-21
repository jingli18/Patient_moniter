import json
import random
import time

def genPatientInfo():

	patientId = '10086'
	name = "Sheng Nan"
	gender = 'female'
	age = '22'
	patientdata = {'patiendId':patientId, 'name':name, 'gender':gender, 'age':age}
	json_string = json.dumps(patientdata)
	return json_stringu

def genSensorData():

	pulse = random.randint(40,130)
	pulseRangeLower = 50
	pulseRangeUpper = 120
	bloodPressure = random.randint(20,110)
	pressureRangeLower = 30
	pressureRangeUpper = 100
	bloodOx = random.randint(50,100)
	oxRangeLower = 60
	oxRangeUpper = 90
	times = time.ctime()
	sensordata = {'pulse': pulse,
	'pulseRange': {'lower': pulseRangeLower, 'upper': pulseRangeUpper},
	'bloodPressure': bloodPressure,
	'pressureRange': {'lower':pressureRangeLower, 'upper':pressureRangeUpper},
	'bloodOx': bloodOx,
	'oxRange': {'lower':oxRangeLower, 'upper':oxRangeUpper},
	'time': times}
	json_string = json.dumps(sensordata)
	return json_string
