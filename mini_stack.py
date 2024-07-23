"Problem to perform all the operations of the stack"
"Push,Pull,top"

class Stack :
    
    def __init__(self):
        self.stack = []
        self.n = 0
        
    def push (self,item):
        self.stack.append(item)
        self.n += 1
        
    def pull(self):
        if self.n == 0:
            print("Stack is empty")
        self.stack.pop()
        self.n -= 1
        
    def top(self):
        if self.stack == 0:
            print("Stack is empty")
            
        return self.stack[-1]
    
    def len(self):
        return self.n
    
    def __str__(self):
        
        return str(self.stack)
    
    
        
        
        
        