from control.matlab import *
import matplotlib.pyplot as plt
variables = {}

class Commands:
    def __init__(self):
        self.commands = {"Help": self.Help,
                        "tf": self.transferFunction,
                        "printVar": self.printVar,
                        "step": self.stepResponse,
                        "rlocus": self.rootLocus,
                        "bode": self.bodePlot}

    def transferFunction(self, args):
        if len(args) != 3:
            print("Number Of Arguments Not Right!")
            return
        num = args[0].split(',')
        den = args[1].split(',')

        for i in range(len(num)):
            num[i] = float(num[i])

        for i in range(len(den)):
            den[i] = float(den[i])

        variables.update({args[2]:tf(num,den)})

    def printVar(self, args):
        if len(args) != 1:
            print("Number Of Arguments Not Right!")
            return
        if (args[0] == '*'):
            print(variables)
            return
        print(variables[args[0]])

    def stepResponse(self, args):
        if len(args) != 1:
            print("Number Of Arguments Not Right!")
            return
        yout, T = step(variables[args[0]])

        plt.plot(T,yout)
        plt.grid()
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.show()

    def rootLocus(self,args):
        if len(args) != 1:
            print("Number Of Arguments Not Right!")
            return
        rlocus(variables[args[0]])
        plt.show()
    
    def bodePlot(self,args):
        if len(args) != 1:
            print("Number Of Arguments Not Right!")
            return
        bode(variables[args[0]])
        plt.show()

    def Help(self,args):
        print("Called Help Command",args)
    
c = Commands()
