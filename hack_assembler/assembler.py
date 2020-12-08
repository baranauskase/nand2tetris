from hack_assembler.parser import make_parser

class Assembler:
    def __init__(self):
        self.machine_code = []
        self.deffered_eval = []
        self.label_address = {}
        self._var_address = {}
        self._next_var_address = 16

    def get_var_address(self, var):
        if var not in self._var_address:
            self._var_address[var] = self._next_var_address
            self._next_var_address += 1 
            
        return self._var_address[var]

    def __repr__(self):
        return '\n'.join(self.machine_code)

    def assemble(self, lines):
        for line in lines:
            parser = make_parser(line)
            parser.parse(self)

        for instruction in self.deffered_eval:
            instruction.parse(self)
