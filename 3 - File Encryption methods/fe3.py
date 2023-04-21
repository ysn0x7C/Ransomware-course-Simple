from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter

def encryption(key,file_name):
	counter = Counter.new(128)
	c = AES.new(key,AES.MODE_CTR,counter=counter)
	with open(file_name,'r+b') as f:
		block_size = 16
		plaintext = f.read(block_size)
		while plaintext:
			f.seek(-len(plaintext),1)
			f.write(c.encrypt(plaintext))
			plaintext = f.read(block_size)
		return [key]

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

key = Random.new().read(16)
e = encryption(key,"/home/tarou/Desktop/file.doc")
print(e)
o = input("do you want to reverse? ")
if o == "y":
	decryption(e[0],"/home/tarou/Desktop/file.doc")