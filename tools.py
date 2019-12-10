commands = ['/math']

def math(str):
    print(str)
    return str

def tools(tool):

    tool = tool.split(' ', 2)
    switcher = {
        '/math':  math,
    }

    try:
        switcher[tool[0]](tool[1]) #, 'nothing'
    except:
        pass

    print(str)
