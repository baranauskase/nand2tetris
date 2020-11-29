// Program: Signum.asm
// Computes:  If R0 > 0
//                R1 = 1
//            else
//                R1 = 0

    @R0
    D = M   // D = RAM[0]

    @POSITIVE
    D;JGT   // JUMP to R0 > 0 case

    @R1 
    M=0     // R1 = 0

    @END
    0;JMP

(POSITIVE)
    @R1
    M=1     // R1 = 1

(END)
    @END
    0;JMP
