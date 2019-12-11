import tools.math as mth
import tools.help as hlp
import tools.weather as wth

math = mth.math()
help = hlp.help()

commands = ['/math', '/help']

def tools(tool):

    switcher = {
        '/math': math,
        '/help': help,
        '/weather': weather,
    }
    output = switcher[tool[0]](tool[1])
    try:
        output = str(output)
    except:
        pass
    return output
