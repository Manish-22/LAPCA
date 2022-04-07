
import ply.yacc as yacc
from C_Lex import tokens
from C_Lex import user_defined_types
import copy
import re  # !/usr/bin/env python3


def p_ST(p):
    ''' ST  : S  '''


def p_S(p):
    ''' S  : TYPE  '''


def p_TYPE(p):
    ''' TYPE  : INT 
    | FLOAT 
    | CHAR 
    | BOOL 
    | DOUBLE   '''


def p_error(p):
    if p:
        print("Syntax error at token", p)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()

input_prog = []
while(True):
    try:
        next_line = input()
    except EOFError:
        #print("Going to Parse Input now!")
        break
    else:
        input_prog.append(next_line)

input_prog_str = "\n".join(input_prog)
result = parser.parse(input_prog_str)
