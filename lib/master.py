from lib.util import *
#TODO Check this file, could be messy
'''
Use master_append() to append a new entry to master file
Use master_delete() to remove an entry from master file
Use master_edit() to edit an entry from master file
Use master_ls() to get a list of all entries

<string> path always refers to the path of the file such as 'master.txt' or '../master.txt', if you don't know what to use, use 'master.txt'
<FTP> ftp always refers to the ftp object, get it with connectToServer() from util
'''

'''
<string> stitolo is the title of the note
<string> autore is the author of the note
<string> dataCalendario is the date wich the note was written, should be gathered with time.time()
<string[]> tags is an arrays of strings containing the tags of the note
'''
def master_append(ftp,path,titolo,autore,dataCalendario,tags):
    max = 0
    with open(path) as f:
        for line_terminated in f:
            data = line_terminated.split(";")
            if(line_terminated[0]!="" and int(line_terminated[0])>max):
                max=int(line_terminated[0])
    out=str(max+1)+";"+titolo+";"+autore+";"+dataCalendario+";0;0;0;"
    x=-1
    for i in tags:
        x+=1
        out+=i
        if(tags[x]!=tags[-1]):
            out+=","
    out+="\n"
    open(path,"a").write(out)
    ftp.storbinary("STOR master.txt", open(path, "rb"))

'''
<string> id is the the id of the entry
'''
def master_delete(ftp,path,id):
    line=0
    x=-1
    with open(path) as f:
        for line_terminated in f:
            x+=1
            data = line_terminated.split(";")
            if(data[0]==id):
                line=x
                break
    with open(path,"r") as f:
        lines = f.readlines()
    lines[x]=""
    with open(path, "w") as f:
        f.writelines(lines)
    ftp.storbinary("STOR master.txt", open(path, "rb"))

'''
<string> id is the id of the entry
<int> index is the index of the data to edit
<string> new is the new string to be inserted in the specified index
'''
def master_edit(ftp,path,id,index,new):
    x=-1
    with open(path) as f:
        for line_terminated in f:
            x+=1
            data = line_terminated.split(";")
            if(data[0]==id):
                break
    db_edit(path,x,index,new)
    ftp.storbinary("STOR master.txt", open(path, "rb"))
def master_ls(ftp,path):
    v=[]
    with open(path) as f:
        for line_terminated in f:
            v.append(line_terminated.rstrip())
    return v
def master_init(ftp):
    if "master.txt" in ftp.nlst():
        ftp.retrbinary("RETR master.txt", open("master.txt", "wb").write)  # TODO Hide file

if __name__=="__main__":
    print("Debugging master.py\n")
    print(master_ls(connectToServer(),"../master.txt"))