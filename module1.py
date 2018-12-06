import sys, configparser

config = configparser.ConfigParser()
try:
    config.read('/home/displayboard/ftp/files/Host_0/cfg1.ini')
except:
    print("Unexpected error:", sys.exc_info()[0])

try:
    config.read('/home/displayboard/ftp/files/Host_0/cfg.ini')
except:
    print("Unexpected error:", sys.exc_info()[0])

if 'bitbucket.org' in config:
    print("bitbucket found")
else: print("bitbucket not found")

slideshow = config['slideshow']
slideshow['Set_switch']
print(slideshow['Slide_time'])
