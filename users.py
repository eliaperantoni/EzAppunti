from lib.util import *
import hashlib
import lib.util
import getpass  # TODO Make this work
import sys
import os

loggedUser = "NULL"
permissions = ""


def addUser(username, password, ftp):
    currId = 0
    for i in open("users.txt", "r"):
        try:
            if (i.split(";")[1] == username):
                return 1
        except:
            "End of file"
        try:
            if (int(i.split(";")[0]) > currId):
                currId = int(i.split(";")[0])
        except:
            "End of file"
    currId += 1
    out = ""
    out += str(currId) + ";" + username + ";" + hashlib.sha256(password.encode('utf-8')).hexdigest() + ";*;0"
    open("users.txt", "a").write(out + "\n")
    ftp.storbinary("STOR users.txt", open("users.txt", "rb"))
    return out


currId = 0  # TODO Make this work
if __name__ == "__main__":
    ftp = connectToServer()
    print("Connecting to: " + host + ":" + user + ":" + "******")
    print("Successfully connected (Perhaps) to the host, downloading users.txt")  # TODO Fix connection failed detection
    if "users.txt" in ftp.nlst():
        ftp.retrbinary("RETR users.txt", open("users.txt", "wb").write)  # TODO Hide file
    print("\n===LOGIN===")
    givenUsr = input("Username: ")
    givenPsw = input("Password: ")
    with open("users.txt") as f:
        for line_terminated in f:
            data = line_terminated.split(";")

            if (data[1] == givenUsr and data[3] == "***"):
                if (hashlib.sha256(givenPsw.encode('utf-8')).hexdigest() == data[2]):
                    print("\nLogged successfully to " + givenUsr)
                    loggedUser = givenUsr
                    permissions = data[3]
                    break
                else:
                    print("Wrong password")
                    loggedUser = "WRONG_PASSWORD"
                    exitProgram()
        if (loggedUser == "NULL"):
            print("No users found for entry " + givenUsr + " or not enough permissions")
            exitProgram()
    print("Use 'cmds' to get a list of available commands")
    while (True):
        i = input("$~ ")
        if (i == "add"):
            for i in open("users.txt", "r"):
                if (int(i.split(";")[0]) > currId):
                    currId = int(i.split(";")[0])
            currId += 1
            out = ""
            out += str(currId) + ";"
            out += input("\tUsername: ")
            out += ";"
            out += hashlib.sha256(input("\tPassword: ").encode('utf-8')).hexdigest()
            out += ";"
            out += input("\tPermissions: ")
            out += ";0"
            open("users.txt", "a").write(out + "\n")
            ftp.storbinary("STOR users.txt", open("users.txt", "rb"))
        elif (i == "cup"):
            i = input("\tWhich user? ")
            x = -1
            with open("users.txt") as f:
                for line_terminated in f:
                    x += 1
                    data = line_terminated.split(";")
                    if (data[1] == i):
                        print("\tCurrent permissions: " + data[3])
                        inp = input("\tWhat would be the new permissions? ")
                        db_edit("users.txt", x, 3, inp)
                        ftp.storbinary("STOR users.txt", open("users.txt", "rb"))
                        break
        elif (i == "ls"):
            with open("users.txt") as f:
                for line_terminated in f:
                    data = line_terminated.split(";")
                    print("\t" + data[1] + "/" + data[3] + "/" + data[4].replace("\n", ""))
        elif (i == "cmds"):
            print(
                "List of commands available:\nexit (Quits the program) \nadd (Used to create a new user)\ncup (Used to change user permissions)\nls (Lists all users)")
        elif (i == "exit"):
            break
        else:
            print("Invalid command")
    os.remove("users.txt")
