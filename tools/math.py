import operator

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
    return result
