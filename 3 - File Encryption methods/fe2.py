from Crypto.Cipher import AES
from Crypto import Random
import os
class E_file:
	
	def __init__(self,key):
		self.key = key

	def encryption(self,o_file):
		iv = Random.new().read(16)
		c = AES.new(self.key,AES.MODE_OFB,iv)
		with open(o_file,'rb') as of:
			with open(o_file.split("/")[-1]+".en",'wb') as ef:
				ef.write(c.encrypt(of.read()))
		ef.close()
		of.close()
		os.remove(o_file)
		return iv


	def decryption(self,e_file,iv):
		c = AES.new(self.key,AES.MODE_OFB,iv)
		with open(e_file,'rb') as ef:
			with open(e_file.split("/")[-1].strip(".en"),'wb') as of:
				of.write(c.decrypt(ef.read()))
		ef.close()
		of.close()
		os.remove(e_file)


key_value = input("the key: ")
padding = lambda s: s + (32 - len(s) % 32) * "*"
key = padding(key_value).encode('ascii')
c = E_file(key)
file_path = "/home/tarou/Desktop/file.doc"
e = c.encryption(file_path)
de = input("the file is encrypted do you want to reverse ?")
if de == "y":
	c.decryption(file_path.split("/")[-1]+".en",e)
	print("done")
