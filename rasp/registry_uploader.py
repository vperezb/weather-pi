from os import listdir, rename
from os.path import isfile, join
import requests
import datetime
import socket
import configparser

from sense_hat import SenseHat

config = configparser.ConfigParser()

def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False
	

def upload_file(file_path):
    with open(file_path, "rb") as file_to_upload:
        domain = config['GoogleCloud']['APIDomain']
        file_day = file_path.split('/')[-1].split('.')[0]
        file_dict = {"inputfile.csv": file_to_upload}
        request_data = {'register_day': file_day}
        response = requests.post(domain + "/upload", 
	        files=file_dict, data = request_data)

	if response.status_code == 201:
        return True
    else:
        return False

sense = SenseHat()

unclouded_dir = 'data/local-files'
clouded_dir = 'data/uploaded-files'

day = datetime.datetime.now().strftime("%Y-%m-%d")

files_to_upload = [ f for f in listdir(unclouded_dir) if isfile(join(unclouded_dir, f)) ]


if not internet():
    sense.show_message('NO INTERNET', text_colour=(255,0,0))
    raise Exception('NO INTERNET connection avaliable')
	
for file_to_upload in files_to_upload:
    if (file_to_upload != '{}.csv'.format(day)):
	    succeed = upload_file(unclouded_dir + '/' + file_to_upload)
        if succeed:
            rename(unclouded_dir + '/' + file_to_upload, clouded_dir + '/' + file_to_upload)
        else:
            pass # TO DO log the error
    else: pass

