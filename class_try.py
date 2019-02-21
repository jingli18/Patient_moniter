import threading
from queue import Queue
import time
import random
import input_module
import alertt
import storage
import json

class patient_monitor():
    # generate data in random time
    def generate_data(self, q, q_alert, q_data):
        print("======****** Welcome to Use Patient Monitor ******======")
        print("========================================================")
        print("***************** Copyright Jing Li ********************")
        print("========================================================")
        print("=============", time.ctime(time.time()), "===========")
        while 1:
            times = random.randint(4,7)
            patientData = input_module.genSensorData()
            patientInfo = input_module.genPatientInfo()
            alert_mes = alertt.alertCheck(patientData)
            #print(patientInfo)
            storage.insert(patientInfo, patientData)
            
            q.put(patientInfo)
            print('... ...Waiting for data to be sent to Info... ...\n')
            
            q_data.put(patientData)
            print("... ...Waiting for data to be sent to display... ...\n")

            q_alert.put(alert_mes)
            print("... ...Waiting for alert check... ...\n")

            time.sleep(times)
        

    # every 5 seconds print the patient information
    def print_info(self, q):
        n = 0
        while 1:
            dataIn = q.get()
            print("Info has got the patient information!\n")
            q.task_done()
            if n%5==0:
                print(dataIn)
                n = 0
            n += 1

    def checkAlert(self, q_alert):

        while 1:
            alertmes = q_alert.get()
            if alertmes != "":
                print(alertmes)
            else:
                print("No Alert \n")
            q_alert.task_done()

    def output(self, q_data):
        while 1:
            data = q_data.get()
            print(data)
            q_data.task_done()
            
    # thread that print the time every 1 second
    def print_time(self):
        while True:
            time.sleep(1)
            print (time.ctime(time.time()) )

    def run(self):

        q = Queue()
        q_data = Queue()
        q_alert = Queue()
        t2 = threading.Thread(target=self.generate_data, args=(q, q_alert, q_data))
        t1 = threading.Thread(target=self.print_info, args=(q,))
        t3 = threading.Thread(target=self.output, args=(q_data,))
        t4 = threading.Thread(target=self.checkAlert, args=(q_alert,))
        t5 = threading.Thread(target= self.print_time)

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        q.join()
        q_alert.join()
        q_data.join()

test = patient_monitor()
test.run()