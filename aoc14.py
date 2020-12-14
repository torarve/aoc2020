import re

def get_input():
    with open('input14.txt') as file:
        return [x.strip() for x in file if x.strip()!=""]

def parse_instruction(line):
    m = None
    if line.startswith("mask"):
        m = re.fullmatch("mask = ([01X]+)", line)
        return "mask", m.groups()[0]
    else:
        m = re.fullmatch("mem\\[(\\d+)\\] = (\\d+)", line)
        return "mem", int(m.groups()[0]), int(m.groups()[1])

class Machine:
    def __init__(self):
        self.current_bitmask = None
        self.memory = {}

    def run(self, program):
        for statement in map(parse_instruction, program):
            instruction = statement[0]
            if instruction == "mask":
                self.current_bitmask = statement[-1]
            elif instruction == "mem":
                self.set_memory(statement[-2], statement[-1])
            else:
                raise "Invalid instruction"
    
    def set_memory(self, offset, value):
        if self.current_bitmask is not None:
            value = value | int(self.current_bitmask.replace("X", "0"), 2)
            value = value & int(self.current_bitmask.replace("X", "1"), 2)
        
        self.memory[offset] = value

machine = Machine()
program = get_input()
machine.run(program)

print(f"Sum of memory values for first program: {sum(machine.memory.values())}")

class Machine2:
    def __init__(self):
        self.current_bitmask = None
        self.memory = {}

    def run(self, program):
        for statement in map(parse_instruction, program):
            instruction = statement[0]
            if instruction == "mask":
                self.current_bitmask = statement[-1]
            elif instruction == "mem":
                self.set_memory(statement[-2], statement[-1])
            else:
                raise "Invalid instruction"
    
    def set_memory(self, offset, value):
        mem_address = self.apply_mask(offset)

        count = self.current_bitmask.count("X")
        for i in range(pow(2,count)):
            new_address = mem_address
            bits = f"{i:036b}"[-count:]
            for j in range(count):
                new_address = new_address.replace("X", bits[j], 1)
            
            self.memory[int(new_address)] = value

    def apply_mask(self, offset):
        def combine(x,y):
            if x=="0": return y
            elif x=="1": return "1"
            else: return "X"

        tmp = map(combine, self.current_bitmask, f"{offset:036b}")
        return "".join(list(tmp))



machine2 = Machine2()
machine2.run(program)

print(f"Sum of memory values for second program: {sum(machine2.memory.values())}")
