from picamera import PiCamera
import pytesseract
import cv2
from PIL import Image
import os
import time
import numpy as np
import subprocess
import servo_example
import RPi.GPIO as GPIO

pytesseract.pytesseract.tesseract_cmd=r'/usr/share/tesseract-ocr/4.00/tessdata'

subject1,subject2,subject3,subject4=[],[],[],[]
subjects=[subject1,subject2,subject3,subject4]

startButton = 16
gpio.output(startButton, gpio.IN)

keywords=open("Subjects.txt","r")
lines=[i.lower() for i in keywords]
pos=0
for i in lines:
    if i=="\n":
        pos+=1
    else:
        i=i.rstrip()
        i=i.replace(",","")
        i=i.replace("?","")
        i=i.replace(".","")
        subjects[pos].append(i.lower())
    


def tester(text):
    test1,test2,test3,test4=0,0,0,0
    for i in text.lower().split():
        if i in subject1:
            test1+=1
        elif i in subject2:
            test2+=1
        elif i in subject3:
            test3==1
        elif i in subject4:
            test4+=1
    subject_results=[test1,test2,test3,test4]
    if sum(subject_results)==0:
        return "Miscellaneous"
    else:
        return subjects[subject_results.index(max(subject_results))][0]

            
camera=PiCamera()

while(gpio.input(startButton)):
    pass

while (not gpio.input(startButton)):
    camera.capture('test.jpg')

    image=cv2.imread('test.jpg')
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imwrite('test_thresh.jpg',thresh)
    subprocess.call("./big_reader.sh")
    output=open("out.txt","r")

    text=list(output)
    text=" ".join(text)
    folder=tester(text)

    most_likely_title=[0,255]
    height,width=thresh.shape[:2]
    start_row=0
    while start_row<height:
        cropped_part=thresh[start_row:start_row+int(height/8), 0:width]
        intensity=np.mean(cropped_part)
        if intensity<most_likely_title[1]:
            most_likely_title=[start_row,intensity]
        start_row+=int(height/8)

    cv2.imwrite("title.jpg",thresh[most_likely_title[0]:most_likely_title[0]+int(height/8),0:width])
    subprocess.call("./small_reader.sh")
    output=open("title.txt","r")
    title=list(output)
    title=" ".join(title)

    try:
        os.mkdir(os.getcwd()+"/"+folder)
    except:
        pass
    im1=Image.open(r"test.jpg")
    try:
        im1.save(os.getcwd()+"/"+folder+"/"+title+".pdf")

    except:
        im1.save(os.getcwd()+"/"+folder+"/"+"scan.pdf")
    print(text)
    print('hi')
    
    servo_example.paperRollers(True);
    time.sleep(5);
    servo_example.paperRollers(False);
    time.sleep(5);

    







