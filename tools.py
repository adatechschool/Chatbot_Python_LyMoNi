import operator

commands = ['/math', '/help']

def math(*args):

    str = args[0].split()

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '**': operator.pow,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
    }

    oper = str[1]
    nmbr1 = float(str[0])
    nmbr2 = float(str[2])
    result = ops[oper](nmbr1, nmbr2)
    # print(type(result))
    return result

    # print(str)
    # return str[]

def help(*args):
    print('hey')
    return 'banana'

def tools(tool):

    switcher = {
        '/math':  math,
        '/help': help,
    }
    output = switcher[tool[0]](tool[1]) #, 2
    try:
        output = str(output)
    except:
        pass
    return output
