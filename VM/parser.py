command_types = {
    'push': 'C_PUSH',
    'pop': 'C_POP',
    'add': 'C_ARITHMETIC',
    'sub': 'C_ARITHMETIC',
    'neg': 'C_ARITHMETIC',
    'eq': 'C_ARITHMETIC',
    'gt': 'C_ARITHMETIC',
    'lt': 'C_ARITHMETIC',
    'and': 'C_ARITHMETIC',
    'or': 'C_ARITHMETIC',
    'not': 'C_ARITHMETIC'
}

class Command:
    def __init__(self, com):
        self.vmCommand = com
        self.arg1 = None
        self.arg2 = None
        
        com = com.split(' ')
        self.commandType = command_types[com[0]]
        if self.commandType == 'C_PUSH' or self.commandType == 'C_POP':
            self.arg1 = com[1]
            self.arg2 = int(com[2])
        elif self.commandType == 'C_ARITHMETIC':
            self.arg1 = com[0]
        else:
            print(f'No command for: {com}')
        


class Parser:
    def __init__(self,file, debug):
        self.debug = debug
        self.commands = []
        try:
            with open(file,'r') as f:
                data = f.readlines()
                for line in data:
                    line = line.strip()
                    if line.startswith('//'):
                        pass
                    elif len(line.strip()) ==  0:
                        pass
                    else:
                        if line.find('//') > -1:
                            line = line[:line.find('//')]
                        line = line.strip()
                        self.commands.append(line)
                        

        except Exception as e:
            print(e)
        if self.debug:
            print(self.commands)
    
    def hasMoreCommands(self):
        if len(self.commands) > 0:
            return True
        return False
    def advance(self):
        if not self.hasMoreCommands():
            return
        current_command = Command(self.commands.pop(0))
        return current_command