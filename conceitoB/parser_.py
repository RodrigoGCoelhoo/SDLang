from tokenizer import *
from nodes import *

## Preprocessing ##
class PrePro:
    def filter(self, initial_content):
        
        ## Replace tabs
        initial_content = initial_content.replace("\t", "")

        filtered_block = []
        stmts = initial_content.split("\n")
        for stmt in stmts:
            if stmt == "":
                continue
            if stmt[0:2] != "//":
                filtered_block.append(stmt)
                filtered_block.append("\n")

        return "".join(filtered_block)
    
class Parser:

    def parse_relational_expression(tokenizer):    
        c1 = Parser.parse_expression(tokenizer)
        if tokenizer.next.type == "EQUAL":
            op = tokenizer.next.type
            tokenizer.select_next()
            
            c2 = Parser.parse_expression(tokenizer)
            if c2 == None:
                raise "Error: second element of comparison invalid"
            c1 = BinOp(op, [c1, c2])
        
        if tokenizer.next.type == "GREATER_THAN":
            op = tokenizer.next.type
            tokenizer.select_next()
            
            c2 = Parser.parse_expression(tokenizer)
            if c2 == None:
                raise "Error: second element of comparison invalid"
            c1 = BinOp(op, [c1, c2])
        
        if tokenizer.next.type == "LESS_THAN":
            op = tokenizer.next.type
            tokenizer.select_next()
            
            c2 = Parser.parse_expression(tokenizer)
            if c2 == None:
                raise "Error: second element of comparison invalid"
            c1 = BinOp(op, [c1, c2])
        
        return c1

    def parse_bool_term(tokenizer):
        c1 = Parser.parse_relational_expression(tokenizer)
        if tokenizer.next.type == "AND":
            op = tokenizer.next.type
            tokenizer.select_next()
            
            c2 = Parser.parse_relational_expression(tokenizer)
            c1 = BinOp(op, [c1, c2])
            if c2 == None:
                raise "Error: second element of comparison invalid"
        
        return c1

    def parse_bool_expression(tokenizer):
        c1 = Parser.parse_bool_term(tokenizer)
        if tokenizer.next.type == "OR":
            op = tokenizer.next.type
            tokenizer.select_next()
            
            c2 = Parser.parse_bool_term(tokenizer)
            c1 = BinOp(op, [c1, c2])
            if c2 == None:
                raise "Error: second element of comparison invalid"
        
        return c1

    def parse_factor(tokenizer):
        if tokenizer.next.type == "INT":
            v = tokenizer.next.value
            tokenizer.select_next()
            return IntVal(v, [])
    
        if tokenizer.next.type == "IDEN":
            v = tokenizer.next.value
            tokenizer.select_next()
            if tokenizer.next.type == "PROP":
                tokenizer.select_next()
                if tokenizer.next.type == "IDEN":
                    v2 = tokenizer.next.value
                    tokenizer.select_next()
                    return PropVal(tokenizer.next.type, [v, v2])
                else:
                    raise "Error: no identifier after '.'"
            return IdenVal(v, [])
        
        elif tokenizer.next.type == "PLUS":
            tokenizer.select_next()
            resultado = Parser.parse_factor(tokenizer)
            return UnOp("PLUS", [resultado])
        
        elif tokenizer.next.type == "MINUS":
            tokenizer.select_next()
            resultado = Parser.parse_factor(tokenizer)
            return UnOp("MINUS", [resultado])

        elif tokenizer.next.type == "NOT":
            tokenizer.select_next()
            resultado = Parser.parse_factor(tokenizer)
            return UnOp("NOT", [resultado])
        
        elif tokenizer.next.type == "OPEN_P":
            tokenizer.select_next()
            resultado = Parser.parse_bool_expression(tokenizer)
            if tokenizer.next.type == "CLOSE_P":
                # v = resultado.Evaluate()
                tokenizer.select_next()
                return resultado
            raise "Error: no ')'"
        
        elif tokenizer.next.type == "SCAN":
            tokenizer.select_next()
            if tokenizer.next.type == "OPEN_P":
                tokenizer.select_next()
                v = int(input())
                if tokenizer.next.type == "CLOSE_P":
                    tokenizer.select_next()
                    return IntVal(v, [])
                else:
                    raise "Error: no ')' after 'Scanln'"
                
            else:
                raise "Error: no '(' after 'Scanln'"
        
        elif tokenizer.next.type == "STRING":
            v = tokenizer.next.value
            tokenizer.select_next()
            return StrVal(v, [])

    def parse_term(tokenizer):
        c1 = Parser.parse_factor(tokenizer)
        while tokenizer.next.type in ["MULT", "DIV"]:
            op = tokenizer.next.type
            tokenizer.select_next()
            
            c2 = Parser.parse_factor(tokenizer)
            c1 = BinOp(op, [c1, c2])

        return c1
        
    def parse_expression(tokenizer):
        c1 = Parser.parse_term(tokenizer)
        while tokenizer.next.type in ["PLUS", "MINUS"]:
            op = tokenizer.next.type
            tokenizer.select_next()

            c2 = Parser.parse_term(tokenizer)
            c1 = BinOp(op, [c1, c2])
        return c1
    
    # def parse_assign(tokenizer):
    #     print("REMOVER PARSE ASSIGN")
        # c1 = IdenVal(tokenizer.next.value, [])
        # tokenizer.select_next()
        # if tokenizer.next.type != "ASSIGN":
        #     raise "Error: no assigment"
        # tokenizer.select_next()
        # c2 = Parser.parse_bool_expression(tokenizer)
        # return AssignVal("IDEN", [c1, c2])
    
    def parse_statement(tokenizer):
        # print(tokenizer.next.type, tokenizer.next.value)
        if tokenizer.next.type == "STMT":
            tokenizer.select_next()
            return NoOp(0, [])
        
        elif tokenizer.next.type == "PRINT":
            tokenizer.select_next()
            if tokenizer.next.type != "OPEN_P":
                raise "Error: no ("
            tokenizer.select_next()
            c1 = Parser.parse_bool_expression(tokenizer)
            if tokenizer.next.type != "CLOSE_P":
                raise "Error: no )"
            tokenizer.select_next()
            return PrintVal("PRINT", [c1])
        
        elif tokenizer.next.type == "SQUAD":
            tokenizer.select_next()
            if tokenizer.next.type != "IDEN":
                raise "Error: no identifier for squad"
            c1 = SquadVal("SQUAD", [tokenizer.next.value])
            tokenizer.select_next()
            return c1

        elif tokenizer.next.type == "EMPLOYEE":
            tokenizer.select_next()
            if tokenizer.next.type != "IDEN":
                raise "Error: no identifier for employee"
            c1 = EmployeeVal("EMPLOYEE", [tokenizer.next.value])
            tokenizer.select_next()
            return c1
        
        elif tokenizer.next.type == "IDEN":
            iden1 = tokenizer.next.value
            tokenizer.select_next()
            if tokenizer.next.type != "ADD" and tokenizer.next.type != "REMOVE":
                raise "Error: no add or remove after identifier"
            flag = tokenizer.next.type
            tokenizer.select_next()
            if tokenizer.next.type != "IDEN":
                raise "Error: no identifier after add or remove"
            iden2 = tokenizer.next.value
            tokenizer.select_next()
            if flag == "ADD":
                return AddVal("IDEN", [iden1, iden2])
            else:
                return RemoveVal("IDEN", [iden1, iden2])
            
        elif tokenizer.next.type == "TASK":
            tokenizer.select_next()
            if tokenizer.next.type != "STRING":
                raise "Error: no string after task"
            task_name = tokenizer.next.value

            tokenizer.select_next()
            if tokenizer.next.type != "TO":
                raise "Error: no to after string"
            
            tokenizer.select_next()
            if tokenizer.next.type != "IDEN":
                raise "Error: no identifier after to"
            employee = tokenizer.next.value

            tokenizer.select_next()
            if tokenizer.next.type != "ON":
                raise "Error: no on after identifier"
            
            tokenizer.select_next()
            if tokenizer.next.type != "IDEN":
                raise "Error: no identifier after on"
            squad_name = tokenizer.next.value

            tokenizer.select_next()
            if tokenizer.next.type != "IS":
                raise "Error: no is after identifier"
            
            tokenizer.select_next()
            if tokenizer.next.type != "STRING":
                raise "Error: no string after is"
            task_status = tokenizer.next.value

            tokenizer.select_next()
            return CreateTaskVal("NEW_TASK", [task_name, employee, squad_name, task_status])
        
        elif tokenizer.next.type == "SET":
            tokenizer.select_next()
            if tokenizer.next.type != "STRING":
                raise "Error: no string after task"
            task_name = tokenizer.next.value
            
            tokenizer.select_next()
            if tokenizer.next.type != "FROM":
                raise "Error: no from after string"
            
            tokenizer.select_next()
            if tokenizer.next.type != "IDEN":
                raise "Error: no identifier after from"
            employee = tokenizer.next.value

            tokenizer.select_next()
            if tokenizer.next.type != "ON":
                raise "Error: no on after identifier"
            
            tokenizer.select_next()
            if tokenizer.next.type != "IDEN":
                raise "Error: no identifier after on"
            squad_name = tokenizer.next.value

            tokenizer.select_next()
            if tokenizer.next.type != "TO":
                raise "Error: no to after identifier"
            tokenizer.select_next()
            if tokenizer.next.type != "STRING":
                raise "Error: no string after to"
            task_status = tokenizer.next.value
            tokenizer.select_next()
            return UpdateTaskVal("NEW_TASK", [task_name, employee, squad_name, task_status])
                    
        elif tokenizer.next.type == "IF":
            tokenizer.select_next()
            condition = Parser.parse_bool_expression(tokenizer)
            if_block = Parser.parse_block(tokenizer)

            tokenizer.select_next()

            if tokenizer.next.type == "ELSE":
                tokenizer.select_next()
                else_block = Parser.parse_block(tokenizer)
                tokenizer.select_next()
                return IfVal("", [condition, if_block, else_block])
            
            tokenizer.select_next()
            return IfVal("", [condition, if_block, None])
        
        elif tokenizer.next.type == "FOR":
            tokenizer.select_next()

            if tokenizer.next.type != "IDEN":
                raise "Error: no identifier after for"
            task_var = tokenizer.next.value
            tokenizer.select_next()

            if tokenizer.next.type != "IN":
                raise "Error: no in after identifier"
            tokenizer.select_next()

            if tokenizer.next.type != "TASKS":
                raise "Error: no tasks after in"
            tokenizer.select_next()

            if tokenizer.next.type != "FROM":
                raise "Error: no from after task"
            tokenizer.select_next()

            if tokenizer.next.type != "IDEN":
                raise "Error: no identifier after from"
            employee = tokenizer.next.value

            tokenizer.select_next()

            block = Parser.parse_block(tokenizer)
            tokenizer.select_next()

            return ForVal("FOR", [task_var, employee, block])
        
        else:
            raise "Error: edge case Parse Statement"
        
    def parse_block(tokenizer):
        if tokenizer.next.type == "OPEN_B":
            tokenizer.select_next()
        else:
            raise "Error: no '{' on if/for"

        if tokenizer.next.type == "STMT":
            tokenizer.select_next()
        else:
            raise "Error: no '\\n' on if/for"
        
        block = BlockVal("BLOCK", [])
        while tokenizer.next.type != "CLOSE_B":
            c = Parser.parse_statement(tokenizer)
            block.children.append(c)

        return block

    def parse_program(tokenizer):
        block = BlockVal("BLOCK", [])
        if(tokenizer.next.type != "START_SPRINT"):
                raise "Error: no START_SPRINT"
        tokenizer.select_next()
        while tokenizer.next.type != "END_SPRINT":            
            c = Parser.parse_statement(tokenizer)
            block.children.append(c)
        return block
    

    def run(source):

        clean_content = PrePro().filter(source)

        tokenizer = Tokenizer(clean_content, 0, None)
        tokenizer.select_next()

        tree = Parser.parse_program(tokenizer)

        if tokenizer.next.type != "END_SPRINT":
            raise "Error: no END_SPRINT"
        return tree
