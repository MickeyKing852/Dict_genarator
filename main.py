import string, os, random

class Dict_generator:
    def __init__(self):
        self.generate('ascii',1,'qw')

    def ascii(self)->string:
        return string.printable

    def generate(self,type:string,size:int,out:string)-> string:
        set = ''
        inputer = open(out, 'w+')

        if type == 'ascii' or 'ASCII':
            set = self.ascii().split()

        while self.size_check(out) != size:
            inputer.write(set[ random.randint(0, len(set)) ])
        inputer.close()

    def size_check(self,path:str)->string:
        return os.path.getsize(path)

obj = Dict_generator()
