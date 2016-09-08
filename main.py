#The purpose of this program is to download data from various
#specified exchanges to run backtests against various trading strageties

import statuses as s
import apiengine
import orderengine

import os
import sys
import time
import urllib2

import csv

DIRECTORY = "./data/" #the directory to store the data
SNAPSHOTS = 10

def run(context,currencies,count):
	prefix = DIRECTORY + "snapshot_" + str(count) + "_"
	exchanges = apiengine.get_books(context,currencies,0,30)
	for i in range(len(exchanges)):
		name = context[i].__class__.__name__
		for ii in range(len(exchanges[i])):
			prefixf = prefix + currencies[ii][0] + "-" + currencies[ii][1] + "_"
			bids = exchanges[i][ii][0]
			asks = exchanges[i][ii][1]
			with open(prefixf + 'bids_' + name + '.csv', 'wb') as csvfile:
				f = csv.writer(csvfile)
				for bid in bids:
					f.writerow(bid)
			with open(prefixf + 'asks_' + name + '.csv', 'wb') as csvfile:
				f = csv.writer(csvfile)
				for ask in asks:
					f.writerow(ask)

def main():
    context = apiengine.CONTEXT
    currencies = apiengine.CURRENCIES
    balance = apiengine.BALANCE
    print(s.RUNNING + "Operating using " + str(len(currencies)) + " currency combinations")
    addresses = apiengine.ADDRESSES

    if not os.path.exists("./data"):
    	os.makedirs("./data")

    i = 0
    print("")
    while(i<SNAPSHOTS):
        chars = ["-", "\\" , "|", "/"]
        
        try:
            run(context,currencies,i)
        except urllib2.HTTPError:
            print(s.ERROR + "CONNECTION REFUSED")
            i -= 1
                
        time.sleep(1)
        print(chars[i%(len(chars))])
        sys.stdout.write('\x1b[1A')   #go back up a line, makes a cool "loading" animation
        i += 1
    
if __name__ == '__main__':
    main()