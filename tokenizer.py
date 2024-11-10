
# Define keywords and symbols for the language (example list, can be extended)

import sys

# Define keywords and symbols for the language (example list, can be extended)
KEYWORDS = {"class", "constructor", "function", "method", "field", "static", "var", "int", "char", "boolean", "void", "true", "false", "null", "this", "let", "do", "if", "else", "while", "return"}
SYMBOLS = {"{", "}", "(", ")", "[", "]", "+", "-", ".", ",", "*", "/", "&", "|", "<", ">", "~", ";", "="}

# List to store tokens
tokens = []

class Token:
    def __init__(self, line_no: int, column_no: int, token_type: str, token_value: str):
        self.lineNo = line_no
        self.columnNo = column_no
        self.tokenType = token_type
        self.tokenValue = token_value

    def __str__(self):
        return f"<{self.tokenType}> {self.tokenValue} </{self.tokenType}>"

def add_token(line_no, column_no, token_type, token_value):
    """Helper function to create a Token and add it to the tokens list."""
    tokens.append(Token(line_no, column_no, token_type, token_value))

def un_string_line(line, line_no):
    i = 0
    while i < len(line):
        if line[i] == "\"":  # Detect a string constant
            opening_quote_index = i
            i += 1
            while i < len(line) and line[i] != "\"":
                i += 1
            if i < len(line):
                closing_quote_index = i
                string_constant = line[opening_quote_index:closing_quote_index + 1]
                add_token(line_no, opening_quote_index, "stringConstant", string_constant)
                line = line[:opening_quote_index] + " " * (closing_quote_index - opening_quote_index + 1) + line[closing_quote_index + 1:]
            else:
                raise ValueError("Unmatched quote in string constant")
        i += 1
    
    i = 0
    while i < len(line):
        if line[i].isspace():
            i += 1
            continue

        elif line[i].isdigit():  # Detect integer constants
            start_index = i
            while i < len(line) and line[i].isdigit():
                i += 1
            integer_constant = line[start_index:i]
            add_token(line_no, start_index, "integerConstant", integer_constant)

        elif line[i].isalpha() or line[i] == "_":  # Detect identifiers and keywords
            start_index = i
            while i < len(line) and (line[i].isalnum() or line[i] == "_"):
                i += 1
            identifier = line[start_index:i]
            if identifier in KEYWORDS:
                add_token(line_no, start_index, "keyword", identifier)
            else:
                add_token(line_no, start_index, "identifier", identifier)

        elif line[i] in SYMBOLS:  # Detect symbols
            symbol = line[i]
            add_token(line_no, i, "symbol", symbol)
            i += 1

        else:
            i += 1

def write_tokens_to_xml(filename="tokenizedfile.xml"):
    with open(filename, "w") as file:
        file.write("<tokens>\n")
        for token in tokens:
            file.write(f"  {token}\n")
        file.write("</tokens>\n")

def main():
    # Check if the filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python tokenizer.py <filename>")
        sys.exit(1)

    input_filename = sys.argv[1]

    try:
        # Open the input file and process each line
        with open(input_filename, "r") as file_input:
            code_lines = file_input.readlines()
            for line_no, line in enumerate(code_lines, start=1):
                un_string_line(line, line_no)
        
        # Write the tokens to the XML file
        write_tokens_to_xml()

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()




#Tasks today
#Parser


class ParsingStructure: # The base class for all structures that include token objects
        pass

class ProgramStructure(ParsingStructure): # ParsingStructures of Program Structures
        pass # class, classVarDec, type, subroutineDec, parameterList, subroutineBody, varDec, className, subroutineName, varName

class Statement(ParsingStructure):
    pass

class ClassParse(ProgramStructure):
    def __init__(self, tokens: list):
        pass

class ClassVarDecParse(ProgramStructure):
    def __init__(self, tokens: list):
        pass

class TypeParse(ProgramStructure):
    def __init__(self, tokens: list):
        pass

class SubroutineDecParse(ProgramStructure):
    def __init__(self, tokens: list):
        pass

class ParameterListParse(ProgramStructure):
    def __init__(self, tokens: list):
        pass

class SubroutineBodyParse(ProgramStructure):
    def __init__(self, tokens: list):
        pass

class VarDecParse(ProgramStructure):
    def __init__(self, tokens: list):
        pass

class ClassNameParse(ProgramStructure):
    def __init__(self, identifier: Token):
        if identifier.tokenType != "identifier":
            raise ValueError("className's identifier must be an identifier")
        self.identifier = identifier
    def __str__(self):
        return f"""<className>
    {str(self.identifier)}
</className>"""

class SubroutineNameParse(ProgramStructure):
    def __init__(self, identifier: Token):
        if identifier.tokenType != "identifier":
            raise ValueError("subroutineName's identifier must be an identifier")
        self.identifier = identifier
    def __str__(self):
        return f"""<subroutineName>
    {str(self.identifier)}
</subroutineName>"""

class VarNameParse(ProgramStructure):
    def __init__(self, identifier: Token):
        if identifier.tokenType != "identifier":
            raise ValueError("varName's identifier must be an identifier")
        self.identifier = identifier
    def __str__(self):
        return f"""<varName>
    {str(self.identifier)}
</varName>"""