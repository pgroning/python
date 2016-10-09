#!/usr/bin/env python

#import libs
import sys, os, getopt, math
from IPython.core.debugger import Tracer

def main():
    argv = sys.argv[1:]
    try:
        optlist, args = getopt.gnu_getopt(argv, "hx:a:d:", ["help","distance","acceleration","deceleration"])
    except getopt.GetoptError, err:
        print str(err) #Print error msg
        print "type 'timetravel --help' for more information"
        sys.exit(2)

    print optlist
    print args
    
    for opt, arg in optlist:
        #print opt,arg
        if opt in ["-h", "--help"]:
            usage()
            sys.exit()
        elif opt in ["-x", "--distance"]:
            traveldistance = float(arg) * 3*10**8 * 3600*24*365 # ly -> m
        elif opt in ["-a", "--acceleration"]:
            acceleration = float(arg) * 9.81 # g -> m/s^2 
        elif opt in ["-d", "--deceleration"]:
            deceleration = float(arg) * 9.81 # g -> m/s^2

    travel = travelclass(traveldistance,acceleration,deceleration) # construct a travel instance
    

class travelclass(object):
    def __init__(self,dist,acc,dec):
        print "init object..."
        print dist,acc,dec
        self.speed_of_light = 3*10**8 #speed of light in vaccum (m/s)
        self.ksi = 1.0 + dist / (self.speed_of_light**2*(1/acc + 1/dec))

        T_tot, T_acc, T_dec = self.elapsed_coord_time(acc,dec)
        print self.elapsed_proper_time(acc,dec)
        print self.elapsed_coord_time(acc,dec)
        print self.maxvel(acc,T_acc)

    def elapsed_proper_time(self,acc,dec):
        c0 = self.speed_of_light
        Tau_tot = c0*(1/acc+1/dec)*math.log(self.ksi+math.sqrt(self.ksi**2-1))
        Tau_acc = Tau_tot/(1.0+acc/dec)
        Tau_dec = Tau_tot - Tau_acc
        return Tau_tot, Tau_acc, Tau_dec

    def elapsed_coord_time(self,acc,dec):
        c0 = self.speed_of_light
        T_tot = c0*(1/acc+1/dec)*math.sqrt(self.ksi**2-1)
        T_acc = T_tot/(1.0+acc/dec)
        T_dec = T_tot - T_acc
        return T_tot, T_acc, T_dec

    def maxvel(self,acc,T_acc):
        c0 = self.speed_of_light
        Vmax = acc * T_acc / math.sqrt(1.0 + (acc*T_acc/c0)**2)
        return Vmax
    
def usage():
    print "Usage: timetravel [options]...\n\
    Options:\n\
    -h, --help     : show this help text and exit\n\
    -d, --distance : distance to travel"
    
if __name__ == "__main__": # Script starts here
    main()
