from commands import Commands
from colors import *

class Interaction:
    def __init__(self):
        print(bcolors.HEADER + bcolors.BOLD + "Control Systems Tool" + bcolors.ENDC)
        self.printAvailCommands()
    
    def printAvailCommands(self):
        Commands().allCommands([])
