#!/usr/bin/env python

## import libs
import sys, os, getopt

## Print help
def usage():
    print "Usage: lsp [Options]... [FILE]...\n\
List FILEs (the current directory by default) with absolute or relative \
paths.\n\
The FILEs are listed in alphabetical order.\n\n\
Options:\n\
 -h, --help      : show this help message and exit\n\
 -d, --directory : starting-point for relative paths (defult current directory)"
    return

## Check input from command line
argv = sys.argv[1:] #input arguments
startpoint = os.curdir; #Set default to current directory
print_relpath = 0
try:                                
    optlist, args = getopt.gnu_getopt(argv, "hd:", ["help", "directory="])
except getopt.GetoptError, err:
    print str(err); #Print error msg
    print "type 'lsp --help' for more information"
    sys.exit(2)

for opt, arg in optlist:
    if opt in ("-h", "--help"):
        usage()
        sys.exit()
    elif opt in ("-d", "--directory"):
        startpoint = arg
        print_relpath = 1

if (len(args) < 1):
    args.append(os.curdir) #List current directory

if (os.path.isdir(startpoint)==0):
    print "'{}' is not a directory".format(startpoint)
    sys.exit(2)

#Check python interpreter version
req_ver = (2,6) #Required python version
cur_ver = sys.version_info #Current version
ver_message = "The python interpreter is too old. \
The current version is {0}.{1}.{2} and the required version is {3}.{4}."\
.format(cur_ver[0],cur_ver[1],cur_ver[2],req_ver[0],req_ver[1])

if (os.path.isdir(args[0])): #Argument is a directory
    path = args[0]
    abspath = os.path.abspath(path)
    dirList=os.listdir(path)
    dirList.sort()
    for fname in dirList:
        absfile = os.path.join(abspath,fname)
        if (os.path.isabs(path) or print_relpath):
            if (cur_ver >= req_ver):
                print os.path.relpath(absfile, startpoint)
            else:
                print ver_message 
        else:
            print absfile
else: #Argument is a file
    for fname in args:
        if (os.path.exists(fname)):
            if (os.path.isabs(fname) or print_relpath):
                if (cur_ver >= req_ver):
                    print os.path.relpath(fname, startpoint)
                else:
                    print ver_message
            else:
                print os.path.abspath(fname)
        else:
            print "lsp: cannot access '{}': No such file or directory"\
.format(fname)
