import operator

def math(*args):

    if None in args:
        return 'There was an error.'
    else:
        str = args[0].split()

    if len(str) > 3:
        return 'You can only use 2 values and 1 operator: value operator value.'

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '**': operator.pow,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
    }

    try:
        oper = str[1]
        nmbr1 = float(str[0])
        nmbr2 = float(str[2])
        result = ps[oper](nmbr1, nmbr2)
    except Exception as e:
        print(e)
        result = 'There was an error.'

    return result
