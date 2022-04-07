k = '''
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
    
input_prog_str = "\\n".join(input_prog) 
result = parser.parse(input_prog_str)'''

st = '''
import ply.yacc as yacc
from C_Lex import tokens
from C_Lex import user_defined_types
import copy
import re'''


f = open("agno_parser.py", "w")
f.write(st)
f1 = open("grammar_cpp.txt", "r")
f.write("#!/usr/bin/env python3\n")
#f.write("print(\"Hello World\")\n")
count = 1
while(1):
    # print(count)
    count += 1
    line = f1.readline()
    flag = 0
    if(line == ""):
        break
    while(1):
        if(len(line)) == 1:
            flag = 1
            break
        line.strip()
        if line[-1] != ";":
            l1 = f1.readline().strip()
            line = line + l1
        else:
            break
    if flag == 1:
        continue

    line = line.replace("\n", "")
    print(line)
    s = "''' "
    prod = ""
    inside = False
    prev = ""
    for i in line:
        if(i == '\''):
            inside = not inside
        if(not inside and i == ';'):
            break
        if i == ':' and not inside:
            s = s + " "+i
        elif i == '|':
            if prev != "'":
                s = s+"\n\t"+i
        else:
            s += i
        prev = i
    s = '\t'+s+" '''\n"
    # print(s)
    # print(line[:line.find(':')-1])
    semi = "def p_"+line[:line.find(':')]+"(p):\n"
    f.write(semi)
    f.write(s)
f.write(k)
f.close()
# exec(open('agno_parser.py').read())
