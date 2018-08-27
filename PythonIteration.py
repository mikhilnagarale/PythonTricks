#Ref:https://www.programiz.com/python-programming/iterator


class PowTwo:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result=2**self.n
            self.n +=1
            return result
        else:
            return StopIteration


a=PowTwo(10)
x=iter(a)
print(next(x))
