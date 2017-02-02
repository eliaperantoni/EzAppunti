import users
import hashlib
from ftplib import FTP
import util
credentials=[]
loggedUser="NULL"#Don't refer to this, use credentials[1]
if __name__ == "__main__":
    print("\nEzAppunti v1.0")
    ftp = FTP(users.host)
    ftp.login(users.user, users.pasw)
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
                    util.exitProgram()#TODO Don't exit, prompt again for password
        if (loggedUser == "NULL"):
            print("No users found for entry " + givenUsr)
            util.exitProgram()
    while True:
        print("[1] Create new note\n[2] Edit existing note\n[3] Delete note")
        inp=input("~ ")