import sys
from ftplib import FTP
def db_edit(file,line,index,new):
    with open(file,"r") as f:
        lines = f.readlines()
    items = lines[line].split(";")
    out=""
    x=-1
    for i in items:
        x+=1
        if(x==index):
            out+=new
            if (items[x] == items[-1]):
                out += "\n"
        else:
            out+=items[x]
        if not(items[x]==items[-1]):
            out+=";"
    lines[line]=out
    with open(file, "w") as f:
        f.writelines(lines)

def exitProgram():
    input("Press enter to exit ")
    sys.exit(0)
host = "f14-preview.royalwebhosting.net"
pasw = "tooezforrtz"
user = "2289107"
def connectToServer():
    ftp = FTP(host)
    ftp.login(user,pasw)
    return ftp