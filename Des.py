import os
import pickle

class Des:
    saved=[]

    def __init__(self,name=None):
        self.name=name
        self.filename=self.name+'.pkl'

    def __get__(self,instance,owner):
        if self.name not in Des.saved:
            raise AttributeError('%s属性未赋值'%self.name)

        with open(self.filename,'rb') as f:
            value=pickle.load(f)

        return value

    def __set__(self,instance,value):
        with open(self.filename,'wb')as f:
            pickle.dump(value,f)
            Des.saved.append(self.name)

    def __delete__(self,instance):
        os.remove(self.filename)
        Des.saved.remove(self.name)
        
