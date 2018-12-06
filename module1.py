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
        print("[slideshow] not found")
    else: print("slideshow cfg found")

    slideshow = config['slideshow']
    slideshow['Set_switch']
    print(slideshow['Slide_time'])
    subprocess_cmd("mkdir /home/pi/scripts/configs")
    subprocess_cmd("sudo cp /etc/dhcpcd.conf.ap /home/pi/scripts/configs/dhcpcd.conf.ap")
    subprocess_cmd("sudo cp /etc/dhcpcd.conf.client /home/pi/scripts/configs/dhcpcd.conf.client")
    subprocess_cmd("sudo cp /etc/dnsmasq.conf.orig /home/pi/scripts/configs/dnsmasq.conf.orig")
    subprocess_cmd("sudo cp /etc/dnsmasq.conf.ap /home/pi/scripts/configs/dnsmasq.conf.ap")
    return_val = 0
