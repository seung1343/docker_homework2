import os
import time
import subprocess

mtime='0000000000000'
f=open('data/my_out.txt','a+')
f.write("recording_started\n")
f.close()
while(True):
	time.sleep(1)
	saved_file = './data/.last'
	if(os.path.exists(saved_file)!=True):
		continue
	g=open(saved_file,'r')
	x=g.readline()
	g.close()
	if x[0:13]!=mtime:
		f=open('data/my_out.txt','a')
		f.write(x)
		f.write('\n')
		f.close()
	mtime=x[0:13]	
