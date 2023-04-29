# Write your solution here
import string

def get_location(program: list):
    locations = {}
    for idx in range(len(program)):
        if program[idx].endswith(':'):
            locations[program[idx][:-1]] = idx

    return locations

def check_condition(commands: list, variables: dict):
    val1 = variables[commands[0]] if commands[0] in variables else int(commands[0]) 
    val2 = variables[commands[-1]] if commands[-1] in variables else int(commands[-1]) 

    match commands[1]:
        case '==':
            return val1 == val2
        case '!=':
            return val1 != val2
        case '<':
            return val1 < val2
        case '<=':
            return val1 <= val2
        case '>':
            return val1 > val2
        case '>=':
            return val1 >= val2
        case _:
            return False

    return False

def run(program: list):
    upper_letters = [i for i in string.ascii_uppercase]
    variables = dict.fromkeys(upper_letters, 0)
    locations = get_location(program)
    ret = []

    idx = 0
    size = len(program)
    while idx < size:
        commands = program[idx].split(' ')
        match commands[0]:
            case 'PRINT':
                ret.append(variables[commands[1]] if commands[1] in variables else int(commands[1]))
            case 'ADD':
                var = commands[1]
                value = commands[2]
                actual_value = variables[value] if value in variables else int(value)
                variables[var] += actual_value
            case 'MOV':
                var = commands[1]
                value = commands[2]
                actual_value = variables[value] if value in variables else int(value)
                variables[var] = actual_value
            case 'SUB':
                var = commands[1]
                value = commands[2]
                actual_value = variables[value] if value in variables else int(value)
                variables[var] -= actual_value
            case 'MUL':
                var = commands[1]
                value = commands[2]
                actual_value = variables[value] if value in variables else int(value)
                variables[var] *= actual_value
            case 'JUMP':
                loc = commands[-1]
                idx = locations[loc]
                continue
            case 'IF':
                if check_condition(commands[1:-2], variables):
                    idx = locations[commands[-1]]
                    continue
            case 'END':
                break
            case _: # for location
                pass
        idx += 1
    return ret

if __name__ == '__main__':
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
