#!/bin/python3
from watch4change import subprocess_cmd

def yn_eval(usr_input):
    ans = usr_input.upper()
    if ans == "Y": return 3
    else: return 5

def respond(usr_input):
    if usr_input == 3: 
        print("Ok, continuing...")
        return 0
    else: 
        print("Quitting.")
        return 1
        
def handle_1():
    print("Would you like to disable client mode and enable AP mode? Y/n")
    test = yn_eval(input())
    if respond(test) == 0:
        print("Turning off client")
        subprocess_cmd("sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.ap")
        subprocess_cmd("sudo cp /etc/dhcpcd.conf.ap /etc/dhcpcd.conf")
        subprocess_cmd("sudo service hostapd restart")
        subprocess_cmd("sudo service dnsmasq restart")
    else: 
        pass
        
def handle_2():
    print("Would you like to disable AP mode and enable client mode? Y/n")
    test = yn_eval(input())
    if respond(test) == 0:
        print("Switching to WiFi Client...")
        subprocess_cmd("sudo cp /etc/dnsmasq.conf.orig /etc/dnsmasq.conf")
        subprocess_cmd("sudo cp /etc/dhcpcd.conf.client /etc/dhcpcd.conf")
        subprocess_cmd("sudo service hostapd stop")
        subprocess_cmd("sudo service dnsmasq stop")
        print("reboot.")
    else : pass

def handle_3():
    print("Would you like to install FrameBufferImage displayer? Y/n")
    test = yn_eval(input())
    if respond(test) == 0: 
        print("https://www.raspberrypi-spy.co.uk/2017/02/how-to-display-images-on-raspbian-command-line-with-fbi/") 
        print("getting fbi from apt")
        subprocess_cmd("sudo apt-get update && sudo apt-get -y install fbi")
    else: pass

def handle_4():
    print("Would you like to turn on AutoLogin and Silent Boot? FrameBufferImage displayer? Y/n")
    test = yn_eval(input())
    if respond(test) == 0: 
        print("https://raspberrypi.stackexchange.com/questions/59310/remove-boot-messages-all-text-in-jessie") 
        print("disabling autologin. silent boot setup.")
        subprocess_cmd("sudo cp /boot/cmdline.txt /boot/cmdline.txt.orig")
        subprocess_cmd("sudo cp /configs/boot.cmdline.txt /boot/cmdline.txt")

        subprocess_cmd("sudo cp /etc/rc.local /etc/rc.local.orig")
        subprocess_cmd("sudo cp /configs/etc.rc.local /etc/rc.local")

        subprocess_cmd("sudo cp /etc/systemd/system/autologin\@.service /etc/systemd/system/autologin\@.service.orig")
        subprocess_cmd("sudo cp /configs/autologin\@.service /etc/systemd/system/autologin\@.service")

        subprocess_cmd("sudo cp /configs/.hushlogin ~/.hushlogin")
    else: pass

def handle_5():
    print("Would you like to turn off AutoLogin and Silent Boot? FrameBufferImage displayer? Y/n")
    test = yn_eval(input())
    if respond(test) == 0: 
        print("https://raspberrypi.stackexchange.com/questions/59310/remove-boot-messages-all-text-in-jessie") 
        print("Reverting autologin and boot setup.")
        subprocess_cmd("sudo cp /boot/cmdline.txt.orig /boot/cmdline.txt")

        subprocess_cmd("sudo cp  /etc/rc.local.orig /etc/rc.local")

        subprocess_cmd("sudo cp /etc/systemd/system/autologin\@.service.orig /etc/systemd/system/autologin\@.service")

        subprocess_cmd("sudo rm -r ~/.hushlogin")
    else: pass

print("\n" * 100)
print("What would you like to set up?\n\n")
print("1. Enable AP Mode\n")
print("2. Enable WiFi Client Mode")
print("3. Install FrameBufferImage software")
print("4. Enable Silent Boot & AutoLogin")
print("5. Disable Silent Boot & AutoLogin")
print("6. vsftpd install")
print("\n\nEnter Choice: ")
startup = 1

while startup == 1:
    answer = input()
    if answer == "1" :
        handle_1()
        startup = 0
        break
    elif answer == "2" : handle_2()
    elif answer == "3" : handle_3()
    elif answer == "4" : handle_4()
    elif answer == "5" : handle_5()
    else: print("Invalid selection.")