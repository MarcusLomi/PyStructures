'''
Created on May 29, 2016

@author: Marcus
'''
from Structures.StringNode import StringNode
class Stack(object):
    '''
    classdocs
    '''
    top=None
    size=0

    def __init__(self):
        '''
        Constructor
        '''
        self.top=None
        self.size=0
    
    def push(self, item):
        item.next=self.top
        self.top=item
        self.size=self.size+1
    
    def pop(self):
        if self.size==0:
            print("There is nothing to pop from the stack")
            return
        else:
            temp=self.top
            self.top=self.top.next
            return temp

    def peek(self):
        if self.size==0:
            print("The stack is empty")
            