
// Push constant 17 to stack
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 17 to stack
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M // D = second number
@SP
AM=M-1
D=M-D // D = first number - second number
@eq_3_true
D;JEQ
@SP
A=M
M=0 // Set stack to false
@SP
M=M+1
@eq_3_exit
0;JMP

(eq_3_true)
@SP
A=M
M=-1 // Set stack to true
@SP
M=M+1
(eq_3_exit)

// Push constant 17 to stack
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 16 to stack
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M // D = second number
@SP
AM=M-1
D=M-D // D = first number - second number
@eq_6_true
D;JEQ
@SP
A=M
M=0 // Set stack to false
@SP
M=M+1
@eq_6_exit
0;JMP

(eq_6_true)
@SP
A=M
M=-1 // Set stack to true
@SP
M=M+1
(eq_6_exit)

// Push constant 16 to stack
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 17 to stack
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
AM=M-1
D=M // D = second number
@SP
AM=M-1
D=M-D // D = first number - second number
@eq_9_true
D;JEQ
@SP
A=M
M=0 // Set stack to false
@SP
M=M+1
@eq_9_exit
0;JMP

(eq_9_true)
@SP
A=M
M=-1 // Set stack to true
@SP
M=M+1
(eq_9_exit)

// Push constant 892 to stack
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 891 to stack
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M // D = second number
@SP
AM=M-1
D=M-D // D = first number - second number
@lt_12_true
D;JLT
@SP
A=M
M=0 // Set stack to false
@SP
M=M+1
@lt_12_exit
0;JMP

(lt_12_true)
@SP
A=M
M=-1 // Set stack to true
@SP
M=M+1
(lt_12_exit)

// Push constant 891 to stack
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 892 to stack
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M // D = second number
@SP
AM=M-1
D=M-D // D = first number - second number
@lt_15_true
D;JLT
@SP
A=M
M=0 // Set stack to false
@SP
M=M+1
@lt_15_exit
0;JMP

(lt_15_true)
@SP
A=M
M=-1 // Set stack to true
@SP
M=M+1
(lt_15_exit)

// Push constant 891 to stack
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 891 to stack
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
AM=M-1
D=M // D = second number
@SP
AM=M-1
D=M-D // D = first number - second number
@lt_18_true
D;JLT
@SP
A=M
M=0 // Set stack to false
@SP
M=M+1
@lt_18_exit
0;JMP

(lt_18_true)
@SP
A=M
M=-1 // Set stack to true
@SP
M=M+1
(lt_18_exit)

// Push constant 32767 to stack
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 32766 to stack
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M // D = second number
@SP
AM=M-1
D=M-D // D = first number - second number
@gt_21_true
D;JGT
@SP
A=M
M=0 // Set stack to false
@SP
M=M+1
@gt_21_exit
0;JMP

(gt_21_true)
@SP
A=M
M=-1 // Set stack to true
@SP
M=M+1
(gt_21_exit)

// Push constant 32766 to stack
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 32767 to stack
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M // D = second number
@SP
AM=M-1
D=M-D // D = first number - second number
@gt_24_true
D;JGT
@SP
A=M
M=0 // Set stack to false
@SP
M=M+1
@gt_24_exit
0;JMP

(gt_24_true)
@SP
A=M
M=-1 // Set stack to true
@SP
M=M+1
(gt_24_exit)

// Push constant 32766 to stack
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 32766 to stack
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
AM=M-1
D=M // D = second number
@SP
AM=M-1
D=M-D // D = first number - second number
@gt_27_true
D;JGT
@SP
A=M
M=0 // Set stack to false
@SP
M=M+1
@gt_27_exit
0;JMP

(gt_27_true)
@SP
A=M
M=-1 // Set stack to true
@SP
M=M+1
(gt_27_exit)

// Push constant 57 to stack
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 31 to stack
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// Push constant 53 to stack
@53
D=A
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D+M
@SP
A=M
M=D
@SP
M=M+1

// Push constant 112 to stack
@112
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@SP
A=M
M=D
@SP
M=M+1

// neg
@SP
A=M-1
M=-M

// and
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M&D
@SP
A=M
M=D
@SP
M=M+1

// Push constant 82 to stack
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D|M
@SP
A=M
M=D
@SP
M=M+1

// not
@SP
A=M-1
M=!M
