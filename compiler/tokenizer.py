import json

# Load reserved words dictionary
with open('./reserved_words.json', 'r') as file:
  reserved_words = json.load(file)

class Token:
    def __init__(self, type:str, value:int):
        self.type = type
        self.value = value

class Tokenizer:
    def __init__(self, source:str, position:int, next: Token):
        self.source = source
        self.position = position
        self.next = next

    def select_next(self):

        if self.position >= len(self.source):
            self.next = Token("EOF", "")
            return

        try:
            element = self.source[self.position]
            while element == " ":
                self.position += 1
                element = self.source[self.position]
        except:
            self.next = Token("EOF", "")
            return
    
        ## Checking for number
        if element.isdigit():
            type_ = "INT"

            resultado = []
            while element.isdigit():
                resultado.append(element)
                self.position += 1
                
                try:
                    element = self.source[self.position]
                except:
                    break
            value = int("".join(resultado))
            self.position -= 1
        
        ## Checking for variable (iden)
        elif element.isalpha():
            type_ = "IDEN"

            resultado = []
            while element.isalpha() or element.isdigit() or element == "_":
                resultado.append(element)
                self.position += 1

                try:
                    element = self.source[self.position]
                except:
                    break

            self.position -= 1
            
            value = str("".join(resultado))

            if value in reserved_words.keys():
                type_ = reserved_words[value]

        ## Checking for doubles (||, && and ==)
        elif element == "=":
            value = element

            self.position += 1
            element = self.source[self.position]
            if element == "=":
                type_ = "EQUAL"
                value = "=="
            else:
                type_ = "ASSIGN"
                self.position -= 1
        
        elif element == "|":
            self.position += 1
            element = self.source[self.position]
            if element == "|":
                type_ = "OR"
                value = element
            else:
                raise "Error: missing '|'"
            
        elif element == "&":
            self.position += 1
            element = self.source[self.position]
            if element == "&":
                type_ = "AND"
                value = element
            else:
                raise "Error: missing '&'"
            
        ## Checking for string
        elif element == '"':
            self.position += 1
            element = self.source[self.position]

            resultado = []
            while element != '"':
                resultado.append(element)
                self.position += 1
            
                try:
                    element = self.source[self.position]
                except:
                    break

                if element == "\n":
                    raise "Error: no ending quotes"
            
            value = str("".join(resultado))

            type_ = "STRING"
        
        ## Checking for singles
        elif element == "+":
            type_ = "PLUS"
            value = element
        elif element == "-":
            type_ = "MINUS"
            value = element
        elif element == "*":
            type_ = "MULT"
            value = element
        elif element == "/":
            type_ = "DIV"
            value = element
        elif element == ".":
            type_ = "PROP"
            value = element
        elif element == "(":
            type_ = "OPEN_P"
            value = element
        elif element == ")":
            type_ = "CLOSE_P"
            value = element
        elif element == "{":
            type_ = "OPEN_B"
            value = element
        elif element == "}":
            type_ = "CLOSE_B"
            value = element
        elif element == "\n":
            type_ = "STMT"
            value = element
        elif element == "!":
            type_ = "NOT"
            value = element
        elif element == ">":
            type_ = "GREATER_THAN"
            value = element
        elif element == "<":
            type_ = "LESS_THAN"
            value = element
        elif element == ";":
            type_ = "SEMI_COLON"
            value = element
        else:
            raise "Error: unidentified symbol"
        # print("type", type_, "value", value)

        self.next = Token(type_, value)
        self.position += 1
