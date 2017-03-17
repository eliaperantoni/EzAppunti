from lib.master import *
import hashlib
from lib.actions import *
from lib.util import *
from lib.updown import *
import os
def updateMap():
    for i in master_ls(ftp, "master.txt"):
        masterMap[i.split(";")[0]] = i
def ls_note(ftp):
    vector = []
    v = master_ls(ftp,"master.txt")
    ###
    dict2 = {"1":0,"2":1,"3":3,"4":2}
    dict = {}
    for i in master_ls(ftp, "master.txt"):
        dict[i.split(";")[dict2[ordination]]] = i
    v = []
    for key in sorted(dict):
        v.append(dict[key])
    ###
    if (isReverse):
        v=v[::-1]
    if filter==[]:
        for i in v:
            id, nome, autore, data, views, like, dislike, tagg = i.split(";")
            data = time.ctime(float(data))
            print("\n","ID:",id,"\n","Nome:",nome,"\n","Autore:",autore,"\n","Data:",data,"\n","Views: ",views,"\n", "Tag:",tagg)
    else:
        for i in v:
            id, nome, autore, data, views, like, dislike, tagg = i.lower().split(";")
            data = time.ctime(float(data))
            for j in range(len(filter)):
                if filter[j] in nome or filter[j] in autore or filter[j] in tagg:
                    print("\n","ID:",id,"\n","Nome:",nome,"\n","Autore:",autore,"\n","Data:",data,"\n","Views: ",views,"\n","Tag:", tagg)
# id/username/password/permessi/karma
credentials = []
filter = []
ordination = "1"
isReverse = False
loggedUser = "NULL"  # NON UTILIZZARE QUEST VARIABILE, USARE credentials[1] PER RICEVERE L'USERNAME DELL'UTENTE LOGGATO
if __name__ == "__main__":
    print("\nEzAppunti v1.0")
    ftp = connectToServer()
    if "users.txt" in ftp.nlst():
        ftp.retrbinary("RETR users.txt", open("users.txt", "wb").write)  # TODO Hide file
    print("[1] Login\n[2] Registrazione")
    inpLoginRegister = input()
    if (inpLoginRegister == "1"):
        print("\n===LOGIN===")
        givenUsr = input("Username: ")
        givenPsw = input("Password: ")
        with open("users.txt") as f:
            for line_terminated in f:
                userData = line_terminated.split(";")
                if (userData[1] == givenUsr):
                    if (hashlib.sha256(givenPsw.encode('utf-8')).hexdigest() == userData[2]):
                        print("\nLogged successfully to " + givenUsr)
                        loggedUser = givenUsr
                        credentials = line_terminated.split(";")
                        credentials[-1] = credentials[-1].rstrip()
                        break
                    else:
                        print("Wrong password")
                        loggedUser = "WRONG_PASSWORD"
                        exitProgram()  # FIXME Non uscire dal programma, chiedi di nuovo la password
            if (loggedUser == "NULL"):
                print("No users found for entry " + givenUsr)
                exitProgram()
    elif (inpLoginRegister == "2"):
        username = input("Username: ")
        password = input("Password: ")
        confirmPassword = input("Confirm password: ")
        actions_register(ftp, username, password, confirmPassword)
    else:
        print("Invalid option")
        exitProgram()
    master_update(ftp)
    masterMap = {}
    updateMap()
    while True:
        exitLoop = True
        ls_note(ftp)
        print("")
        if filter != []:
            activeFiltersStr = ""
            for i in filter:
                activeFiltersStr += (i + " ")
            print("The filter is: " + activeFiltersStr)
            del activeFiltersStr
        else:
            print("There is no filter")
        if filter == []:
            print("\n[1]Note add\n[2]Select note\n[3]Add filter\n[4]Ordination")
        else:
            print("\n[1]Note add\n[2]Select note\n[3]Remove filter\n[4]Ordination")
        _inp = input("~ ")
        if (_inp == "1"):
            if (credentials[3] == "**" or credentials[3] == "***"):
                tag = []
                app = " "
                fileName = input("How do you want to name the note? ")
                print("What tags will this note have? Press return after each tag\nPress return again to move to the next step")
                while app != "":
                    app = input()
                    tag.append(app)
                tag.pop(-1)
                open("temp.txt", "w").close()
                os.startfile(os.path.normpath("temp.txt"))
                input("Press return after you've finished writing, remember to save the file!")
                v = open("temp.txt", "r").readlines()
                print("\nLoading....\n")
                actions_create_note("master.txt", fileName, v, credentials, ftp, tag)
            else:
                print("You don't have the right to write new files\n")
        if (_inp == "3"):
            if filter == []:
                updateMap()
                researchStr = ""
                researchStr = input("What's the filter?").lower()
                for i in researchStr.split(" "):
                    filter.append(i)
            else:
                filter = []
        if (_inp == "2"):
            print("Which note do you want to select?")
            id = input("~ ")
            actions_visual(ftp,id)
            updown_download(ftp, "data/" + id + ".txt", id + ".txt")
            print("\nTitle: " + masterMap[id].split(";")[1])
            print("Tags: " + masterMap[id].split(";")[7])
            print("<<" + open("data/" + str(id) + ".txt", "r").read() + ">>")
            inpE = ""
            while inpE != "0" and exitLoop != False:
                print("\n[1]Edit title\n[2]Edit tags\n[3]Edit text\n[4]Delete note\n[5]Like\n[6]Dislike\n[0]Exit")
                inpE = input("~ ")
                if inpE == "3" and (credentials[3] == "**" or credentials[3] == "***"):
                    os.startfile(os.path.normpath("data/" + id + ".txt"))
                    input("Press enter when you're done editing, remember to save!")
                    updown_upload(ftp, "data/" + id + ".txt", id + ".txt")
                    updateMap()
                if inpE == "1" and (credentials[3] == "**" or credentials[3] == "***"):
                    print(masterMap[id].split(";")[1])
                    newTitle = input("Which is the new title?")
                    master_edit(ftp, "master.txt", id, 1, newTitle)
                    updateMap()
                if inpE == "2" and (credentials[3] == "**" or credentials[3] == "***"):
                    inpTag = ""
                    inpStr = "a"
                    print("The old tags were: " + masterMap[id].split(";")[7])
                    inpStr = input("What's the new tags?")
                    master_edit(ftp, "master.txt", id, 7, inpStr)
                    updateMap()
                    print("The new tags are: " + masterMap[id].split(";")[7])
                if inpE == "4" and (credentials[3] == "**" or credentials[3] == "***"):
                    os.remove("data/{0}.txt".format(id))
                    master_delete(ftp, "master.txt", id)
                    updateMap()
                    exitLoop = False
                if inpE=="5":
                    actions_like(id,loggedUser,masterMap,ftp)
        if _inp == "4":
            inp = input("Ordinate for:\n[1]Id\n[2]Name\n[3]Date\n[5]Toggle reverse ordination\n")
            if inp == "0":
                isReverse = not isReverse
            else:
                ordination = inp