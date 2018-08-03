#!usr/bin/env python3

import sys
import csv
class Config(object):
    def __init__(self, fname):
        with open(fname, 'r') as file:
            self._dict = {}
            for line in file:
                strs = line.split('=')
                self._dict[strs[0].strip()] = float(strs[1].strip())
        self._dict['Rate'] = self._dict['YangLao'] + self._dict['YiLiao'] + self._dict['ShiYe'] + self._dict['GongShang'] + self._dict['ShengYu'] + self._dict['GongJiJin'];
    def get_attr(self, str):
        if self._dict.get(str) == None:
            print('No Corresponding Atrr configuration!')
            exit(-1)
        return self._dict[str];

class Workers(object):
    def cal(self, presalary, config):
        low = config.get_attr('JiShuL');
        up = config.get_attr('JiShuH');
        rate = config.get_attr('Rate');

        if presalary < low:
            insurance = low * rate
        elif presalary > up:
            insurance = up * rate
        else:
            insurance = presalary * rate
        rest = presalary - insurance - 3500

        if rest <= 0:
            tax = 0
        elif rest <= 1500:
            tax = rest * 0.03 - 0
        elif rest > 1500 and rest <= 4500:
            tax = rest * 0.10 - 105
        elif rest > 4500 and rest <= 9000:
            tax = rest * 0.20 - 555
        elif rest > 9000 and rest <= 35000:
            tax = rest * 0.25 - 1005
        elif rest > 35000 and rest <= 55000:
            tax = rest * 0.30 - 2755
        elif rest > 55000 and rest <= 80000:
            tax = rest * 0.35 - 5505
        else:
            tax = rest * 0.45 - 13505
        salary = presalary - insurance - tax
        return insurance,tax,salary

    def __init__(self, fname, config):
        with open(fname, 'r') as file:
            self._dict = {}
            for line in file:
                strs = line.split(',')
                id = strs[0].strip()
                presalary = float(strs[1].strip())
                insurance,tax,salary = self.cal(presalary, config)
                self._dict[id] = [presalary, insurance, tax, salary]
    def output(self, fname):
        with open(fname, 'w') as file:
            for key,value in self._dict.items():
                string = ''
                string = string + str(key)
                string = string + ',' + format(value[0], '.2f')
                string = string + ',' + format(value[1], '.2f')
                string = string + ',' + format(value[2], '.2f')
                string = string + ',' + format(value[3], '.2f') + '\n'
                file.write(string)

if __name__ == '__main__':
    try:
        arglist = sys.argv[1:]
        config_name = arglist[arglist.index('-c') + 1]
        input_name = arglist[arglist.index('-d') + 1]
        output_name = arglist[arglist.index('-o') + 1]
    except:
        print('Something wrong in the argument!')
        exit(-1)
    config = Config(config_name)
    workers = Workers(input_name, config)
    workers.output(output_name)
