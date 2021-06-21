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
        inputer = open(out, 'a+')

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

    def mix_generate(self,type:[],size:int,out:string):
        set_1 = ''
        set_2 = ''
        inputer = open(out, 'a+')

        if 'emoji' in type:
            if set_1 == '':
                set_1 = self.emoji()
            elif set_2 == '':
                set_2 = self.emoji()

        if 'english' in type:
            if set_1 == '':
                set_1 = self.english()
            elif set_2 == '':
                set_2 = self.english()

        if 'chinese' in type:
            if set_1 == '':
                set_1 = self.chinese()
            elif set_2 == '':
                set_2 = self.chinese()

        #part_1
        while os.path.getsize(out) <= size*0.5:
            inputer.write(set_1[random.randint(0, len(set_1) - 1)])
            inputer.close()
            inputer = open(out, 'a+')

        #part_2
        while os.path.getsize(out) <= size*0.5:
            inputer.write(set_2[random.randint(0, len(set_2) - 1)])
            inputer.close()
            inputer = open(out, 'a+')

    def mix_genrate_2(self,type:[],size:int,out:string):
        set = ''
        inputer = open(out, 'a+')

        if 'emoji' in type:
            set += self.emoji()

        if 'english' in type:
            set += self.english()

        if 'chinese' in type:
            set += self.chinese()

        while os.path.getsize(out) <= size:

            inputer.write(set[ random.randint(0, len(set)-1) ])
            inputer.close()
            inputer = open(out, 'a+')

        print(f'file size: {os.path.getsize(out)}\ntarget size:{size}')

obj = Dict_generator()

