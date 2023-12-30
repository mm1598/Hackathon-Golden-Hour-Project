def find_args(CMD_FLAGS: str) -> list:
    lines = None
    new_lines = []

    with open(CMD_FLAGS) as f:
        lines = f.readlines()

    # remove all none comments from CMD_FLAGS
    for line in lines:
        if line[0] != '#': # remove comment lines            
            new_lines.append(line)
    
    return new_lines

def find_arg(args: list, arg: str) -> str:
    pass
