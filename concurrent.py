import os, signal
from multiprocessing import Process
import time
from watch4change import subprocess_cmd

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

def run_picture_viewer():
	print("waiting to launch picture viewer for 0")
	time.sleep(0)
	subprocess_cmd("sudo fbi -a -noverbose -t 5 /home/displayboard/ftp/files/Host_0/*.jpg")

def check_kill_proc(pstring):
	for line in os.popen("ps a | grep " + pstring + " | grep -v grep"):
		fields = line.split()
		pid = fields[0]
		pid_string = "sudo kill " + pid
		subprocess_cmd(pid_string)

if __name__ == '__main__':
	#Process(target=loop_a).start()
	proc_counter = Process(target=loop_b)
	proc_counter.start()
	#Process(target=run_picture_viewer).start()
	proc_pic = Process(target=run_picture_viewer)
	proc_pic2 = Process(target=run_picture_viewer)
	proc_pic.start()
	print("sleep 10 first")
	time.sleep(10)
	print("sleep 10 first ended")
	check_kill_proc("fbi")
	proc_pic.terminate()
	time.sleep(10)
	check_kill_proc("fbi")
	time.sleep(10)
	proc_pic.start()
	time.sleep(5)
	proc_pic2.start()
	time.sleep(3)
	check_kill_proc("fbi")
	check_kill_proc("fbi")
	check_kill_proc("fbi")

