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

(LOOP)
    // reset screen base
    @SCREEN
    D=A
    @screenreg
    M=D

    // last screen register e.g. screen base address + 32 * 256
    @SCREEN
    D=A
    @8192
    D=D+A
    @lastscreenreg
    M=D      

    // check if key is pressed
    @KBD
    D=M

    // if it is then we need to fill the screen
    @KEYDOWN
    D;JGT

    // otherwise we need to clear the screen
    @fill
    M=0
    @DRAW
    0;JMP

(KEYDOWN)
    @fill
    M=-1  

(DRAW)
    @fill
    D=M

    @screenreg
    A=M
    M=D

    @screenreg
    M=M+1
    D=M

    @lastscreenreg
    D=M-D

    @DRAW
    D;JGT

    @LOOP
    0;JMP