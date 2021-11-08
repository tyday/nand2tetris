import os, sys

DEBUG = True


dest_dict = {
    'X': 0b000000,
    'M': 0b1000,
    'D': 0b10000,
    'A': 0b100000
}
jump_dict = {
    "null": 0b000,
    'JGT': 0b001,
    'JEQ': 0b010,
    'JGE': 0b011,
    'JLT': 0b100,
    'JNE': 0b101,
    'JLE': 0b110,
    'JMP': 0b111
}

comp_dict = {
    '0': 0b101010000000,
    '1': 0b111111000000,
    '-1': 0b111010000000,
    'D': 0b001100000000,
    'A': 0b110000000000,
    '!D': 0b001101000000,
    '!A': 0b110001000000,
    '-D': 0b001111000000,
    '-A': 0b110011000000,
    'D+1': 0b011111000000,
    'A+1': 0b110111000000,
    'D-1': 0b001110000000,
    'A-1': 0b110010000000,
    'D+A': 0b000010000000,
    'D-A': 0b010011000000,
    'A-D': 0b000111000000,
    'D&A': 0b000000000000,
    'D|A': 0b010101000000
}

symbols_dict = {
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4,
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6,
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R10': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,
    'SCREEN': 16384,
    'KBD':24576
}

memory = set()
for k,v in symbols_dict.items():
    memory.add(v)


def parse_A_instruction(instruction, symbols, lineposition):
    instruction = instruction.strip()
    try:
        address = instruction[1:]
        if address in symbols:
            address = symbols[address]
        elif address.isdigit():
            address = int(address)
            # memory.add(address)
        else:
            address = instruction
        return address
    except Exception as e:
        print(f'Could not parse instruction: {instruction}')
        print(e)


def build_mc_for_C_instruction(dest, comp, jump):
    instruction = 0b1110000000000000
    if comp.find('M') > -1:
        instruction += 0b1000000000000
        comp = comp.replace('M', 'A')
    instruction += comp_dict[comp]

    for d in dest:
        instruction += dest_dict[d]
    instruction += jump_dict[jump]
    return instruction


def parse_C_instruction(in_instruction):
    instruction = in_instruction.strip()
    if instruction.find("//") > - 1:
        instruction = instruction[:instruction.find("//")].strip()
    dest = "X"
    comp = "null"
    jump = "null"

    if instruction.find("=") > -1:
        dest = instruction.split("=")[0].strip()
        comp = instruction.split("=")[1].strip()
        if comp.find(";") > -1:
            jump = comp.split(";")[1].strip()
            comp = comp.split(";")[0].strip()
    else:
        if instruction.find(";") > -1:
            comp = instruction.split(";")[0].strip()
            jump = instruction.split(";")[1].strip()
        else:
            comp = instruction.strip()
    return build_mc_for_C_instruction(dest, comp, jump)

def get_next_free_ram(mem):
    while True:
        if mem in memory:
            mem += 1
        else:
            return mem

def compile(file):
    data = None
    binary_data = []
    with open(file) as f:
        data = f.readlines()

    i = 0
    for line in data:
        if len(line.strip()) == 0:
            pass
        elif line.strip().startswith('@'):
            i += 1
            binary_data.append(parse_A_instruction(line,symbols_dict,i))
            if DEBUG:
                code = parse_A_instruction(line, symbols_dict,i)
                try:
                    print(f'{code:016b} -- {code:04x}')
                except:
                    print(code)
        elif line.strip().startswith('//'):
            if DEBUG: print('comment', line.strip())
        elif line.strip().startswith('('):
            # Jump marker
            symbols_dict[line.strip()[1:-1]] = i
            memory.add(i)
            if DEBUG: print(f'{line}  --  {line.strip()[1:-1]} : {i}')
        else:
            i += 1
            binary_data.append(parse_C_instruction(line))
            if DEBUG: print(
                f'{parse_C_instruction(line):016b} -- {parse_C_instruction(line):x}')
        
    mem = 16
    for j in range(len(binary_data)):
        line = binary_data[j]
        if isinstance(line,str):
            variable = line[1:]
            if not variable in symbols_dict:
                # assign the symbol a place in available memory
                mem = get_next_free_ram(mem)
                memory.add(mem)
                symbols_dict[variable] = mem
            
            line = parse_A_instruction(line, symbols_dict,i)
            binary_data[j] = line
        
        

    return binary_data             

if __name__ == '__main__':
    DEBUG = False
    # file = "E:\\OneDrive\\Desktop\\nand2tetris\\projects\\Assembler\\testfile.asm"
    file = '/home/ty/Desktop/nand2tetris/projects/assembler/testfile.asm'

    if len(sys.argv) > 1:
        file = sys.argv[1]

    file_path = os.path.abspath(file)
    binary_data =compile(file_path)

    new_file_name = os.path.basename(file_path).split('.')[0]
    new_file_name += '.hack'
    with open(new_file_name,'w') as f:
        for line in binary_data:
            f.write(f'{line:016b}\n')
    
