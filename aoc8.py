import re

def get_input():
    with open('input8.txt') as file:
        return [x.strip() for x in file]

def parse_instruction(line):
    m = re.fullmatch("(nop|acc|jmp) (.*)", line)
    if m is None:
        raise RuntimeError(f"Unable to parse instruction {line}")
    return m.groups()

instructions = [parse_instruction(x) for x in get_input()]

class Machine:
    def __init__(self):
        self.completed = False
        self.accumulator = None

    def run_program(self, instructions):
        lines_visited = set()
        self.accumulator = 0
        pc = 0
        while pc not in lines_visited:
            lines_visited.add(pc)
            instruction, argument = instructions[pc]
            if instruction == "nop":
                pc = pc + 1
            elif instruction == "acc":
                self.accumulator += int(argument)
                pc = pc + 1
            elif instruction == "jmp":
                pc += int(argument)
            
            if pc == len(instructions):
                break

        self.completed = pc==len(instructions)
        return self.accumulator

machine = Machine()

print(f"Accumulator when loop found: {machine.run_program(instructions)}")

for i in range(len(instructions)):
    tmp = list(instructions)
    instruction, arg = tmp[i]
    if instruction == 'jmp':
        tmp[i] = ['nop', arg]
    elif instruction == 'nop':
        tmp[i] = ['jmp', arg]
    
    machine.run_program(tmp)
    if machine.completed:
        print(f"Machine accumulator when program completes: {machine.accumulator}")
        break
