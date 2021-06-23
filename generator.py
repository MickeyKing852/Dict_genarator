import string, os, random, sys

class Dict_generator:

    def emoji(self) -> string:
        return [chr(i) for i in range(0x1F601,0x1F64F) and range(0x2702, 0x27B0) and range(0x1F680,0x1F6C0) and range(0x1F600,0x1F636) and range(0x1f681, 0x1f6c5) and range(0x1F30D,0x1F567)]

    def english(self) -> string:

        return [chr(i) for i in range(0x0020, 0x7f)]

    def chinese(self) -> string:

        return [chr(i) for i in range(0x4e00, 0x9ff0)]

    def generate(self, type: string, size: int, out: string) -> string:
        set = ''
        inputer = open(out, 'a+')

        if 'emoji' in type:
            set = self.emoji()

        if 'english' in type:
            set = self.english()

        if 'chinese' in type:
            set = self.chinese()

        while os.path.getsize(out) <= size:
            data = set[random.randint(0, len(set) - 1)]
            inputer.write(data)
            inputer.close()
            inputer = open(out, 'a+')

        print(f'file size: {os.path.getsize(out)}\ntarget size:{size}')

    def mix_generate(self, type: [], size: int, out: string):

        set_1 = ''
        set_2 = ''
        set_3 = ''
        persent_1 = 1.0
        persent_2 = 1.0
        persent_3 = 1.0

        if 'emoji' in type:
            if set_1 == '':
                set_1 = self.emoji()
            elif set_2 == '':
                set_2 = self.emoji()
            elif set_3 == '':
                set_3 = self.emoji()
            else: pass

        if 'english' in type:
            if set_1 == '':
                set_1 = self.english()
            elif set_2 == '':
                set_2 = self.english()
            elif set_3 == '':
                set_3 = self.english()
            else: pass

        if 'chinese' in type:
            if set_1 == '':
                set_1 = self.chinese()
            elif set_2 == '':
                set_2 = self.chinese()
            elif set_3 == '':
                set_3 = self.chinese()
            else: pass

        if set_1 and set_2 and set_3 != '':
            persent_1 = 1/3
            persent_2 = 1/3
            persent_3 = 1/3

        elif set_1 and set_2 != '':
            persent_1 = 1/2
            persent_2 = 1/2

        else: pass

        inputer = open(out, 'a+')

        # part_1
        while os.path.getsize(out) <= size * persent_1:
            inputer.write(set_1[random.randint(0, len(set_1) - 1)])
            inputer.close()
            inputer = open(out, 'a+')
        print('part 1 fin')
        print(persent_1)
        print(f'file size: {os.path.getsize(out)}')

        inputer.close()
        inputer = open(out, 'a+')

        # part_2
        while os.path.getsize(out) <= size * (persent_1+persent_2):
            inputer.write(set_2[random.randint(0, len(set_2) - 1)])
            inputer.close()
            inputer = open(out, 'a+')
        print('part 2 fin')
        print(persent_2)
        print(f'file size: {os.path.getsize(out)}')

        inputer.close()
        inputer = open(out, 'a+')

        #part3
        while os.path.getsize(out) <= size * (persent_1+persent_2+persent_3):
            inputer.write(set_3[random.randint(0, len(set_3) - 1)])
            inputer.close()
            inputer = open(out, 'a+')

        print('part 3 fin')
        print(persent_3)
        print(f'file size: {os.path.getsize(out)}\ntarget size:{size}')

class input_err(Exception):
    pass

if __name__ == '__main__':

    try:
        obj = Dict_generator()
        type = []
        size = 0
        out = ''

        if '-t' and '-size' and '-o' not in sys.argv:
            raise input_err

        if (sys.argv.index('-size') - sys.argv.index('-t') > 1):
            for i in range(1,sys.argv.index('-size') - sys.argv.index('-t')):
                type.append(sys.argv[sys.argv.index('-t') + i])
        else:
            type.append(sys.argv[sys.argv.index('-t') + 1])

        print(type)

        size = sys.argv[sys.argv.index('-size') + 1]
        out = sys.argv[sys.argv.index('-o') + 1]

        if len(type) > 1:
            obj.mix_generate(type, int(size), out)
        else:
            obj.generate(type, int(size), out)

    except input_err:
        print('python3 generator.py -t [chinese english emoji] -size -o outfile')

