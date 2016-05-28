class StringNode:
    string="";
    next=None;
    
    def __init__(self, word, node):
        self.string=word;
        self.next=node;