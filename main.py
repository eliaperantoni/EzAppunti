from lib.master import *
import hashlib
from lib.actions import *
from lib.util import *
from lib.updown import *
import os
import webbrowser

cfg = open("ezappunti.cfg", "r").readlines()
# FIXME Not working when import class color in another file outside of this folder
useColors = "True" in cfg[0]

def log(text,type="Verbose"):
    out="[{0}][{1}][{2}][{3}] {4}\n".format( time.ctime(time.time()), type, credentials[1], credentials[0], text)
    open("log.txt","a").write(out)

class color:
    if useColors:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    else:
        PURPLE = ''
        CYAN = ''
        DARKCYAN = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERLINE = ''
        END = ''


def updateMap():
    for i in master_ls(ftp, "master.txt"):
        masterMap[i.split(";")[0]] = i


def ls_note(ftp):
    """
    :param ftp: The FTP object
    :type ftp: FTP
    """
    vector = []
    v = master_ls(ftp, "master.txt")
    ###
    dict = {"1": 0, "2": 1, "3": 3, "4": 2, "5": 4, "6": 5, "7": 6}
    toTreatAsInts = ["1", "3"]
    toConsiderLength = ["6", "7"]
    sortKey = ""
    if ordination in toTreatAsInts:
        v.sort(key=lambda x: int(x.split(";")[dict[ordination]]))
    elif ordination in toConsiderLength:
        def sortLength(x):
            v=x.split(";")[dict[ordination]].split(",")
            return len(val for val in v if val != "")
        v.sort(key=lambda x: [val for val in x.split(";")[dict[ordination]].split(",") if val != ""])
    else:
        v.sort(key=lambda x: x.split(";")[dict[ordination]])
    ###
    if (isReverse):
        v = v[::-1]
    if filter == []:
        for i in v:
            id, nome, autore, data, views, like, dislike, tagg = i.split(";")
            data = time.ctime(float(data))
            like.split(",")
            dislike.split(",")
            print("\n", color.GREEN + "ID:", id + color.END, "\n", "Title:", nome, "Author:", autore, "\n", "Date:",
                  data, "\n", "Views:",
                  views, "Likes:", len(like), "Dislikes:", len(dislike), "\n", "Tags:", tagg)
    else:
        for i in v:
            id, nome, autore, data, views, like, dislike, tagg = i.lower().split(";")
            data = time.ctime(float(data))
            like.split(",")
            dislike.split(",")
            for j in range(len(filter)):
                if filter[j] in nome or filter[j] in autore or filter[j] in tagg:
                    print("\n", color.GREEN + "ID:", id + color.END, "\n", "Title:", nome, "Author:", autore, "\n",
                          "Date:", data, "\n",
                          "Views:", views, "Likes:", len(like), "Dislikes:", len(dislike), "\n", "Tags:",
                          tagg)


# id/username/password/permessi/karma
credentials = []
filter = []
ordination = "1"
isReverse = False
loggedUser = "NULL"  # NON UTILIZZARE QUEST VARIABILE, USARE credentials[1] PER RICEVERE L'USERNAME DELL'UTENTE LOGGATO
if __name__ == "__main__":
    print(color.BLUE + "\nEzAppunti v1.0" + color.END)
    ftp = connectToServer()
    if "users.txt" in ftp.nlst():
        ftp.retrbinary("RETR users.txt", open("users.txt", "wb").write)  # TODO Hide file
    print("[1] Login\n[2] Registrazione\n[3] Segnala Bug")
    inpLoginRegister = input()
    if (inpLoginRegister == "1"):
        print(color.BLUE + "\n===LOGIN===" + color.END)
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
                        f.close()
                        exitProgram()  # FIXME Non uscire dal programma, chiedi di nuovo la password
            if (loggedUser == "NULL"):
                print("No users found for entry " + givenUsr)
                f.close()
                exitProgram()
    elif (inpLoginRegister == "2"):
        print(color.BLUE + "\n===REGISTER===" + color.END)
        username = input("Username: ")
        password = input("Password: ")
        confirmPassword = input("Confirm password: ")
        credentials = actions_register(ftp, username, password, confirmPassword).split(";")
    elif inpLoginRegister == "3":
        webbrowser.open("https://github.com/hellix08/EzAppunti/issues/new")
        exitProgram()
    else:  # FIXME
        print("Invalid option")
        exitProgram()
    log("Firing up the program","Info")
    masterMap = {}
    while True:
        master_update(ftp)
        updateMap()
        exitLoop = True
        ls_note(ftp)
        print("")
        if filter != []:
            activeFiltersStr = ""
            for i in filter:
                activeFiltersStr += (i + " ")
            print(color.YELLOW + "The filter is: " + activeFiltersStr + color.END)
            del activeFiltersStr
        else:
            print(color.YELLOW + "There is no filter" + color.END)
        if filter == []:
            print("\n[1]Note add\n[2]Select note\n[3]Add filter\n[4]Ordination\n[0]Exit")
        else:
            print("\n[1]Note add\n[2]Select note\n[3]Remove filter\n[4]Ordination\n[0]Exit")
        _inp = input("~ ")
        if (_inp == "1"):
            if (credentials[3] == "**" or credentials[3] == "***"):
                tag = []
                app = " "
                fileName = input("How do you want to name the note? ")
                print(
                    "What tags will this note have? Press return after each tag\nPress return again to move to the next step")
                while app != "":
                    app = input()
                    tag.append(app)
                tag.pop(-1)
                open("temp.txt", "w").close()
                os.startfile(os.path.normpath("temp.txt"))
                input(color.BLUE + "Press return after you've finished writing, remember to save the file!" + color.END)
                v = open("temp.txt", "r").readlines()
                print(color.YELLOW + "\nLoading....\n" + color.END)
                idC=actions_create_note("master.txt", fileName, v, credentials, ftp, tag)
                log("Created a note ID:{0} Title:{1} Tags:{2}".format(idC,fileName,tag))
                updateMap()
            else:
                print(color.RED + "You don't have the right to write new files\n" + color.END)
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
            ids = [val.split(";")[0] for val in master_ls(ftp,"master.txt")]
            if(not id in ids):
                print(color.RED+"No such id"+color.END)
                continue
            actions_visual(ftp, id)
            updown_download(ftp, "data/" + id + ".txt", id + ".txt")
            print("\nTitle: " + masterMap[id].split(";")[1])
            print("Tags: " + masterMap[id].split(";")[7])
            print(color.GREEN + "<<\n" + color.END + open("data/" + str(id) + ".txt",
                                                          "r").read() + color.GREEN + ">>" + color.END)
            inpE = ""
            while inpE != "0" and exitLoop != False:
                print(
                    "-----\n[+]Like\n[-]Dislike\n-----\n[1]Edit title\n[2]Edit tags\n[3]Edit text\n[4]Delete note\n[0]Exit")
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
                    inpStr = input("Insert now new tags separated by a comma:")
                    master_edit(ftp, "master.txt", id, 7, inpStr)
                    updateMap()
                    log("Edited tags to:{0}".format(inpStr))
                    print("The new tags are: " + masterMap[id].split(";")[7])
                if inpE == "4" and (credentials[3] == "**" or credentials[3] == "***"):

                    os.remove("data/{0}.txt".format(id))
                    master_delete(ftp, "master.txt", id)
                    updateMap()
                    exitLoop = False
                    log("Deleted note with ID:{0}".format(id))
                if inpE == "+":
                    actions_like(ftp, id, credentials[0])
                if inpE == "-":
                    actions_dislike(ftp, id, credentials[0])
        if _inp == "4":
            inp = input(
                "Ordinate for:\n[1]Id\n[2]Name\n[3]Date\n[4]Author\n[5]View\n[6]Likes\n[7]Dislikes\n[0]Toggle reverse ordination\n")
            if inp == "0":
                isReverse = not isReverse
            else:
                ordination = inp
        if _inp == "0":
            exitProgram(1)
