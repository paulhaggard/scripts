#!/bin/python3
from watch4change import subprocess_cmd
import sys, configparser

config = configparser.ConfigParser()
dataset = config.read('/home/displayboard/ftp/files/Host_0/cfg.ini')

if len(dataset) <= 0:
    print("missing file")
    return_val = 1
else:
    if 'slideshow' in config:
        print("slideshow cfg found")
        slideshow = config['slideshow']
        slideshow['Set_switch']
        print(slideshow['Slide_time'])
        return_val = 0
    else: 
        print("[slideshow] not found")
        return_val = 1