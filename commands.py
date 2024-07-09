from control import *
import matplotlib.pyplot as plt
from colors import *
variables = {}

class Commands:
    def __init__(self):
        self.commands = {"ss": self.stateSpace,
                        "tf": self.transferFunction,
                        "printVar": self.printVar,
                        "step": self.stepResponse,
                        "rlocus": self.rootLocus,
                        "bode": self.bodePlot,
                        "nyquist": self.nyquistPlot,
                        "stepinfo": self.stepInfo,
                        "ufeedback": self.unityFeedback,
                        "bye": self.bye,
                        "allCommands": self.allCommands,
                        "sv": self.storeVariable}

    def transferFunction(self, args):
        if len(args) != 3:
            print("Number Of Arguments Not Right!")
            return
        num = args[0].split(',')
        den = args[1].split(',')

        if ('' in num) or ('' in den):
            print("Format Error!")
            return

        for i in range(len(num)):
            num[i] = float(num[i])

        for i in range(len(den)):
            den[i] = float(den[i])

        variables.update({args[2]:tf(num,den,name = args[2])})

    def stateSpace(self, args):
        if len(args) != 5:
            print("Number Of Arguments Not Right!")
            return
        
        '''Splitting string to get A, B, C, D matrices'''
        aMat = self.splitMat(args[0])
        bMat = self.splitMat(args[1])
        cMat = self.splitMat(args[2])
        dMat = self.splitMat(args[3])
        try:
            s = ss(aMat,bMat,cMat,dMat)
        except ValueError:
            print("Error! Matrices Not Given Right")
            return
        variables.update({args[4]:s})

    
    def splitMat(self, st):
        mat = st.split(';')

        for i in range(len(mat)):
            b = mat[i].split(',')
            for c in range(len(b)):
                b[c] = float(b[c])
            mat[i] = b
        return mat
                

    def printVar(self, args):
        if len(args) != 1:
            print("Number Of Arguments Not Right!")
            return
        if (args[0] == '*'):
            print(variables)
            return
        try:
            print(variables[args[0]])
        except:
            print("Error! Probably Variable Does not Exist")

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

    def storeVariable(self, args):
        if len(args) != 2:
            print("Number Of Arguments Not Right!")
            return 
        try:
            var = float(args[0])
        except:
            print(bcolors.FAIL + bcolors.BOLD +"Type Error!"+bcolors.ENDC)
            return

        variables.update({args[1]:var})

    def bye(self, args):
        if len(args) != 0:
            print("Number Of Arguments Not Right!")
            return
        print('Bye!')
        exit()

    def allCommands(self, args):
        if len(args) != 0:
            print("Number Of Arguments Not Right!")
            return
        
        print()
        print(bcolors.OKGREEN + bcolors.UNDERLINE +"Available Commands" + bcolors.ENDC)
        print()
        keys = list(self.commands.keys())
        for c in keys:
            print("---> "+bcolors.BOLD + c + bcolors.ENDC)


    def preprocessor(self, args):
        if args[0] != 'sv':
            for i in range(1, len(args[1:])):
                if args[i].isalpha():
                    try:
                        args[i] = str(variables[args[i]])
                    except:
                        print(bcolors.FAIL + bcolors.BOLD + "Error! Probably Variable '" + args[i] + "' Does not Exist" + bcolors.ENDC)
                        return
        self.commands[args[0]](args[1:])

                    