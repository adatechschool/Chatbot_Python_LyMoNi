import operator

commands = ['/math', '/weather']

def math(str):

    str = str.split()

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '**': operator.pow,
        '*': operator.mul,
        '/': operator.truediv,
    }

    oper = str[1]
    nmbr1 = float(str[0])
    nmbr2 = float(str[2])
    result = ops[oper](nmbr1, nmbr2)
    # print(type(result))
    return result

    # print(str)
    # return str[]

def tools(tool):

    switcher = {
        '/math':  math,
    }
    if len(tool) <= 1:
        return "You need at least a list length of 2"
    output = switcher[tool[0]](tool[1])
    try:
        output = str(output)
    except:
        pass
    return output
