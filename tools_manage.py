import tools.math as mth
import tools.help as hlp
import tools.weather as wth

commands = ['/help', '/math', '/weather']

def tools(tool):

    switcher = {
        '/math': mth.math,
        '/help': hlp.help,
        '/weather': wth.weather,
    }

    if len(tool) == 1:
        x = None
    else:
        x = tool[1]

    output = switcher[tool[0]](x)

    try:
        output = str(output)
    except:
        pass
    return output
