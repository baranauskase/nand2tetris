// Adds up two numbers
// Usage: put the values that you wish to add in RAM[0] and RAM[1].
// Resulet will be stored in RAM[2]

@0
D = M

@1
D = D + M

@2
M = D

//Infinite loop to prevent NOP slide
@6
0;JMP