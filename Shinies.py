'''
Created on Aug 26, 2016

@author: Marcus
'''
import time
from test.datetimetester import DAY
fw=open('chainRecord.txt', 'w')

cont=True;
chain=0;
print("\tWelcome to the shiny chainer.")
print("\nCaught, broken, or chained? (c/b/enter)")
while cont:
    reply=input()
    if reply=='c':
        
        print('--------------------------------')
        fw.write('--------------------------------\n')
        name=input("What did you catch?")
        currDate=time.strftime("%m/%d/%Y")
        currTime=time.strftime("%H:%M:%S")
        print(name,'\n\t', currDate, 'at', currTime ,'\n\t Chain:', chain,'\n')
        fw.write(name)
        fw.write("\n")
        fw.write(currDate)
        fw.write("\n")
        fw.write(currTime)
        fw.write("\n")
        fw.write("Chain: ")
        fw.write(str(chain)+"\n")
        ##fw.write(name+'\n\t'+ currDate+ 'at'+ currTime +'\n\t Chain:'+ chain+'\n')
        fw.flush()
        chain=0
    elif reply=='':
        chain+=1
        print(chain)
    elif reply=='b':
        print("The chain has been broken.")
        chain=0;
    elif reply!='b'and reply!='c' and reply!='' and reply!='exit':
        print("please enter a valid response")
    elif reply=='exit':
        cont=False

print("Good luck chaining next time Marcus")
fw.close()    