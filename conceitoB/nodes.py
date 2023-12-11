# Symbol table
# {x: {
#    value: 1,
#    type: int
# }}

symbol_table = {}

class Node:
    def __init__(self, value: int, children: list):
        self.value = value
        self.children = children

    def Evaluate():
        pass

class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        c1 = self.children[0].Evaluate()[0]
        c2 = self.children[1].Evaluate()[0]

        c1_t = self.children[0].Evaluate()[1]
        c2_t = self.children[1].Evaluate()[1]
        
        res = None

        # Operations
        if self.value == "PLUS":
            res = c1 + c2
            t = "int"
        elif self.value == "MINUS":
            res = c1 - c2
            t = "int"
        elif self.value == "MULT":
            res = c1 * c2
            t = "int"
        elif self.value == "DIV":
            res = c1 // c2
            t = "int"
        
        # Comparisons
        elif self.value == "EQUAL":
            res = c1 == c2 
            t = "int"
            if c1_t != c2_t:
                raise "Error: invalid comparison"
        
        elif self.value == "AND":
            res = c1 and c2
            t = "int"
            if c1_t != c2_t:
                raise "Error: invalid comparison"
            
        elif self.value == "OR":
            res = c1 or c2
            t = "int"
            if c1_t != c2_t:
                raise "Error: invalid comparison"
            
        elif self.value == "GREATER_THAN":
            res = c1 > c2
            t = "int"
            if c1_t != c2_t:
                raise "Error: invalid comparison"
            
        elif self.value == "LESS_THAN":
            res = c1 < c2
            t = "int"
            if c1_t != c2_t:
                raise "Error: invalid comparison"

        # Concat
        elif self.value == "CONCAT":
            res = str(c1) + str(c2)
            t = "str"
        
        if res != None:
            if res == True:
                res = 1
            if res == False:
                res = 0
            return (res, t)
        
        print("Aqui: ", self.value, c1, c2)
         
        raise "Edge case 'Evaluate BinOp'"

class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        res = None
        if self.value == "PLUS":
            res = self.children[0].Evaluate()[0]
        elif self.value == "MINUS":
            res = self.children[0].Evaluate()[0] * -1
        elif self.value == "NOT":
            res = not self.children[0].Evaluate()[0]

        if res != None:
            return (res, "int")
        
        raise "Edge case 'Evaluate UnOp'"

class IntVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        return (self.value, 'int')


class NoOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self):
        self.value

class BlockVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        for c in self.children:
            c.Evaluate()

class IfVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        condition = self.children[0]
        if_block = self.children[1]
        else_block = self.children[2]

        if condition:
            if_block.Evaluate()
        else:
            if else_block != None:
                else_block.Evaluate()

class ForVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        init = self.children[0]
        condition = self.children[1]
        increment = self.children[2]
        block = self.children[3]

        init.Evaluate()
        while condition.Evaluate()[0]:
            block.Evaluate()
            increment.Evaluate()

class IdenVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        iden = self.value
        if iden in symbol_table.keys():
            st_value = symbol_table[iden]['value']
            st_type = symbol_table[iden]['type']
            return (st_value, st_type)
        
        raise "Error: identifier not defined"

class AssignVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        iden = self.children[0].value
        v, type_ = self.children[1].Evaluate()

        st_type = symbol_table[iden]["type"]
        if type_ != st_type:
            raise "Error: typing missmatching"
        
        symbol_table[iden]["value"] = v

class PrintVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        print(self.children[0].Evaluate()[0])

class VarDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        c1 = self.children[0]
        c2 = self.children[1]

        iden = c1.value

        # Checks if iden already was initialized before
        if iden in symbol_table.keys():
                raise "Error: variable already declared"
        
        if not c2:
            # Just declare without assign
            symbol_table[iden] = {"value": None, "type": self.value}

        else:
            # Evaluate c2 and assign
            # Check typing
            v, type_ = c2.Evaluate()
            if type_ != self.value:
                raise f"Error: variable typing. Var '{iden}' is set of type '{self.value}', but resolution is resulting in type:'{type_}' and value: '{v}'"
            symbol_table[iden] = {"value": v, "type": type_}
            
class StrVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        return (self.value, 'string')

class SquadVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        
        print("SquadVal: ", self.value)

class EmployeeVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        
        print("EmployeeVal: ", self.value)

class AddVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        
        print("AddVal: ", self.value)

class RemoveVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        
        print("RemoveVal: ", self.value)

class CreateTaskVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        
        print("CreateTaskVal: ", self.value)

class UpdateTaskVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        
        print("CreateTaskVal: ", self.value)
