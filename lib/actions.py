from lib.util import *
from lib.updown import *
from lib.master import *
import os
import time
def actions_create_note(masterPath,fileName,linesVector,credentials,ftp,tag):
    id=0
    with open(masterPath) as f:
        for line_terminated in f:
            data = line_terminated.split(";")
            if(int(data[0])>id):
                id=int(data[0])
    id+=1
    f1=open("data/"+str(id)+".txt","w")
    for i in linesVector:
        f1.write(i+"\n")
    f1.close()
    updown_upload(ftp,"data/"+str(id)+".txt",str(id)+".txt")
    master_append(id,ftp,masterPath,fileName,credentials[1],time.time(),tag)
def actions_edit_note(id):
    os.startfile("data/"+str(id)+".txt")