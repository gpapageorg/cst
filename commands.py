from control import *
import matplotlib.pyplot as plt
import commandDesc as cD
from colors import *
import multiprocessing

variables = {}
notToBePrepossed = ['sv', 'ufeedback']
toBeMultiprocessed = ['step','bode', 'nyquist','rlocus']
class Commands:
    def __init__(self, gra = 0):
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
        self.gra = gra


    def transferFunction(self, args):
        if len(args) != 3:
            self.gra.update_terminal_log("Number Of Arguments Not Right!\n", "red",True)
            
        num = args[0].split(',')
        den = args[1].split(',')

        if ('' in num) or ('' in den):
            print("Format Error!")
            self.gra.update_terminal_log("Format Error!\n", "red",True)

            return

        for i in range(len(num)):
            num[i] = float(num[i])

        for i in range(len(den)):
            den[i] = float(den[i])

        variables.update({args[2]:tf(num,den,name = args[2])})
        self.gra.update_terminal_log(str(variables[args[2]]), "green")
        
    def stateSpace(self, args):
        if len(args) != 5:
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!\n",'red',True)
            return
        
        '''Splitting string to get A, B, C, D matrices'''
        aMat = self.splitMat(args[0])
        bMat = self.splitMat(args[1])
        cMat = self.splitMat(args[2])
        dMat = self.splitMat(args[3])
        try:
            s = ss(aMat,bMat,cMat,dMat)
        except ValueError:
            # print("Error! Matrices Not Given Right")
            self.gra.update_terminal_log("Error! Matrices Not Given Righ\nt",'red',True)
            return
        variables.update({args[4]:s})
        # self.gra.update_terminal_log("G = ", "green")
        self.gra.update_terminal_log(str(variables[args[4]]), "green")

    
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
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!\n",'red',True)
            return
        if (args[0] == '*'):
            print(variables)
            return
        try:
            print(variables[args[0]])
        except:
            # print("Error! Probably Variable Does not Exist")
            self.gra.update_terminal_log("Error! Probably Variable Does not Exist\n",'red',True)


    def stepResponse(self, args):
        if len(args) != 1 and args[1] != 't':
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!",'red',True)

            return
        if len(args) == 2 and args[1] == 't':
            plt.figure()


        T, yout = step_response(variables[args[0]])
        plt.plot(T,yout, label = args[0])
        plt.grid(True)
        plt.title("Step Response")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.show()


    def rootLocus(self,args):
        if len(args) >= 2:
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!",'red',True)
            
            return
        
        rlocus(variables[args[0]])
        plt.show()
    
    def bodePlot(self,args):
        if len(args) != 1 and args[1] != 't':
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!",'red',True)
            return
       
        if len(args) == 2 and args[1] == 't':
            plt.figure()

        # plt.ion()
        bode_plot(variables[args[0]],dB = True)
        # bode_plot(variables[args[0]], title="Bode` Plot for " + str(args[0]))
        plt.show()

    def nyquistPlot(self, args):
        if len(args) != 1:
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!",'red',True)

            return
        print(args[0])
        nyquist(variables[args[0]])
        plt.show()
    
    def unityFeedback(self, args):
        if len(args) != 2:
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!",'red',True)

            return
    
        if args[0] not in variables.keys():
            # print("Variable " + args[0] + " Not Found!")
            self.gra.update_terminal_log("Variable " + args[0] + " Not Found!",'red',True)

            return
        
        tmp = feedback(variables[args[0]],1)
        variables.update({args[1]:tmp})
        self.gra.update_terminal_log(str(variables[args[1]]), "green")

        

        

    def stepInfo(self, args):
        if len(args) != 1:
            # print("Number Of Arguments Not Right!")
            return
        info = step_info(variables[args[0]])

        print()
        self.gra.update_terminal_log("\n",'white')

        for k in info:
            print(k + ": {:.3f}".format(info[k]))
            self.gra.update_terminal_log(str(k),'white')
            self.gra.update_terminal_log(" : {:.3f}\n".format(info[k]),'white',True)


    def storeVariable(self, args):
        if len(args) != 2:
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!\n",'red',True)

            return 
        try:
            var = float(args[0])
        except:
            print(bcolors.FAIL + bcolors.BOLD +"Type Error!"+bcolors.ENDC)
            return

        variables.update({args[1]:var})

    def bye(self, args):
        if len(args) != 0:
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!",'red',True)

            return
        print('Bye!')
        exit()

    def allCommands(self, args):
        if len(args) != 0:
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!", "red")
            return
        
        # print()
        # print(bcolors.OKGREEN + bcolors.UNDERLINE +"Available Commands" + bcolors.ENDC)
        # print()
        keys = list(cD.desc.keys())
        for c in keys:
            # print("---> "+bcolors.BOLD + c + " >>> ",end=' ')
            # print(bcolors.OKBLUE + cD.desc[c]+ bcolors.ENDC)
            self.gra.update_terminal_log("---> " + c + " ", bold =True)
            self.gra.update_terminal_log(cD.desc[c]+"\n","blue", bold =True)

    def preprocessor(self, arg):
        if arg[0] not in notToBePrepossed:
            for i in range(1, len(arg[1:])):
                if arg[i].isalpha():
                    try:
                        arg[i] = str(variables[arg[i]])
                    except:
                        self.gra.update_terminal_log("Error! Probably Variable '" + arg[i] + "' Does not Exist","red", bold =True)
                        print(bcolors.FAIL + bcolors.BOLD + "Error! Probably Variable '" + arg[i] + "' Does not Exist" + bcolors.ENDC)
                        return

        if (arg[0] in toBeMultiprocessed):
            self.processController(self.commands[arg[0]],arg[1:])
        else:
            self.commands[arg[0]](arg[1:])
        
    def processController(self,func,args):
        p = multiprocessing.Process(target=func , args=(args,))
        p.start()