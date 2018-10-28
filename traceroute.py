#!/usr/bin/env python3
from __future__ import print_function
import matplotlib.pyplot as plot
import re
def delay(fileName, saveFile):
    '''
    :get the information from a file(fileName):
    :then save the result to a new File(saveFile):
    ::
    '''
    readFile= open(fileName, 'r')
    timeRead = re.compile('([0-9.]+)')
    saveToFile = open(saveFile, 'w')
    ilist=[]
    for times in readFile.readlines():
        if "akamaitechnologies.com" in times:
            findRead = timeRead.findall(times)
            dealyTimes= findRead[-1]
            p=float(dealyTimes.strip())
            ilist.append(p)
    ilist.sort(key=float)
    saveToFile.writelines(str(ilist))
    print("There is {} values".format(len(ilist)))
    readFile.close()
    saveToFile.close()
    y = []
    elist = len(ilist)
    y.append(float(1) / elist)
    for i in range(2, elist + 1):
        y.append(float(1) / elist + y[i - 2])
    plot.plot(ilist,y)
    plot.ylim(0, 1.02)
    plot.xlim(0, ilist[-1])
    plot.title('CDF of tracerouting www.svt.se website\nHighest Value = {}, and Lowest Value = {}\nThere are {} values'.format(ilist[-1], ilist[0],(len(ilist))))
    plot.savefig('processedDelay.png')
    plot.grid(True)
    plot.show()
if __name__=="__main__":
    delay('traceDump.txt', 'traceroute.txt')
