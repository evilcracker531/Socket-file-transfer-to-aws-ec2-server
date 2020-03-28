import socket,os,time,threading

class Cthread(threading.Thread):
    def __init__(self,address,csock):
        threading.Thread.__init__(self)
        self.c=csock
        self.addr=address
        print("New Connection added: ",self.addr)
    def run(self):
       print("Connection from Client: ",self.addr)
       #c->s img
       fileimg=self.c.recv(1024)
       print("File name recive img")
       sizeimg=self.c.recv(1024)
       print("File size recived img")
       sizeimg=int(sizeimg)*2
       print(sizeimg)
       f=open(fileimg,'w')
       strimg=self.c.recv(1024)
       while(strimg!='\0'):
           f.write(strimg)
           strimg=self.c.recv(1024)
       print("String reviced img")
       f.close()
       print("Imaged saved")
       #s->c audio
       print("sending mp3")
       filemp3='audio.mp3'
       self.c.send(filemp3)
       print("file name sent mp3")
       size=os.path.getsize(filemp3)
       size=str(size)
       time.sleep(0.5)
       self.c.send(size)
       time.sleep(0.5)
       fp=open(filemp3,'rb')
       while True:
       	  l=fp.read(1024)
          while(l):
                self.c.send(l)
                l=fp.read(1024)
          if not l:
                fp.close()
                self.c.close()
                break
       print("String sent mp3")
       print("Transfer Completed")

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 5057))
while(1):
   s.listen(10)
   csock,address=s.accept()
   newthread=Cthread(address,csock)
   newthread.start()
