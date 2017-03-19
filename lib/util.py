import sys
from ftplib import FTP
import os

outtaLib = "../"


def db_edit(file, line, index, new):
    """
    :param file: File path
    :type file: string
    :param line: Index of line to edit
    :type line: int
    :param index: Index of block to edit
    :type index: int
    :param new: Overwrite previous string with this one
    :type new: string
    """
    with open(file, "r") as f:
        lines = f.readlines()
    items = lines[line].split(";")
    out = ""
    x = -1
    for i in items:
        x += 1
        if (x == index):
            out += new
            if (items[x] == items[-1]):
                out += "\n"
        else:
            out += items[x]
        if not (items[x] == items[-1]):
            out += ";"
    lines[line] = out
    with open(file, "w") as f:
        f.writelines(lines)


def deleteFiles():
    try:
        os.remove("master.txt")
    except:
        "Error"
    try:
        os.remove("temp.txt")
    except:
        "Error"
    try:
        os.remove("master.txt")
    except:
        os.remove("users.txt")


def exitProgram(code=0):
    """
    :param code: If not 1 doesn't prompt
    :type code: int
    """
    if code == 0:
        input("\nPress enter to exit ")
        deleteFiles()
        sys.exit(0)

    else:
        deleteFiles()
        sys.exit(0)


host = "f14-preview.royalwebhosting.net"
pasw = "tooezforrtz"
user = "2289107"


def connectToServer():
    ftp = FTP(host)
    ftp.login(user, pasw)
    return ftp
