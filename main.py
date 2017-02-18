from lib.master import *
import hashlib
from lib.actions import *
from lib.util import *
from lib.updown import *
def ls_note(ftp):
    for i in range(len(master_ls(ftp, "master.txt"))):
        id, nome, autore, data, views, like, dislike, tagg = master_ls(ftp, "master.txt")[i].split(";")
        print("\n", "ID:", id, "\n", "Nome:", nome, "\n", "Autore:", autore, "\n", "Data:", data, "\n", "Views:", views,"\n", "Like:", like, "\n", "Dislike", dislike, "\n", "Tag:",tagg)
#id/username/password/permessions/karma
credentials=[]
loggedUser="NULL"#Don't refer to this, use credentials[1]
if __name__ == "__main__":
    print("\nEzAppunti v1.0")
    ftp=connectToServer()
    if "users.txt" in ftp.nlst():
        ftp.retrbinary("RETR users.txt", open("users.txt", "wb").write)  # TODO Hide file
    print("\n===LOGIN===")
    givenUsr = input("Username: ")
    givenPsw = input("Password: ")
    with open("users.txt") as f:
        for line_terminated in f:
            data = line_terminated.split(";")
            if (data[1] == givenUsr):
                if (hashlib.sha256(givenPsw.encode('utf-8')).hexdigest() == data[2]):
                    print("\nLogged successfully to " + givenUsr)
                    loggedUser=givenUsr
                    credentials = line_terminated.split(";")
                    credentials[-1]=credentials[-1].rstrip()
                    break
                else:
                    print("Wrong password")
                    loggedUser = "WRONG_PASSWORD"
                    exitProgram()#TODO Don't exit, prompt again for password
        if (loggedUser == "NULL"):
            print("No users found for entry " + givenUsr)
            exitProgram()
    master_init(ftp)
    while True:
        print("\nAdmin pannel:\n[1] Create new note\n[2] Edit existing note\n[3] Delete note\nUser pannel:\n[4] Lista")
        inp=input("~ ")
        if(inp=="1"):
            if(data[3]=="**"or data[3]=="***"):
                tag=[]
                app=" "
                v=[]
                fileName=input("How do you want to name the file? ")
                print("Write the tag, wehn you're done send an empty line")
                while app!="":
                    app=input()
                    tag.append(app)
                tag.pop(-1)
                print("What do you want to write inside the file? When you're done, send an empty line")
                i=" "
                while(i!=""):
                    i=input("")
                    v.append(i)
                actions_create_note("master.txt",fileName,v,credentials,ftp,tag)
            else:
                print("You don't have the right to write new files\n")
        if (inp == "2"):
            if (data[3] == "**" or data[3] == "***"):
                ls_note(ftp)
                id=input("Input the id of note: ")
                #updown_download(ftp,"data/"+id+".txt",id+".txt")
                actions_edit_note(id)

        if(inp=="4"):
            ls_note(ftp)


