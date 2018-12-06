#!/usr/bin/env python
import sys
import subprocess
import time
import threading
from queue import Queue
import shutil
from multiprocessing import Process

#lock to serialize console output
#lock = threading.Lock()

def wait(time_sec):
	time.sleep(time_sec) #is in seconds

def subprocess_cmd(command):

	wait(1)
	print("new task started")
	if command == 1:
		time.sleep(10)
		print("did nothing for 10")
		response = 1
	elif command == 2:
		wait(20)
		print("waited 20")
		response = 2
	else:
		process = subprocess.Popen((command), stdout=subprocess.PIPE, shell=True)
		proc_stdout = process.communicate()[0].strip()
		response = proc_stdout
	return response

#def worker():
#	while True:
#		item =q.get()
#		(target=subprocess_cmd(item)).start()
#		q.task_done()
#
#q = Queue() #create a placeholder for tasks

#q.put(1)
#q.put(2)
#response = subprocess_cmd(
#q.put("cd /home/displayboard/ftp/files/Host_0; ls | wc -l")
#print("counted files")
#subprocess_cmd("echo test")
#subprocess_cmd("cd ..")
#print(int(response))
#subprocess_cmd(
#q.put("fbi -noverbose -a -t 5 /home/displayboard/ftp/files/Host_0/*.jpg")
#print("on exit, print this")
#q.join()
#print("\n\n")
#print(response)
#print("\n\n")
