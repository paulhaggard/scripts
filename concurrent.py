import os, signal
from multiprocessing import Process
import time
from watch4change import subprocess_cmd

process_pic = Process()
file_count = 0


def watch_count():
    while True: 
        time.sleep(5)
        print("file watch running")
        #global file_count
        file_count_new = int(subprocess_cmd("cd /home/displayboard/ftp/files/Host_0; ls | wc -l"))
        if file_count != file_count_new:
            print("file count changed")
            return 1
        else: 
            print("file count same")

def get_count():
    global file_count
    file_count = int(subprocess_cmd("cd /home/displayboard/ftp/files/Host_0; ls | wc -l"))
    print("file count is:")
    print(file_count)

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
    time.sleep(2)
    process_pic.terminate()

def check_kill_proc(pstring):
	for line in os.popen("ps a | grep " + pstring + " | grep -v grep"):
		fields = line.split()
		pid = fields[0]
		pid_string = "sudo kill " + pid
		subprocess_cmd(pid_string)

if __name__ == '__main__':
	
    #time.sleep(3)
    #run_picture_viewer()
    #print("sleep 10 first")
    #time.sleep(10)
    #print("sleep 10 first ended")
    #kill_picture_viewer()
    #time.sleep(10)
    #run_picture_viewer()
    #time.sleep(10)
    #kill_picture_viewer()
    #time.sleep(5)

    get_count()
    while True:
        run_picture_viewer()
        return_val = watch_count()
        print("this runs after watchcount codeline")
        if return_val == 1:
            print("\n"*100)
            get_count()
            kill_picture_viewer()
        else: 
            print("ended loop")
            print(return_val)
            break


    time.sleep(10)