import os

maths = {
    'add': 'D=D+M',
    'sub': 'D=M-D',
    'gt': 'D=M>D',
    'lt': 'D=M<D',
}


class Codewriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path).split('.')[0]
        self.asm = []
        self.command_count = 0
    def save(self,file_path=None):
        file = self.file_path
        if file_path:
            file = file_path

        print(self.file_path)
        with open(file, 'w') as f:
            for line in self.asm:
                f.write(line + '\n')
    def push(self,segment,index):
        self.command_count += 1
        assembly = []
        if segment == 'constant':
            assembly.append(f'\n// Push constant {index} to stack')
            assembly.append(f'@{index}')
            assembly.append('D=A')
            assembly.append('@SP')
            assembly.append('A=M')
            assembly.append('M=D')
            assembly.append('@SP')
            assembly.append('M=M+1')
        elif segment == 'temp':
            assembly.append(f'\n// Push temp {index} to stack')
            assembly.append(f'@{index + 5}')
            assembly.append('D=M')
            assembly.append('@SP')
            assembly.append('A=M')
            assembly.append('M=D')
            assembly.append('@SP')
            assembly.append('M=M+1')
        elif segment == 'static':
            assembly.append(f'\n// Push static {index} to stack')
            assembly.append(f'@{self.file_name}.{index}')
            assembly.append('D=M')
            assembly.append('@SP')
            assembly.append('A=M')
            assembly.append('M=D')
            assembly.append('@SP')
            assembly.append('M=M+1')
        elif segment == 'pointer':
            assembly.append(f'\n// Push {"this" if index == 0 else "that"} to stack')
            assembly.append(f'@{"this" if index == 0 else "that"}')
            assembly.append('D=M')
            assembly.append('@SP')
            assembly.append('A=M')
            assembly.append('M=D')
            assembly.append('@SP')
            assembly.append('M=M+1')
        else:
            assembly.append(f'\n// Push {segment} {index} to stack')
            assembly.append(f'@{segment}')
            assembly.append('D=M')
            assembly.append(f'@{index}')
            assembly.append('D=D+A')
            assembly.append('@SP')
            assembly.append('A=M')
            assembly.append('M=D')
            assembly.append('@SP')
            assembly.append('M=M+1')
        return assembly
    def pop(self,segment,index):
        self.command_count += 1
        assembly = []
        if segment == 'constant':
            raise Exception("Constants don't support pop")
        elif segment == 'temp':
            assembly.append(f'// Pop from stack to {segment} {index}')
            assembly.append('@SP')
            assembly.append('M=A-1')
            assembly.append('A=M') 
            assembly.append('D=M')
            assembly.append('@{5+index}')
            assembly.append('M=D')
        
    
    def writeArithmetic(self,command):
        self.command_count += 1
        if command in ['add', 'sub', 'and', 'or']:
            # These commands need the top two values from the stack
            # pop from stack and store in D
            # pop second from stack and store in M
            a = [f'\n// {command}']
            a += ['@SP']
            a += ['AM=M-1']
            a += ['D=M']
            a += ['@SP']
            a += ['AM=M-1']
            if command == 'add':
                a += ['D=D+M']
            elif command == 'sub':
                a += ['D=M-D']
            elif command == 'and':
                a += ['D=M&D']
            elif command == 'or':
                a += ['D=D|M']
            else:
                # We shouldn't have got here
                a += ['Error in writeArithmetic with command {command}']
            a += ['@SP']
            a += ['A=M']
            a += ['M=D']
            a += ['@SP']
            a += ['M=M+1']
            self.asm += a
        elif command in ['lt','gt','eq']:
            # These commands need the top two values from the stack
            # pop from stack and store in D
            # pop second from stack and store in M
            a = [f'\n// {command}']
            a += ['@SP']
            a += ['AM=M-1']
            a += ['D=M // D = second number']
            a += ['@SP']
            a += ['AM=M-1']
            a += ['D=M-D // D = first number - second number']
            if command == 'lt':
                a += [f'@{command}_{self.command_count}_true']
                a += ['D;JLT']
                # a += [f'@{command}_exit']
                # a += ['0;JMP']
            elif command =='gt':
                a += [f'@{command}_{self.command_count}_true']
                a += ['D;JGT']
            elif command =='eq':
                a += [f'@{command}_{self.command_count}_true']
                a += ['D;JEQ']
            else:
                a += ['Error in writeArithmetic with command {command}']

            # if the code reaches this section
            # the results aren't true
            # so we add 0 to the stack
            a += ['@SP']
            a += ['A=M']
            a += ['M=0 // Set stack to false']
            a += ['@SP']
            a += ['M=M+1']
            a += [f'@{command}_{self.command_count}_exit']
            a += ['0;JMP', '']


            a += [f'({command}_{self.command_count}_true)']
            a += ['@SP']
            a += ['A=M']
            a += ['M=-1 // Set stack to true']
            a += ['@SP']
            a += ['M=M+1']


            a += [f'({command}_{self.command_count}_exit)']
            self.asm += a
        
        elif command in ['neg','not']:
            a = [f'\n// {command}']
            a += ['@SP']
            a += ['A=M-1']
            if command == 'not':
                a += ['M=!M']
            elif command == 'neg':
                a += ['M=-M']
            self.asm += a
    def writePushPop(self,command,segment,index):
        assembly = []
        if command == 'C_PUSH':
            # pushes an integer from ram to the stack
            assembly += self.push(segment,index)


        elif command == 'C_POP':
            # Pops last value from stack
            # and stores it in segment[index]
            pass
        
        self.asm += assembly