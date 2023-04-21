from Crypto.Cipher import AES
from Crypto import Random
#OFB
key_value = input("the key: ")
padding = lambda s: s + (32 - len(s) % 32) * "*"
key = padding(key_value).encode('ascii')
def encryption(key,o_file):
	block_size = AES.block_size
	with open(o_file,'r+b') as f:
		plaintext = f.read(block_size)
		iv = Random.new().read(16)
		c = AES.new(key,AES.MODE_OFB,iv)
		while plaintext:
			f.seek(-len(plaintext),1)
			f.write(c.encrypt(plaintext))
			plaintext = f.read(block_size)
		return [key,iv]
		f.close()

e = encryption(key,"/home/tarou/Desktop/file.doc")

def decryption(key,iv,e_file):
	block_size = AES.block_size
	with open(e_file,'r+b') as f:
		plaintext = f.read(block_size)
		d = AES.new(key,AES.MODE_OFB,iv)
		while plaintext:
			f.seek(-len(plaintext),1)
			f.write(d.decrypt(plaintext))
			plaintext = f.read(block_size)
		f.close()
de = input("the file is encrypted do you want to reverse ?")
if de == "y":
	decryption(e[0],e[1],"/home/tarou/Desktop/file.doc")
	print("done")