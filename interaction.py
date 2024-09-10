from commands import Commands
from colors import *
import subprocess

class Interaction:
    def __init__(self, gra):
        self.gra = gra
        subprocess.call("clear")
        st = '''
  ____     _          _     
 / ___|___| |    __ _| |__  
| |   / __| |   / _` | '_ \ 
| |___\__ \ |__| (_| | |_) |
 \____|___/_____\__,_|_.__/ 
'''

        self.gra.update_terminal_log("Welcome To CsLab!\n", "green", True)
        self.printAvailCommands()

        # self.gra.update_terminal_log(st,"green")
        # self.printAvailCommands()
    
    def printAvailCommands(self):
        Commands(self.gra).allCommands([])
