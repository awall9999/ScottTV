#!/usr/bin/python

# -*- coding: utf-8 -*-
import os
import subprocess
import time
import RPi.GPIO as GPIO
#set up GPIO using BCM numbering

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def tata(video):
  

   print ('omxplayer', '/mnt/usb/movies/' + video)
   myprocess = subprocess.Popen(['omxplayer','-o','local', '--aspect-mode', 'fill', '/mnt/usb/movies/' + video],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
   time.sleep(5)
   
   while True:
 
    if(GPIO.input(17) == 0):
        print('button 1')
        myprocess.communicate(b"q")
        return
    if(GPIO.input(27) == 0):
        print('button 1')
        myprocess.communicate(b"q")
        return
    if(GPIO.input(22) == 0):
        print('button 1')
        myprocess.communicate(b"q")
        return
    if(GPIO.input(5) == 0):
        print('button 1')
        myprocess.communicate(b"q")
        return
    if(GPIO.input(6) == 0):
        print('button 1')
        myprocess.communicate(b"q")
        return
    if(GPIO.input(13) == 0):
        print('button 1')
        myprocess.communicate(b"q")
        return

#check if omxplayer is still running
    processname = 'omxplayer'
    tmp = os.popen("ps -Af").read()
    proccount = tmp.count(processname)
    print(proccount)
    if proccount == 1:
        print('stopp')
        return


