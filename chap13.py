from datetime import time, date
import re
import time as t
f = open('today.txt','w')
f.write(str(date.today()))
f.close()
f = open('today.txt','r')
parser = '[\.]*[\d]+[\b]*'

f = open('today.txt','r')
times = re.findall(parser, f.read())
year,month,day = times
print(year,month,day)

dat = date(int(year),int(month),int(day))
dat2 = date(1992,8,9)
print(dat2.strftime('%A'))
f.close()
from datetime import timedelta
dat3 = timedelta(days=10000)
dat4 = dat3 + dat2
print(dat4)