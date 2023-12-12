from main import *



symbol_table = {}
# Symbol table
# {x: {
#    value: 1,
#    type: int
# }}

squads_table={}
employee_array=[]
temp_var = ""

current_task = {}
# Squads table
# {
#     "squad_name": {
#         "employees": [],
#         "tasks": {
#             "task_name": {
#                 "status": "status",
#                 "owner": "owner",
#             }
#         }
#     }
# }

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
        
        if res != None:
            if res == True:
                res = 1
            if res == False:
                res = 0
            return (res, t)
         
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
        global current_task
        global temp_var
        task_var = self.children[0]
        employee = self.children[1]
        block = self.children[2]

        # print("ForVal: ", task_var, employee)
 
        temp_var = task_var

        if employee not in employee_array:
            raise "Error: employee not declared"
        
        employee_tasks = []
        for squad_items in squads_table.values():
            for task in squad_items["tasks"].values():
                if task["owner"] == employee:
                    employee_tasks.append(task)

        # print("Employee tasks: ", employee_tasks)
        for task in employee_tasks:
            current_task = task
            block.Evaluate()
        


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
        squad_name = self.children[0]
        if squad_name in squads_table.keys():
            raise "Error: squad already declared"
        squads_table[squad_name] = {"employees": [], "tasks": {}}
        if VERBOSE_MODE:
            print(f"Created squad '{squad_name}'")

class EmployeeVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        employee_name = self.children[0]
        if employee_name in employee_array:
            raise "Error: employee already declared"
        employee_array.append(employee_name)
        if VERBOSE_MODE:
            print(f"Created employee '{employee_name}'")

class AddVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        squad_name = self.children[0]
        employee_name = self.children[1]

        if squad_name not in squads_table.keys():
            raise "Error: squad not declared"
        if employee_name not in employee_array:
            raise "Error: employee not declared"
        squads_table[squad_name]["employees"].append(employee_name)
        
        if VERBOSE_MODE:
            print(f"Added employee '{employee_name}' to squad '{squad_name}'")

class RemoveVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        squad_name = self.children[0]
        employee_name = self.children[1]

        if squad_name not in squads_table.keys():
            raise "Error: squad not declared"
        if employee_name not in employee_array:
            raise "Error: employee not declared"
        squads_table[squad_name]["employees"].remove(employee_name)

        if VERBOSE_MODE:
            print(f"Removed employee '{employee_name}' from squad '{squad_name}'")

class CreateTaskVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        task_name = self.children[0]
        employee_name = self.children[1]
        squad_name = self.children[2]
        task_status = self.children[3]

        if employee_name not in employee_array:
            raise "Error: employee not declared"
        if employee_name not in squads_table[squad_name]["employees"]:
            raise "Error: employee not in squad"
        if task_status not in ["TODO", "DOING", "DONE"]:
            raise "Error: invalid task status"
        if task_name in squads_table[squad_name]["tasks"].keys():
            raise "Error: task already declared"

        squads_table[squad_name]["tasks"][task_name] = {"status": task_status, "owner": employee_name, "name": task_name}
        
        if VERBOSE_MODE:
            print(f"Created task '{task_name}' for employee '{employee_name}' in squad '{squad_name}' with status '{task_status}'")

class UpdateTaskVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        task_name = self.children[0]
        employee_name = self.children[1]
        squad_name = self.children[2]
        task_status = self.children[3]

        if employee_name not in employee_array:
            raise "Error: employee not declared"
        if employee_name not in squads_table[squad_name]["employees"]:
            raise "Error: employee not in squad"
        if task_status not in ["TODO", "DOING", "DONE"]:
            raise "Error: invalid task status"
        if task_name not in squads_table[squad_name]["tasks"].keys():
            raise "Error: task not declared"
        
        squads_table[squad_name]["tasks"][task_name] = {"status": task_status, "owner": employee_name, "name": task_name}
        
        if VERBOSE_MODE:
            print(f"Updated task '{task_name}' from '{employee_name}' in squad '{squad_name}' to status '{task_status}'")

class PropVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self):
        temp_var_local = self.children[0]
        prop = self.children[1]

        if temp_var_local != temp_var:
            raise "Error: variable not declared"
        if prop not in ["status", "owner", "name"]:
            raise "Error: invalid property"
        
        return (current_task[prop], "string")