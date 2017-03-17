from lib.util import *
from lib.updown import *
from lib.master import *
from users import *
import os
import time


def actions_create_note(masterPath, fileName, linesVector, credentials, ftp, tag):
    id = 0
    with open(masterPath) as f:
        for line_terminated in f:
            data = line_terminated.split(";")
            if (int(data[0]) > id):
                id = int(data[0])
    id += 1
    f1 = open("data/" + str(id) + ".txt", "w")
    for i in linesVector:
        f1.write(i + "\n")
    f1.close()
    updown_upload(ftp, "data/" + str(id) + ".txt", str(id) + ".txt")
    master_append(id, ftp, masterPath, fileName, credentials[1], time.time(), tag)


def actions_register(ftp, username, password, confirmPassword, mastertPath="master.txt"):
    if password == confirmPassword:
        code = addUser(username, password, ftp)
        if (code == 1):
            print("A user named {0} already exists".format(username))
            exitProgram()
    else:
        print("The passwords don't match")

def actions_like(id,user_id,masterMap,ftp):
    for i in masterMap:
        master_edit(ftp,"master.txt",id,6,user_id)
        if user_id not in masterMap[id].split(";")[6]:
            user_id+=masterMap[id].split(";")[6]+","
            master_edit(ftp,"master.txt",id,6,user_id)
        else:
            user_id=masterMap[id].split(";")[6].split(",").pop(str(user_id))