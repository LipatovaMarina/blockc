import os, sys
def decrypt(file):
	import pyAesCrypt
	password="qwerty"
	bufferSize = 512*1024
	pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
	print("[decrypted] '"+str(os.path.splitext(file)[0])+"'")
	os.remove(file)
def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			try: decrypt(path)
			except: pass
		else: walk(path)
walk("D:\distr")
os.remove(str(sys.argv[0]))