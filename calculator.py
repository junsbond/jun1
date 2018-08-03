#!/usr/bin/env python3
import sys
takepay = {}
try:
    for arg in sys.argv[1:]:
        empno, salary = arg.split(":")
        takepay[empno] = int(salary)
       # takehomepay(takepay)
except:
    print("Parameter Error")
    sys.exit()


#def social():
#    so = saraly*0.165
#    return(so)

#def tax(salary):

def takehomepay(takepay):
    for empno,salary in takepay.items():
        so = salary*0.165
        ntax = salary-so-3500
        if ntax <= 0:
            tax = 0
        elif ntax <= 1500:
            tax = ntax*0.30
        elif ntax <= 4500:
            tax = ntax*0.10-105
        elif ntax <= 9000:
            tax = ntax*0.20-555
        elif ntax <= 35000:
            tax = ntax*0.25-1005
        elif nax <= 55000:
            tax = ntax*0.30-2755
        elif ntax <= 80000:
            tax = ntax*0.35-5505
        else:
            tax = ntax*0.45-13305
        thp = salary-so-tax
        print(empno,end='')
        print(":",end='')
        print("{:.2f}".format(thp))

#if __name__ == "__main__":

#    for arg in sys.argv[1:]:
#        try:
#            empno,salary = arg.split(":")
#            takepay[empno] = int(salary)
           # takehomepay(takepay)
#        except:
#            print("Parameter Error")
#            sys.exit()
takehomepay(takepay)

