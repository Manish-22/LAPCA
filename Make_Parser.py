import sys


def write_file_at(at_state, string):
    funcname = "def p_"+at_state+"(p):\n"
    for i in range(len(file_lines)):
        if file_lines[i] == funcname:
            x = i
            break
    while(file_lines[x].strip() != "# ADD" and x < len(file_lines)):
        x += 1
    # print("".join(string))
    file_lines.insert(x+1, "".join(string))


file_handle = open("C_Parser.py", "rt")
file_lines = file_handle.readlines()
file_handle.close()

formal = open(sys.argv[1], "rt")
lines = formal.readlines()
formal.close()

i = 0
code = []
while(i < len(lines)):
    words = lines[i]
    if(not words):
        continue
    if(words[0:5] != "STATE"):
        i += 1
        break
    i += 1
    cur_state = words[6:-1]
    while(i < len(lines)):
        words = lines[i]
        if(words == "END_STATE\n"):
            break
        if cur_state == "before_parse_main" or cur_state == "after_parse_main":
            code.append(words[4:])
        else:
            code.append(words)
        i += 1
    write_file_at(cur_state, code)

file_handle_new = open("C_Parser_new.py", "wt")
file_handle_new.writelines(file_lines)
file_handle_new.close()
