import string, os, random
PRINTABLE =''
class Dict_generator:

    def emoji(self)->string:

        choice =random.randint(1,6)
        if choice == 1:
            return [i for i in range(0x24c2,0x1f251)]
        if choice == 2:
            return [i for i in range(0x2702,0x27b0)]
        if choice == 3:
            return [i for i in range(0x1f30d,0x1f567)]
        if choice == 4:
            return [i for i in range(0x1f600,0x1f636)]
        if choice == 5:
            return [i for i in range(0x1f680,0x1f6c0)]
        if choice == 6:
            return [i for i in range(0x1f681,0x1f6c5)]

    def english(self)->string:

       return [i for i in range(0x0020, 0x007f) ]

    def chinese(self)->string:

        return [i for i in range(0x4e00, 0x9fbf)]

    def generate(self,type:string,size:int,out:string)-> string:
        set = ''
        inputer = open(out, 'w+')

        if type == 'emoji':
            set = self.emoji()

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
#obj.generate('english',12,'/home/mickey/Desktop/test.txt')
