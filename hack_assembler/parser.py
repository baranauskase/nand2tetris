def make_parser(instruction):
    instruction = instruction.split('//')[0]
    instruction = instruction.strip()
    instruction = ''.join(instruction.split(' '))

    if len(instruction) == 0:
        return Noop()
    elif instruction.startswith('@'):
        return CParser(instruction)
    elif instruction.startswith('(') and instruction.endswith(')'):
        return Label(instruction)
    else:
        return AParser(instruction)

class Noop:
    def parse(self, assembler):
        pass

class Label:
    def __init__(self, label):
        self._label = label

    def parse(self, assembler):
        label_val = self._label[1:-1]
        assembler.label_address[label_val] = len(assembler.machine_code)

class CParser:
    def __init__(self, instruction):
        self._instruction = instruction
        self._instruction_idx = -1

        self._named_address = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'KBD': 24576
        }   
        for i in range(16):
            self._named_address[f'R{i}'] = i

    def parse(self, assembler):
        val = self._instruction[1:]

        if val in self._named_address:
            val = self._named_address[val]

        if self._instruction_idx > -1:
            if val in assembler.label_address:
                val = assembler.label_address[val]
            else:
                val = assembler.get_var_address(val)

        try:
            binary_val = bin(int(val))[2:]
            binary_val = binary_val.zfill(16)
        except ValueError:
            assembler.deffered_eval.append(self)
            assembler.machine_code.append(None)
            self._instruction_idx = len(assembler.machine_code) - 1
            return

        if self._instruction_idx > 0:
            assembler.machine_code[self._instruction_idx] = binary_val
        else:
            assembler.machine_code.append(binary_val)

class AParser:
    def __init__(self, instruction):
        self._instruction = instruction

        self._d_lookup = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            '!D': '001101',
            '-D': '001111',
            'D+1': '011111',
            'D-1': '001110'
        }

        self._am_lookup = {
            'A': 'value',
            'M': 'value',
            '!A': 'not',
            '!M': 'not',
            '-A': 'negate',
            '-M': 'negate',
            'A+1': 'increment',
            'M+1': 'increment',
            'A-1': 'decrement',
            'M-1': 'decrement',
            'D+A': 'add',
            'A+D': 'add',
            'D+M': 'add',
            'M+D': 'add',
            'D-A': 'subtrahend',
            'D-M': 'subtrahend',
            'A-D': 'minuend',
            'M-D': 'minuend',
            'D&A': 'and',
            'A&D': 'and',
            'D&M': 'and',
            'M&D': 'and',    
            'D|A': 'or',
            'A|D': 'or',
            'D|M': 'or',
            'M|D': 'or',     
        }

        self._am_common = {
            'value': '110000',
            'not': '110001',
            'negate': '110011',
            'increment': '110111',
            'decrement': '110010',
            'add': '000010',
            'subtrahend': '010011',
            'minuend': '000111',
            'and': '000000',
            'or': '010101'
        }

        self._jump_lookup = {
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }

    def _build_comp(self, comp):
        if 'A' in comp or 'M' in comp:
            am_common_code = self._am_lookup[comp]
            comp_code = self._am_common[am_common_code]
        else:
            comp_code = self._d_lookup[comp]

        a_bit = int('M' in comp)

        return f'{a_bit}{comp_code}'

    def _build_dest(self, dest):
        d1 = int('A' in dest)
        d2 = int('D' in dest)
        d3 = int('M' in dest)

        return f'{d1}{d2}{d3}'

    def _build_jump(self, jump):
        return self._jump_lookup.get(jump, '000')

    def parse(self, assembler):
        instruction = self._instruction
        
        dest = ''
        if '=' in instruction:
            dest, instruction = instruction.split('=')

        jump = None
        if ';' in instruction:
            instruction, jump = instruction.split(';')

        comp = instruction

        comp_bits = self._build_comp(comp)
        dest_bits = self._build_dest(dest)
        jump_bits = self._build_jump(jump)

        machine_code = f'111{comp_bits}{dest_bits}{jump_bits}'

        assembler.machine_code.append(machine_code)