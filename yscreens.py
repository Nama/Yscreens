import os
import sys
import base64
import paramiko
import pyperclip
import configparser
from PIL import ImageGrab
from balloons import WindowsBalloonTip

config = configparser.ConfigParser()
config.read('yscreens.ini')

try: #Check for script-parameters
    m = sys.argv[1]
    screen_count = int(config.get('yscreens', 'count'))
    upload_file = 'y%s.jpg' %screen_count
    ImageGrab.grab().save(upload_file)
    screen_count += 1
    config.set('yscreens', 'count', str(screen_count))
    with open('yscreens.ini', 'r+') as configfile:
        config.write(configfile)
except: #If no parameters are set
    upload_file = input('Type in the Filepath: ').replace('"', '')
    upload_file_name = str(upload_file.split('\\').pop())
    m = 'file'
#Connect to the ssh server
t = paramiko.Transport((config.get('yscreens', 'host'), int(config.get('yscreens', 'port'))))
key_file = config.get('yscreens', 'key', fallback=None)
if key_file != '':
    key = paramiko.RSAKey.from_private_key_file(key_file)
    t.connect(username=config.get('yscreens', 'username'), pkey=key, hostkey=None)
else:
    password = config.get('yscreens', 'pw')
    t.connect(username=config.get('yscreens', 'username'), password=password, hostkey=None)
sftp = paramiko.SFTPClient.from_transport(t)

if m == 'screen': #If script-parameter 'screen', upload the screenshot, put the link in to clipboard, delete screenshot
    sftp.put(upload_file, config.get('yscreens', 'rmpath') + upload_file)
    pyperclip.copy(config.get('yscreens', 'url') + upload_file)
    os.remove(upload_file)
else: #Upload the given file, put link in to clipboard
    sftp.put(upload_file, config.get('yscreens', 'rmpath') + upload_file_name)
    pyperclip.copy(config.get('yscreens', 'url') + upload_file_name)
    upload_file = upload_file_name
t.close

WindowsBalloonTip('Upload', 'Transfer of ' + upload_file + ' finished')