import configparser

config = configparser.ConfigParser()
config.read('/home/displayboard/ftp/files/Host_0/cfg.ini')
if 'bitbucket.org' in config:
    print("bitbucket found")
else: print("bitbucket not found")

slideshow = config['slideshow']
slideshow['Set_switch']
print(slideshow['Slide_time'])
