

class GameBoy:    

    def __init__(self, instr):
        self.pc = 0
        self.accumulator = 0
        self.opcode = None
        self.instr =  instr[:]
        
        self.finished = False

        self.OPS = {
            'nop': self.nop,
            'acc': self.acc,
            'jmp': self.jmp,
        }

    def nop(self, args):
        pass

    def acc(self, args):
        self.accumulator += args
        return self.accumulator

    def jmp(self, args):        
        self.pc += args-1

    def fetch(self):
        opcode, value = self.instr[self.pc].split(' ')
        self.opcode = self.OPS[opcode]
        
        self.pc += 1

        return int(value)

    def compute(self):
        while self.pc < len(self.instr):
            args = self.fetch()  
            yield self.opcode(args) 
        self.finished = True


def run(gb: GameBoy):
    loops = []
    for output in gb.compute():
        if gb.pc in loops:  
            print('Infinite loop detected at PC=', gb.pc, 'Accumulator=', gb.accumulator)          
            break
        loops.append(gb.pc)
    else:
        print(f'Program completed with patch at position {i}. Accumulator={gb.accumulator}')
        return True

def patch(instr, position):
    instr = instr[:]
    if instr[position].startswith('jmp'):
        instr[position] = instr[position].replace('jmp', 'nop')
    elif instr[position].startswith('nop'):
        instr[position] = instr[position].replace('nop', 'jmp')
    return instr


with open('input.txt', 'r') as file:
    instr = list(file.read().splitlines())


for i in range(len(instr)):
    gb = GameBoy(patch(instr, i))
    if run(gb):
        break
