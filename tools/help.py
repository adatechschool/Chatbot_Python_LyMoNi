import tools_manage as tls

def man_math():
    man_m = '\nYou can only calculate basic and simple operations.\nEach element has to be separated by a " "\nEx: 1 + 2.'
    man_m += '\nPossible operators are: +, -, **, *, /, %.\nEvery result will return as a float.\n'
    return man_m

def man_weather():
    man_w = '\nJust enter a city name as second parameter.\n'
    return man_w

def help(*args):
    if None in args:
        ret = 'Possible mans are:'
        for i in tls.commands:
            ret += ' "{}"'.format(i)
        ret += '.'
        return ret
    if '/math' in args:
        return man_math()
    if '/weather' in args:
        return man_weather()
