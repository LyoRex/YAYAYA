import sys

valid_commands = ["YA", "A", "YAYA", "AYA", "YAYAYA", "AYAYA", "??", "!!"]

def run_code(filename: str):
    in_str = ""
    with open(filename, "r") as f:
        in_str = f.read()
    parse(in_str)

def parse(inp: str):
    stripped_inp = ""
    for line in inp:
        stripped_inp += line.strip()

    commands = stripped_inp.split("YAH")
    commands = [command.strip() for command in commands if command.strip() in valid_commands]

    data = [0 for _ in range(255)]
    pointer = 0
    code_ptr = 0
    bracket_dict = get_matching_brackets(commands)

    while(code_ptr < len(commands)):
        c = commands[code_ptr]

        if(c == "YA"):
            pointer += 1
        elif(c == "A"):
            pointer -= 1
        elif(c == "YAYA"):
            data[pointer] += 1
            if data[pointer] > 255:
                data[pointer] = 0
        elif(c == "AYA"):
            data[pointer] -= 1
            if data[pointer] < 0:
                data[pointer] = 255
        elif(c == "YAYAYA"):
            print(chr(data[pointer]), end="")
        elif(c == "AYAYA"):
            r = sys.stdin.read(1)
            data[pointer] = ord(r)
        elif(c == "??"):
            if data[pointer] == 0: 
                code_ptr = bracket_dict[code_ptr]
        elif(c == "!!"):
            if data[pointer] != 0: 
                code_ptr = bracket_dict[code_ptr]

        code_ptr += 1

def get_matching_brackets(code):
    starts = []
    bracket_dict = {}

    for idx in range(len(code)):
        if code[idx] == "??": 
            starts.append(idx)
        if code[idx] == "!!":
            start = starts.pop()
            bracket_dict[start] = idx
            bracket_dict[idx] = start
    return bracket_dict

def main():
    if len(sys.argv) == 2:
        run_code(sys.argv[1])

if __name__ == "__main__":
    main()