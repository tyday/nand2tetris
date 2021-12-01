# Opens up a .vm file and then saves
# the saves the result as a .asm file


import os, sys
from parser import Parser
from codewriter import Codewriter

if __name__ == "__main__":
    DEBUG = True
    if len(sys.argv) < 2:
        print("need file location")
    else:
        file = os.path.abspath(sys.argv[1])
        out_file_name = os.path.basename(file).split('.')[0]
        out_file_name += '.asm'
        out_file_name = os.path.join(os.path.dirname(file), out_file_name)
        parser = Parser(file, DEBUG)
        codewriter = Codewriter(out_file_name)

        while parser.hasMoreCommands():
            current_command = parser.advance()
            if DEBUG:
                print(current_command.vmCommand, ':', current_command.commandType)
            if current_command.commandType == 'C_PUSH':
                codewriter.writePushPop(current_command.commandType,current_command.arg1,current_command.arg2)
            elif current_command.commandType == 'C_POP':
                codewriter.writePushPop(current_command.commandType,current_command.arg1,current_command.arg2)
            elif current_command.commandType == 'C_ARITHMETIC':
                codewriter.writeArithmetic(current_command.arg1)
            else:
                pass
        codewriter.save()
