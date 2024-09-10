import commands as c
class Commander:
    def __init__(self,app):
        self.app = app
        self.cList = c.Commands(app)


    def getCommand(self,command):
        args = command.split()
        if args[0] in self.cList.commands.keys():
            # cList.commands[args[0]](args[1:])
            # self.gra.update_terminal_log(cList.preprocessor(args))
            return self.cList.preprocessor(args)
        else:
            print("Command '" + command + "' Not Found!")