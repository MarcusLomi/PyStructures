'''
Created on May 28, 2016

@author: Marcus
'''

from Structures.LinkedList import LinkedList
from Structures.StringNode import StringNode
 


ll=LinkedList()
print("Welcome to the terminal.")
cont=True
while cont:
    ans=input("\tWhat do you want to do with your linked list? \n 1.Add to front, 2. Add after, 3.Printout, 4. Print reverse\n")
    while ans!='1' and  ans!='2' and  ans!='3' and ans!='4':
        ans=input("Please enter a correct value:")
    if ans=='1':
        newItem=input("What value would you like to add?")
        ll.addToFront(newItem)
    elif ans=='3':
        ll.printOut()
    elif ans=='4':
        ll.printReverse(ll.front)
    