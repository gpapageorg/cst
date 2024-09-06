from commands import Commands
from colors import *
import subprocess

class Interaction:
    def __init__(self):
        subprocess.call("clear")
        st = '''
  ____     _          _     
 / ___|___| |    __ _| |__  
| |   / __| |   / _` | '_ \ 
| |___\__ \ |__| (_| | |_) |
 \____|___/_____\__,_|_.__/ 
'''

        print(bcolors.HEADER + bcolors.BOLD + st + bcolors.ENDC)
        self.printAvailCommands()
    
    def printAvailCommands(self):
        Commands().allCommands([])
