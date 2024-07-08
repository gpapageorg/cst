from control import *

import matplotlib.pyplot as plt
variables = {}

class Commands:
    def __init__(self):
        self.commands = {"tf": self.transferFunction,
                        "printVar": self.printVar,
                        "step": self.stepResponse,
                        "rlocus": self.rootLocus,
                        "bode": self.bodePlot,
                        "nyquist": self.nyquistPlot,
                        "stepinfo": self.stepInfo,
                        "ufeedback": self.unityFeedback}

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

        variables.update({args[2]:tf(num,den,name = args[2])})

    def printVar(self, args):
        if len(args) != 1:
            print("Number Of Arguments Not Right!")
            return
        if (args[0] == '*'):
            print(variables)
            return
        print(variables[args[0]])

    def stepResponse(self, args):
        if len(args) != 1 and args[1] != 't':
            print("Number Of Arguments Not Right!")
            return
        if len(args) == 2 and args[1] == 't':
            plt.figure()


        plt.ion()
        T, yout = step_response(variables[args[0]])

        plt.plot(T,yout, label = args[0])
        plt.grid(True)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()

    def rootLocus(self,args):
        if len(args) >= 2:
            print("Number Of Arguments Not Right!")
            return
        
        plt.ion()
        rlocus(variables[args[0]])
        plt.show()
    
    def bodePlot(self,args):
        if len(args) != 1 and args[1] != 't':
            print("Number Of Arguments Not Right!")
            return
        
        if len(args) == 2 and args[1] == 't':
            plt.figure()

        plt.ion()
        bode_plot(variables[args[0]], title="Bode Plot for " + args[0])
        plt.show()

    def nyquistPlot(self, args):
        if len(args) != 1:
            print("Number Of Arguments Not Right!")
            return
        nyquist(variables[args[0]])
        plt.show()
    
    def unityFeedback(self, args):
        if len(args) != 2:
            print("Number Of Arguments Not Right!")
            return
        tmp = feedback(variables[args[0]],1)
        variables.update({args[1]:tmp})

        

    def stepInfo(self, args):
        if len(args) != 1:
            print("Number Of Arguments Not Right!")
            return
        info = step_info(variables[args[0]])

        print()

        for k in info:
            print(k + ": {:.3f}".format(info[k]))

    