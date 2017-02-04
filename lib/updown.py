from lib.util import *
def updown_upload(ftp,localPath,name):
    ftp.storbinary("STOR data/"+name, open(localPath, "rb"))
def updown_download(ftp,localPath,name):
    ftp.retrbinary("RETR data/"+name, open(localPath, "wb").write)
if __name__ == "__main__":
    updown_download(connectToServer(), "../README.md", "README.md")