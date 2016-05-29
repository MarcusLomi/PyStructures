from Structures.StringNode import StringNode

class LinkedList(object):
    front=None;
    size=0;
    
    def __init__(self):
        self.front;
        self.size;
    
    def getSize(self):
        print()
        print(self.size)
    
    def addToFront(self, word):
        if self.front==None:
            newNode= StringNode(word, None);
            self.front=newNode;
            self.size=self.size+1;
        else:
            newNode=StringNode(word, self.front);
            self.front=newNode;
            self.size=self.size+1;
        
    def printOut(self):
        print()
        if self.size==0:
            print("There are no items in the LL")
            return;
        else:
            ptr=self.front;
            while ptr!=None:
                print(ptr.string+ " ---> ", end="")
                ptr=ptr.next
     
    def addAfter(self, tar, string):
        if self.isEmpty():
            return
        else:
            ptr=self.front
            while ptr!=None:
                if ptr.string==tar:
                    ptr.next=StringNode(string, ptr.next)
                    self.size=self.size+1
                    return
                ptr=ptr.next
        
        print("Did not find your target")
        return
    def isEmpty(self):
        if self.size==0:
            print("The list is empty")
            return True;
        
    def printReverse(self,fron):
        if fron==None:
            return;
        self.printReverse(fron.next)
        if fron.string=="None" or fron.string==None:
            print("NIGGER WHAT THE FUCK")
        print(fron.string+" <---", end="")