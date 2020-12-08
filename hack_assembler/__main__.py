import sys
from hack_assembler.assembler import Assembler

if __name__ == '__main__':
    for source_file in sys.argv[1:]:
        with open(source_file) as f:
            assembler = Assembler()
            assembler.assemble(f)
            
            compiled_file = source_file.replace('.asm', '.hack')
            with open(compiled_file, 'w') as f:
                f.write(str(assembler))
        