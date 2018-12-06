import os, signal
import subprocess
import time
import configparser
from multiprocessing import Process

config = configparser.ConfigParser()
config.read('/home/displayboard/ftp/files/Host_0/cfg.ini')
'bitbucket.org' in config
topsecret = config['topsecret.server.com']
topsecret['Port']
process_pic = Process()
file_count = 0

def subprocess_cmd(command):
    if command == 1:
        time.sleep(10)
        print("did nothing for 10")
        response = 1
    elif command == 2:
        time.sleep(20)
        print("waited 20")
        response = 2
    else:
        process = subprocess.Popen((command), stdout=subprocess.PIPE, shell=True)
        proc_stdout = process.communicate()[0].strip()
        response = proc_stdout
    return response

def watch_count():
    while True: 
        time.sleep(20)
        file_count_new = int(subprocess_cmd("cd /home/displayboard/ftp/files/Host_0; ls | wc -l"))
        if file_count != file_count_new:
            print("file count changed")
            return 1
        else: 
            print("file count same")

def get_count():
    global file_count
    print("\n"*100)
    file_count = int(subprocess_cmd("cd /home/displayboard/ftp/files/Host_0; ls | wc -l"))

def picture_viewer():
    subprocess_cmd("sudo fbi -a -noverbose -t 8 /home/displayboard/ftp/files/Host_0/*.jpg")
    
def run_picture_viewer():
    global process_pic
    print("\n"*100)
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

    get_count()
    while True:
        run_picture_viewer()
        return_val = watch_count()
        print("this runs after watchcount codeline")
        if return_val == 1:       
            get_count()
            kill_picture_viewer()
        else: 
            print("ended loop with watch_count return:")
            print(return_val)
            break

    time.sleep(10)