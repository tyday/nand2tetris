// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
    // There are 256 rows
    // 512 pixels per row
    // 32 Registers per row
    // 8192 total Registers
    @SCREEN
    D=A
    @8192
    D=D+A
    @lastScreenRegister
    M=D
  
(MAINLOOP)
    @KBD
    D=M
    @BLACK
    D;JGT

    @KBD
    D=M
    @WHITE
    D;JEQ

    @R0
    D=M
    @MAINLOOP
    D;JEQ

    @R0
    D=M
    @BLACK
    D;JLT

    @R0
    D=M
    @WHITE
    D;JGT

// initialize

(BLACK)
    // There are 256 rows
    // 512 pixels per row
    // 32 Registers per row
    // 8192 total Registers
    @SCREEN
    D=A
    @i
    M=D
(BLOOP)
    @i
    A=M
    M=-1
    @i
    D=M
    M=D+1
    D=M

    // Check if i > lastScreenRegister
    @lastScreenRegister
    D=D-M
    @BLOOP
    D;JLT

    @R0
    M=-1
    @MAINLOOP
    0;JMP

(WHITE)
    @R0
    D=M
    @MAINLOOP
    D;JEQ
    // There are 256 rows
    // 512 pixels per row
    // 32 Registers per row
    // 8192 total Registers
    @SCREEN
    D=A
    @i
    M=D
(WLOOP)
    @i
    A=M
    M=0
    @i
    D=M
    M=D+1
    D=M

    // Check if i > lastScreenRegister
    @lastScreenRegister
    D=D-M
    @WLOOP
    D;JLT

    @R0
    M=0
    @MAINLOOP
    0;JMP
(END)
    @END
    0;JMP