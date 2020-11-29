// Program rectangle.asm
// Draws a filled rectangle at the screens's top left corner.
// The rectangle's with is 16 pixels, and its height is RAM[0].
// Usage: put a non-negative number (rectangle's height) in RAM[0]

    // obtain height
    @R0
    D=M
    @height
    M=D

    // step size to get to the next row
    // e.g. 512/16
    @32
    D=A
    @step
    M=D    

    // last row in the screen
    // e.g. 512/16*256
    @8192
    D=A
    @last
    M=D

    // init screen base address
    @SCREEN
    D=A
    @line
    M=D

    @0
    D=A
    @rowidx
    M=0

(BLACK_LOOP)
    @rowidx
    D=M
    @height
    D=M-D
    @END
    D;JEQ

    @line
    A=M
    M=-1    // e.g. store 11111..1111

    @step
    D=M
    @line
    M=M+D

    @rowidx
    M=M+1
    @BLACK_LOOP
    0;JMP

(END)
    @END
    0; JMP
