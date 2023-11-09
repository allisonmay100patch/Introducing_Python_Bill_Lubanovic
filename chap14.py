import os

print(os.listdir('.'))
print(os.listdir('..'))

test1 = 'This is a test of the emergency text system'

fout = open('test.txt','w')

fout.write(test1)
fout.close()

test2 = open('test.txt','r')

contents = test2.readline()

print(contents == test1)

contents2 = test2.readlines()

print(contents2, contents, test1)