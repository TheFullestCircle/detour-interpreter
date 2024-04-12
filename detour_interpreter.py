value_dict = {}
pointer_dict = {}

def get_value(cell):
    if cell not in value_dict:
        value_dict[cell] = cell
    return value_dict[cell]

def get_pointer(cell):
    if cell not in pointer_dict:
        pointer_dict[cell] = cell
    return pointer_dict[cell]

def parse(code):
    def parse_indent(code, position):
        j = position + 1
        newcode = []
        while code[j][:2] == "  ":
            newcode.append(code[j][2:])
            j += 1
            if j == len(code):
                break
        parse(newcode)
    for i in range(len(code)):
        line = code[i]
        if line[:2] == "  ":
            0 #code was (supposed to be) parsed by whatever was above it, so do nothing
        elif line[-1] == "+":
            cell = int(line[:-1])
            pointer_dict[cell] = get_pointer(cell) + 1
        elif line[-1] == "-":
            cell = int(line[:-1])
            pointer_dict[cell] = get_pointer(cell) - 1
        elif line[-1] == "v":
            cell = int(line[:-1])
            value_dict[get_pointer(cell)] = int(input())
        elif line[0] == "v":
            cell = int(line[1:])
            value_dict[cell] = int(input())
        elif line[-1] == "^":
            cell = int(line[:-1])
            print(get_value(get_pointer(cell)))
        elif line[0] == "^":
            cell = int(line[1:])
            print(get_value(cell))
        elif line[-1] == ">":
            cell = int(line[:-1])
            value_dict[get_pointer(cell)] = get_value(cell)
        elif line[-1] == "<":
            cell = int(line[:-1])
            value_dict[cell] = get_value(get_pointer(cell))
        elif line[-1] == "?":
            cell = int(line[:-1])
            if get_value(cell) == get_value(get_pointer(cell)):
                parse_indent(code,i)
        elif line[-1] == ":":
            cell = int(line[:-1])
            while get_value(cell) != get_value(get_pointer(cell)):
                parse_indent(code,i)
        else:
            cells = line.split()
            pointer_dict[int(cells[0])] = int(cells[1])

parse([x[:-1] for x in open("detour.txt", "r").readlines()]) #list comprehension to trim newlines
