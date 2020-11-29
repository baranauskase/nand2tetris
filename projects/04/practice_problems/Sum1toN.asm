// Program: sum1toN.asm
// Computes RAM[1] = 1+2+ ... +n
// Usage: put a number (n) in RAM[0]

@counter
M=1

@R1
M=0

(ADD_NEXT)
    @R0
    D=M
    @counter
    D=D-M

    @END
    D;JLT    // check if we are done counting

    @counter
    D=M
    @R1
    M=M+D

    @counter
    M=M+1   // inc counter

    @ADD_NEXT
    0;JMP 

(END)
    @END
    0;JMP
