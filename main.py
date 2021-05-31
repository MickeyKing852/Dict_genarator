import string, os, random

class Dict_generator:

    def english(self)->string:
        printable =''
        for i in range(0x0020, 0x007f):
            printable += chr(i)
        return printable

    def chinese(self)->string:
        printable = ''
        for i in range(0x4e00, 0x9fbf):
            printable += chr(i)
        return printable

    def generate(self,type:string,size:int,out:string)-> string:
        set = ''
        inputer = open(out, 'w+')

        if type == 'english':
            set = self.english()

        if type == 'chinese':
            set = self.chinese()

        while os.path.getsize(out) <= size:

            inputer.write(set[ random.randint(0, len(set)-1) ])
            inputer.close()
            inputer = open(out, 'a+')
        print(f'file size: {os.path.getsize(out)}\ntarget size:{size}')

obj = Dict_generator()
obj.generate('english',12,'/home/mickey/Desktop/test.txt')
