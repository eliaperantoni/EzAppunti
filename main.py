from lib.master import *
import hashlib
from lib.actions import *
from lib.util import *
from lib.updown import *
def updateMap():
    for i in master_ls(ftp,"master.txt"):
        masterMap[i.split(";")[0]]= i
def ls_note(ftp):
    for i in range(len(master_ls(ftp, "master.txt"))):
        id, nome, autore, data, views, like, dislike, tagg = master_ls(ftp, "master.txt")[i].split(";")
        data=time.ctime(float(data))
        print("\n", "ID:", id, "\n", "Nome:", nome, "\n", "Autore:", autore, "\n", "Data:", data, "\n", "Views:", views,"\n", "Like:", like, "\n", "Dislike", dislike, "\n", "Tag:",tagg)
#id/username/password/permessi/karma
credentials=[]
filter=[]
loggedUser="NULL"#NON UTILIZZARE QUEST VARIABILE, USARE credentials[1] PER RICEVERE L'USERNAME DELL'UTENTE LOGGATO
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
            userData = line_terminated.split(";")
            if (userData[1] == givenUsr):
                if (hashlib.sha256(givenPsw.encode('utf-8')).hexdigest() == userData[2]):
                    print("\nLogged successfully to " + givenUsr)
                    loggedUser=givenUsr
                    credentials = line_terminated.split(";")
                    credentials[-1]=credentials[-1].rstrip()
                    break
                else:
                    print("Wrong password")
                    loggedUser = "WRONG_PASSWORD"
                    exitProgram()#FIXME Non uscire dal programma, chiedi di nuovo la password
        if (loggedUser == "NULL"):
            print("No users found for entry " + givenUsr)
            exitProgram()
    master_init(ftp)
    masterMap={}
    updateMap()
    while True:

        ls_note(ftp)
        print("")
        if filter!=[]:
            activeFiltersStr = ""
            for i in filter:
                activeFiltersStr+=(i+" ")
            print("The filters are: "+activeFiltersStr)
            del activeFiltersStr
        else:
            print("There are no filters")
        if filter==[]:
            print("\n[1]Note add\n[2]Select note\n[3]Add filter")
        else:
            print("\n[1]Note add\n[2]Select note\n[3]Remove filter")
        _inp=input("~ ")
        if(_inp=="1"):
            if(credentials[3]=="**"or credentials[3]=="***"):
                tag=[]
                app=" "
                fileName=input("How do you want to name the file? ")
                print("Write the tag, when you're done send an empty line")
                while app!="":
                    app=input()
                    tag.append(app)
                tag.pop(-1)
                open("temp.txt","w").close()
                os.startfile(os.path.normpath("temp.txt"))
                input("Press enter after you've finished writing, remember to save the file!")
                v=open("temp.txt","r").readlines()
                print("\nLoading....\n")
                actions_create_note("master.txt",fileName,v,credentials,ftp,tag)
            else:
                print("You don't have the right to write new files\n")
        if(_inp=="3"):
            if filter==[]:
                updateMap()
                researchStr=""
                researchStr=input("What's the filters? ")
                for i in researchStr.split(" "):
                    filter.append(i)
            else:
                filter=[]
        if(_inp=="2"):
            print("Which note do you want to select?")
            id_=input("~ ")
            updown_download(ftp,"data/"+id_+".txt",id_+".txt")
            print("\nTitle: "+masterMap[id_].split(";")[1])
            print("Tags: "+masterMap[id_].split(";")[7])
            print("<<"+open("data/"+str(id_)+".txt","r").read()+">>")
            inpE=""
            while inpE!="5":
                print("\n[1]Edit title\n[2]Edit tags\n[3]Edit text\n[4]Delete note\n[5]Exit")
                inpE=input("~ ")
                if inpE=="3" and (credentials[3]=="**"or credentials[3]=="***"):
                    os.startfile(os.path.normpath("data/" + id_ + ".txt"))
                    input("Press enter when you're done editing, remember to save!")
                    updown_upload(ftp,"data/"+id_+".txt",id_+".txt")
                    updateMap()
                if inpE=="1" and (credentials[3]=="**"or credentials[3]=="***"):
                    print(masterMap[id_].split(";")[1])
                    newTitle = input("Which is the new title?")
                    master_edit(ftp,"master.txt",id_,1,newTitle)
                    updateMap()
                if inpE=="2" and (credentials[3]=="**"or credentials[3]=="***"):
                    inpTag=""
                    inpStr="a"
                    print("The old tags were: "+masterMap[id_].split(";")[7])
                    inpStr=input("What's the new tags?")
                    master_edit(ftp,"master.txt",id_,7,inpStr)
                    updateMap()
                    print("The new tags are: "+masterMap[id_].split(";")[7])
                if inpE=="4" and (credentials[3]=="**"or credentials[3]=="***"):
                    print("work in progress")