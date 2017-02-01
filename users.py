from ftplib import FTP
import hashlib
host = "f14-preview.royalwebhosting.net"
pasw = "tooezforrtz"
user = "2289107"
loggedUser="NULL"
permissions=""
if __name__ == "__main__":
    ftp = FTP(host)
    print("Connecting to: "+host+":"+user+":"+"******")
    ftp.login(user,pasw)
    print("Successfully connected (Perhaps) to the host, downloading users.txt")#TODO Fix connection failed detection
    if "users.txt" in ftp.nlst():
        ftp.retrbinary("RETR users.txt",open("users.txt","wb").write)
    print("\n===LOGIN===")
    givenUsr=input("Username: ")
    givenPsw = input("Password: ")
    with open("users.txt") as f:
        for line_terminated in f:
            data = line_terminated.split(";")
            if (data[1] == givenUsr):
                if(hashlib.sha256(givenPsw.encode('utf-8')).hexdigest() == data[2]):
                    print("\nLogged successfully to " + givenUsr)
                    loggedUser=givenUsr
                    permissions=data[3]
                    break
                else:
                    print("Wrong password")
                    loggedUser="WRONG_PASSWORD"
        if(loggedUser=="NULL"):
            print("No users found for entry "+givenUsr)