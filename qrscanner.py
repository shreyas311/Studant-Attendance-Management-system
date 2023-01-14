from ast import Continue
from msilib.schema import Error
import cv2
import json
import os
import csv
import pandas as pd
from datetime import datetime
from pyzbar.pyzbar import decode 


file = (r'details.json')
path = r'C:\Users\shrey\Desktop\mini project\test'  
full_path = os.path.join(path,file)
header = ['name', 'Branch','Room number','Hostel','Time','Attendance']
now = datetime.now()
currDate = now.date()
currTime = now.time()
name = os.path.join(path,'Attendance - '+str(currDate)+'.csv') 

def getID(full_path): #load JSON file
    
    if os.path.isfile(full_path):
        with open(full_path, "r") as read_file:
            
            uqId = json.load(read_file)
            
    return uqId

def scanQR(): # Function for scanning qr code
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    scan = True

    while scan:

        _, frame = cap.read()
        decodedObjects = decode(frame)
        
        if len(decodedObjects) > 1:
            data = "Only 'one' QR at a time"
            cv2.putText(frame, data, (50, 50), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 0), 3)       
        
        else:

            for obj in decodedObjects:
                (x,y,w,h) = obj.rect
                
                if w > 280 and h > 280:
                    scan = False
                    data = bytes.decode(obj.data)             

                else:
                    pass
        
        cv2.imshow("Frame", frame)
        
        key = cv2.waitKey(1)
        if key == 27:
            break

    return data

def chkID(data,uqId):  #function for check id with json data 
    keys = list(uqId.keys())
    for key in keys:
        if data == key:
            detail =  uqId[data]
        else:
            pass
    return detail

def sheetGen(header,uqId,name):
    
    detailData = list(uqId.values())
    if os.path.exists(name):
        pass
    else:
        with open(name, 'w', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for num in range(len(detailData)):
                writer.writerow({
                    'name':detailData[num]['name'], 
                    'Branch':detailData[num]['Branch'],
                    'Room number':detailData[num]['Room number'],
                    'Hostel':detailData[num]['Hostel'],
                    'Time': currTime, 
                    'Attendance': 'Absent' 
                    })
    return True

def markPresent(name,detaildata,header):
   
    dataFrame = pd.read_csv(name,index_col=False)
    namesList = list(dataFrame.name)
    dataName = detaildata['name']
    
    if dataName in namesList:
        pos = namesList.index(dataName)
        dataFrame.loc[pos, 'Attendance'] = 'Present'
        
        npArray = dataFrame.to_numpy()
        data = []
        for lists in npArray:
            list(lists).pop(0)
            data.append(lists)
            
        with open(name, 'w', encoding='UTF8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for num in range(len(data)):
                writer.writerow({
                    'name':data[num][0], 
                    'Branch':data[num][1],
                    'Room number':data[num][2],
                    'Hostel':data[num][3],
                    'Time': data[num][4], 
                    'Attendance': data[num][5]
                    })
        
st=getID(full_path)
sheetGen(header,st,name)
nid=scanQR()
datadetail=chkID(nid,st)
print(datadetail)
markPresent(name,datadetail,header)