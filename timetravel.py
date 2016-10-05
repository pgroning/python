#!/usr/bin/env python

#import libs
import sys, os, getopt

def main():
    argv = sys.argv[1:]
    try:
        optlist, args = getopt.gnu_getopt(argv, "hx:a:d:", ["help","distance","acceleration","deceleration"])
    except getopt.GetoptError, err:
        print str(err); #Print error msg
        print "type 'timetravel --help' for more information"
        sys.exit(2)

    print args
    for opt, arg in optlist:
        #print opt,arg
        if opt in ["-h", "--help"]:
            usage()
            sys.exit()
        elif opt in ["-x", "--distance"]:
            traveldistance = arg
        elif opt in ["-a", "--acceleration"]:
            acceleration = arg
        elif opt in ["-d", "--deceleration"]:
            deceleration = arg

    travel = travelclass(traveldistance,acceleration,deceleration) # construct a travel instance
    

class travelclass(object):
    def __init__(self,distance,acceleration,deceleration):
        print "init object..."
        print distance,acceleration,deceleration

def usage():
    print "Usage: timetravel [options]...\n\
    Options:\n\
    -h, --help     : show this help text and exit\n\
    -d, --distance : distance to travel"
    
if __name__ == "__main__": # Script starts here
    main()
