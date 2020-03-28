import socket,os,time
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("3.93.151.85", 5057))
print("Connected to server")
fileimg='image.jpg'
c.send(fileimg)
print("File name sent")
fp=open(fileimg,'r')
strimg = fp.read()
size = os.path.getsize(fileimg)
size = str(size)
time.sleep(0.5)
c.send(size)
print("Size sent")
time.sleep(0.5)
c.send(strimg)
print("String sent")
end='\0'
c.send(end)
print("IMAGE Transfer completed")

#aud recie
print("Waiting for filename mp3")
filemp3=c.recv(1024)
print("file name reviced mp3")
print(filemp3)
sizemp3=c.recv(1024)
print(sizemp3)
print("File size recived mp3")
sizemp3=int(sizemp3)*2
print("Waiting for file transfer")
f=open(filemp3,'wb')
print("File opened")
while True:
	strmp3=c.recv(1024)
	if not strmp3:
		f.close()
		print("File Closed")
		break
	f.write(strmp3)
print("String  recived mp3")
f.close()
print("Completed")
