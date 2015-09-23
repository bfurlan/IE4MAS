import sys


def myFun(x):
    print 'testing:', x
    fp = open('output.pl', 'w')
    fResult = -1
    if len(x) > 2:
        fp.write("person(p).\n")
        fp.write("name(p,'" + x + "').\n")
        fResult = 0
        print True
    fp.close()
    return fResult

# MAIN PROGRAM
value = ' '.join(sys.argv[1:])
exit(myFun(value))

