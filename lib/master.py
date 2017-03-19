from lib.util import *


def master_append(id, ftp, path, titolo, autore, dataCalendario, tags):
    """
    :param id: The id of the new note
    :type id: int
    :param ftp: The ftp object
    :type ftp: FTP
    :param path: Path where master.txt is located:
    :type path: string
    :param titolo: The title of the note
    :type titolo: string
    :param autore: The author of the note
    :type autore: string
    :param dataCalendario: The date wich the note was written, should be gathered with time.time()
    :type dataCalendario: float
    :param tags: An arrays of strings containing the tags of the note
    :type tags: string array
    """
    master_update(ftp)
    out = str(id) + ";" + titolo + ";" + autore + ";" + str(dataCalendario) + ";0;;;"
    x = -1
    for i in tags:
        x += 1
        out += i
        if (tags[x] != tags[-1]):
            out += ","
    out += "\n"
    open(path, "a").write(out)
    ftp.storbinary("STOR master.txt", open(path, "rb"))


def master_delete(ftp, path, id):
    """
    :param ftp: The ftp object
    :type ftp: FTP
    :param path: Path where master.txt is located:
    :type path: string
    :param id: The id of the note to be deleted
    :type id: int
    """
    master_update(ftp)
    line = 0
    x = -1
    with open(path) as f:
        for line_terminated in f:
            x += 1
            data = line_terminated.split(";")
            if (data[0] == id):
                line = x
                break
    with open(path, "r") as f:
        lines = f.readlines()
    lines[x] = ""
    with open(path, "w") as f:
        f.writelines(lines)
    ftp.storbinary("STOR master.txt", open(path, "rb"))


def master_edit(ftp, path, id, index, new):
    """
    :param ftp: The ftp object
    :type ftp: FTP
    :param path: Path where master.txt is located:
    :type path: string
    :param id: The id of the note to be edited
    :type id: string
    :param index: The index of the block to edit, zero based
    :type index: int
    :param new: The new string to be inserted in the specified index
    :type new: string
    """
    master_update(ftp)
    x = -1
    with open(path) as f:
        for line_terminated in f:
            x += 1
            data = line_terminated.split(";")
            if (data[0] == id):
                break
    db_edit(path, x, index, new)
    ftp.storbinary("STOR master.txt", open(path, "rb"))


def master_ls(ftp, path):
    """
    :param ftp: The ftp object
    :type ftp: FTP
    :param path: Path where master.txt is located:
    :type path: string
    """
    master_update(ftp)
    v = []
    with open(path) as f:
        for line_terminated in f:
            v.append(line_terminated.rstrip())
    return v


def master_update(ftp):
    """
    :param ftp: The ftp object
    :type ftp: FTP
    """
    if "master.txt" in ftp.nlst():
        ftp.retrbinary("RETR master.txt", open("master.txt", "wb").write)  # TODO Hide file


if __name__ == "__main__":
    print("Debugging master.py\n")
