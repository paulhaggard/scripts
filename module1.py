import sys, configparser

config = configparser.ConfigParser()
try:
    dataset = config.read('/home/displayboard/ftp/files/Host_0/cfg.ini')
except:
    print("Unexpected error:", sys.exc_info()[0])
if len(dataset) <= 0:
    print("missing file")
    return_val = 1
else:
    if 'bitbucket.org' in config:
        print("bitbucket found")
    else: print("bitbucket not found")

    slideshow = config['slideshow']
    slideshow['Set_switch']
    print(slideshow['Slide_time'])
    return_val = 0
