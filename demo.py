class Counter:
    def __init__(self):
        super().__setattr__('counter',0)
    def __setattr__(self,name,size):
        super().__setattr__('counter',self.counter+1)
        super().__setattr__(name,value)
    def __delattr__(self,name):
        super().__setattr__('counter',self.counter-1)
        super().__delattr__(name)
        
