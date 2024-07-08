import commands as c
cList = c.Commands()
class Commander:
    def __init__(self):
        pass
    def getCommand(self,command):
        args = command.split()
        
        if args[0] in cList.commands.keys():
            cList.commands[args[0]](args[1:])
        else:
            print("Command '" + command + "' Not Found!")