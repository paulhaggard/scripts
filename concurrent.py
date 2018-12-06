import os, signal
from multiprocessing import Process
import time
from watch4change import subprocess_cmd

process_pic

def loop_a():
	while 1:
		time.sleep(1)
		print("waited 1")

def loop_b():
	count = 0
	while count != 50:
		time.sleep(1)
		print('waited {}'.format(count))
		count = count + 1

def picture_viewer():
    subprocess_cmd("sudo fbi -a -noverbose -t 5 /home/displayboard/ftp/files/Host_0/*.jpg")
    
def run_picture_viewer():
    global process_pic
    process_pic = Process(target=picture_viewer)
    process_pic.start()

def kill_picture_viewer():
    global process_pic
    check_kill_proc("fbi")
    process_pic.terminate()

def check_kill_proc(pstring):
	for line in os.popen("ps a | grep " + pstring + " | grep -v grep"):
		fields = line.split()
		pid = fields[0]
		pid_string = "sudo kill " + pid
		subprocess_cmd(pid_string)

if __name__ == '__main__':
	
    time.sleep(3)
    run_picture_viewer()
	print("sleep 10 first")
	time.sleep(10)
	print("sleep 10 first ended")
	kill_picture_viewer()
	time.sleep(10)
	run_picture_viewer()
	time.sleep(10)
	kill_picture_viewer()
	time.sleep(5)