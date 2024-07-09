from commands import Commands
from colors import *

class Interaction:
    def __init__(self):
        st = '''   _____               _                _    _____              _                          _______             _ 
  / ____|             | |              | |  / ____|            | |                        |__   __|           | |
 | |      ___   _ __  | |_  _ __  ___  | | | (___   _   _  ___ | |_  ___  _ __ ___   ___     | |  ___    ___  | |
 | |     / _ \ | '_ \ | __|| '__|/ _ \ | |  \___ \ | | | |/ __|| __|/ _ \| '_ ` _ \ / __|    | | / _ \  / _ \ | |
 | |____| (_) || | | || |_ | |  | (_) || |  ____) || |_| |\__ \| |_|  __/| | | | | |\__ \    | || (_) || (_) || |
  \_____|\___/ |_| |_| \__||_|   \___/ |_| |_____/  \__, ||___/ \__|\___||_| |_| |_||___/    |_| \___/  \___/ |_|
                                                     __/ |                                                       
                                                    |___/                                                        '''
        print(bcolors.HEADER + bcolors.BOLD + st + bcolors.ENDC)
        self.printAvailCommands()
    
    def printAvailCommands(self):
        Commands().allCommands([])
