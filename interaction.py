import commands 
class Interaction:
    def __init__(self):
        print(bcolors.HEADER +bcolors.BOLD + "Control Systems Tool" + bcolors.ENDC)
        self.printAvailCommands()
    
    def printAvailCommands(self):
        print()
        print(bcolors.OKGREEN + bcolors.UNDERLINE +"Available Commands" + bcolors.ENDC)
        print()
        keys = list(commands.Commands().commands.keys())
        for c in keys:
            print("---> "+bcolors.BOLD + c + bcolors.ENDC)
    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
