import sys
def db_edit(file,line,index,new):
    with open(file,"r") as f:
        lines = f.readlines()
    items = lines[line].split(";")
    out=""
    x=-1
    for i in items:
        x+=1
        if(x==index):
            out+=new
        else:
            out+=items[x]
        if not(items[x]==items[-1]):
            out+=";"
    lines[line]=out
    with open(file, "w") as f:
        f.writelines(lines)

def exitProgram():
    input("Press enter to exit ")
    sys.exit(0)