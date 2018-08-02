#!/usr/bin/env python3
import sys
try:
    saraly = sys.argv[1:]
except:
    print("Params Error")
    sys.exit()

def social():
    so = saraly*0.165
    return so

def tax(tax):
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
    return('{:.2f}'.format(tax))

def takehomepay(**kw):
    for arg in sys.argv[1:]:
    
