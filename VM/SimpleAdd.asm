// Push constant 7 to stack
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
// Push constant 8 to stack
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
MA=M-1
D=M
@SP
M=M-1
A=M
D=D+M
@SP
A=M
M=D
