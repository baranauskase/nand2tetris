// for (i=0; i<n; i++){
//    arr[i] = -1 
// }

    // define base address for array
    @100
    D=A
    @arr
    M=D

    // define array length
    @10
    D=A
    @n
    M=D

    // initialize loop index
    @i
    M=0

(LOOP)
    // find the memory location by offseting counter
    // with our array base address
    @i
    D=M
    @arr
    A = D + M

    M = -1

    // inc counter and repeat if neccessary
    @i
    M = M + 1
    D = M

    @n
    D = M - D

    @LOOP
    D; JGT

(END)
    @END
    0; JMP


