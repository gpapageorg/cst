import commands as c
class Commander:
    def __init__(self):
        # self.app = app
        self.cList = c.Commands()

    def getCommand(self,command):
        args = command.split()
        # if args[0] in self.cList.commands.keys():
        #     return self.cList.preprocessor(args)
        # else:
        #     print("Command '" + command + "' Not Found!")
        #     self.app.update_terminal_log("Command '" + command + "' Not Found!", "red", True)
        self.cList.preprocessor(args)
