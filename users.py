from ftplib import FTP
import hashlib
import getpass #TODO Make this work
import sys
import os
host = "f14-preview.royalwebhosting.net"
pasw = "tooezforrtz"
user = "2289107"
loggedUser="NULL"
permissions=""
currId=0 #TODO Make this work
def exitProgram():
    input("Press enter to exit ")
    sys.exit(0)
if __name__ == "__main__":
    ftp = FTP(host)
    print("Connecting to: "+host+":"+user+":"+"******")
    ftp.login(user,pasw)
    print("Successfully connected (Perhaps) to the host, downloading users.txt")#TODO Fix connection failed detection
    if "users.txt" in ftp.nlst():
        ftp.retrbinary("RETR users.txt",open("users.txt","wb").write)#TODO Hide file
    print("\n===LOGIN===")
    givenUsr=input("Username: ")
    givenPsw = input("Password: ")
    with open("users.txt") as f:
        for line_terminated in f:
            data = line_terminated.split(";")
            if(int(data[0])>currId):
                currId=int(data[0])
            if (data[1] == givenUsr and data[3]=="**"):
                if(hashlib.sha256(givenPsw.encode('utf-8')).hexdigest() == data[2]):
                    print("\nLogged successfully to " + givenUsr)
                    loggedUser=givenUsr
                    permissions=data[3]
                    break
                else:
                    print("Wrong password")
                    loggedUser="WRONG_PASSWORD"
                    exitProgram()
        if(loggedUser=="NULL"):
            print("No users found for entry "+givenUsr+" or not enough permissions")
            exitProgram()
    print("Use 'cmds' to get a list of available commands")
    while(True):
        i=input("$~ ")
        if(i=="add"):
            currId+=1
            out=""
            out+=str(currId)+";"
            out+=input("\tUsername: ")
            out += ";"
            out+=hashlib.sha256(input("\tPassword: ").encode('utf-8')).hexdigest()
            out += ";"
            out+=input("\tPermissions: ")
            out+=";0"
            open("users.txt","a").write("\n"+out)
            ftp.storbinary("STOR users.txt",open("users.txt","rb"))
        elif(i=="cup"):#TODO Make this a little bit better and more reliable
            i=input("\tWhich user? ")
            x=-1
            with open("users.txt") as f:
                for line_terminated in f:
                    x+=1
                    data = line_terminated.split(";")
                    if(data[1]==i):
                        print("\tCurrent permissions: "+data[3])
                        inp=input("\tWhat would be the new permissions? ")
                        temp=open("users.txt","r").read()
                        out=""
                        lineData=temp.split("\n")[x].split(";")
                        for i in range(3):
                            out+=lineData[i]+";"
                        out+=inp+";"
                        out+=lineData[4]
                        with open("users.txt", "r") as file:
                            lines = file.readlines()
                        if not(lines[-1]==lines[x]):
                            out+="\n"
                        lines[x]=out
                        with open("users.txt", "w") as file:
                            file.writelines(lines)
                        ftp.storbinary("STOR users.txt", open("users.txt", "rb"))
                        break
        elif(i=="ls"):
            with open("users.txt") as f:
                for line_terminated in f:
                    data = line_terminated.split(";")
                    print("\t"+data[1]+"/"+data[3]+"/"+data[4].replace("\n",""))
        elif(i=="cmds"):
            print("List of commands available:\nexit (Quits the program) \nadd (Used to create a new user)\ncup (Used to change user permissions)\nls (Lists all users)")
        elif(i=="exit"):
            break
        else:
            print("Invalid command")
    os.remove("users.txt")