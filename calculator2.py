#!/usr/bin/env python3
import sys

def social():
    so = saraly*0.165
    print(int(so))

def tax(salary):
    if salary <= 5000:
        tax = (salary-social()-3500)*0.30
    elif salary <=8000:
        tax = (salary-socila()-3500)*0.10-105
    elif salary<=12500:
        tax = (salary-social()-3500)*0.20-555
    elif salary<=38500:
        tax = (salary-social()-3500)*0.25-1005
    elif salary<=58500:
        tax = (salary-social()-3500)*0.30-2755
    elif salary<=83500:
        tax = (salary-social()-3500)*0.35-5505
    else:
        tax = (salary-social()-3500)*0.45-13305
    print('{:.2f}'.format(tax))

def takehomepay(empno,salary):
    for empno in list[0]:
        thp = salary-social()-tax(salary)
        print(int(empno):'{:.2f}'.format(thp))

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        list = arg.split(":")    
        try:
            empno=int(list[0])
            salary=int(list[1])
            takehomepay(empno,salary)
        except:
            print("Params Error")
            sys.exit()

