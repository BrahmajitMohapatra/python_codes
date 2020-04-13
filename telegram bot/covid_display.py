import requests
import json

import serial
import time

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM10', 9600)


def GetCity(city):
    response=requests.get("https://api.covid19india.org/state_district_wise.json")
    r=response.json()
    print(city.casefold())
    for i,j in r.items():
        #print(i,j)
        for k,l in j.items():
            if i=="Maharashtra" :
                #print(k,l)
                for m,n in l.items():
                    #print(m,n)
                    for o,p in n.items():
                            if o=="confirmed":
                               # print(m.casefold())
                                if(m.casefold()==city.casefold()):
                                 #   print(m,p)
                                    return p
    return -1


def GetState(state):
    response=requests.get("https://api.covid19india.org/data.json")
    data=response.json()
    #print(data)
    Active_All = 0
    Confirmed_all = 0
    statedata = data.get("statewise") 
    for cov_data in statedata:
            #print(cov_data.get("state"),cov_data.get("active"),cov_data.get("confirmed")," deaths " ,cov_data.get("deaths"),cov_data.get("recovered"))
            if(cov_data.get("state") == 'Total'):
                return cov_data.get("active"),cov_data.get("confirmed"),cov_data.get("deaths"),cov_data.get("recovered")
                
           
while True:        
    active,confirm,deaths,recovered =  GetState("MH")
    print("A"+active)
    print("D"+deaths)
    print("R"+recovered)
    print("C"+confirm)
    ser.write(("A"+str(active)+"\n").encode())
    time.sleep(2)
    ser.write(("C"+str(confirm)+"\n").encode())
    time.sleep(2)
    ser.write(("R"+str(recovered)+"\n").encode())
    time.sleep(2)
    ser.write(("D"+str(deaths)+'\n').encode())
    time.sleep(10)


