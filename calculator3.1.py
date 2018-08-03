#!/usr/bin/env/python3

import sys
import csv
class Config(object):
   def __init__(self,fname):
        with open(fname,'r') as file:
            self._dict = {}
            for line in file:
                strs =  line.split('=')
                self._dict[strs[0].strip()] = float(strs[1].strip())
        self._dict['Rate'] = self._dict['YangLao']+self._dict['YiLiao']+self._dict['ShiYe']+self._dict['GongShang']+self._dict['ShengYu']+self._dict['GongJiJin']
    def get_attr(self,str):
        if self._dict.get(str) == None:
            print('AttributeError!')
            exit(-1)
        return self._dict.get(str)

class Calculator(object):
    def cal(self,salary,config):
        low = config.get_attr('JiShuL')
        up = config.get_attr('JiShuH')
        rate = config.get_attr('Rate')

        if salary < low:
            social = low*rate
        elif salary > up:
            social = up*rate
        else:
            social = salary*rate
        rest = salary - social - 3500

        if rest <= 0:
            tax = 0
        elif rest <=1500:
            tax = rest*0.03
        elif rest <=4500:
            tax = rest*0.10-105
        elif rest <=9000:
            tax = rest*0.20-555
        elif rest <=35000:
            tax = rest*0.25-1005
        elif rest <=55000:
            tax = rest*0.30-2755
        elif rest <=80000:
            tax = rest*0.35-5505
        else:
            tax = rest*0.45-13505
        takemoney = salary-socail-tax
        return social,tax,takmoney
    
    def __init__(self,fname,config):
        with open(fname,'r') as file:
            self._dict = {}
            for line in file:
                strs = line.split(',')
                id = strs[0].strip()
                salary = float(strs[1].strip())
                social,tax,takmoney = self.cal(salary,config)
                self._dict[id] = [salary,social,tax,takemoney]
    def output(self,fname):
        with open(fname,'w') as file:
            for key,value in self._dict.items():
                string = ''
                string = string + str(key)
                string = string + ',' + format(value[0],'.2f')
                string = string + ',' + format(value[1],'.2f')
                string = string + ',' + format(value[2],'.2f')
                string = string + ',' + format(value[3],'.2f') + '\n'
                file.write(sting)
if __name__ == '__main__':
    try:
        arglist = sys.argv[1:]
        config_name = arglist[arglist.index('-c')+1]
        input_name = arglist[arglist.index('-d')+1]
        output_name = arglist[arglist.index('-o')+1]
    except:
        print('argument error!')
        exit(-1)
    config = Config(config_name)
    calculator = Calculator(input_name,config)
    calculator.output(output_name)


