from control import *
import matplotlib.pyplot as plt
import commandDesc as cD
from colors import *
import multiprocessing
import threading
import subprocess

variables = {}
notToBePrepossed = ['ufeedback']
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
                        "clc": self.clearTerminal,
                        "cvars": self.clearVariables}

    def transferFunction(self, args):
        if len(args) != 3:
            # self.gra.update_terminal_log("Number Of Arguments Not Right!\n", "red",True)
            print(bcolors.FAIL+bcolors.BOLD+"Number Of Arguments Not Right!"+bcolors.ENDC)
            return
        
        num = args[0].split(',')
        den = args[1].split(',')

        if ('' in num) or ('' in den):
            print(bcolors.FAIL + bcolors.BOLD+"Format Error!" + bcolors.ENDC)
            # self.gra.update_terminal_log("Format Error!\n", "red",True)
            return

        for i in range(len(num)):
            num[i] = float(num[i])

        for i in range(len(den)):
            den[i] = float(den[i])

        variables.update({args[2]:tf(num,den,name = args[2])})
        # self.gra.update_terminal_log(str(variables[args[2]]), "green")
        print(bcolors.OKGREEN + str(variables[args[2]]) + bcolors.ENDC)

        
    def stateSpace(self, args):
        if len(args) != 5:
            print(bcolors.FAIL+bcolors.BOLD+"Number Of Arguments Not Right!"+bcolors.ENDC)
            # self.gra.update_terminal_log("Number Of Arguments Not Right!\n",'red',True)
            return
        
        '''Splitting string to get A, B, C, D matrices'''
        aMat = self.splitMat(args[0])
        bMat = self.splitMat(args[1])
        cMat = self.splitMat(args[2])
        dMat = self.splitMat(args[3])
        try:
            s = ss(aMat,bMat,cMat,dMat)
        except ValueError:
            # self.gra.update_terminal_log("Error! Matrices Not Given Righ\nt",'red',True)
            print(bcolors.FAIL + bcolors.BOLD + "Error! Matrices Not Given Right" + bcolors.ENDC)
            
            return
        variables.update({args[4]:s})
        # self.gra.update_terminal_log("G = ", "green")
        # self.gra.update_terminal_log(str(variables[args[4]]), "green")
        print(bcolors.OKGREEN + str(variables[args[4]]) + bcolors.ENDC)
    
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
            print(bcolors.FAIL+bcolors.BOLD+"Number Of Arguments Not Right!"+bcolors.ENDC)
            # self.gra.update_terminal_log("Number Of Arguments Not Right!\n",'red',True)
            return
        
        if (args[0] == '*'):
            # self.gra.update_terminal_log(str(variables),'green')
            # self.gra.update_terminal_log("\n",'red',True)
            try:
                keysToPrint = list(variables.keys())
                keysToPrint.remove('__builtins__')
            except:
                keysToPrint = list(variables.keys())

            print(bcolors.OKGREEN, end='')
            for i in keysToPrint:
                print(i,'-->', variables[i])
            print(bcolors.ENDC, end='')
            # print(variables)
            return
        try:
            print(bcolors.OKGREEN + str(variables[args[0]]) + bcolors.ENDC)
            # self.gra.update_terminal_log(str(variables[args[0]]),'green')
            # self.gra.update_terminal_log("\n",'red',True)

        except:
            print(bcolors.FAIL + bcolors.BOLD + "Error! Probably Variable" + str(args[0]) + "Does not Exist" + bcolors.ENDC)
            # self.gra.update_terminal_log("Error! Probably Variable Does not Exist\n",'red',True)


    def stepResponse(self, args):
        if len(args) != 1 and args[1] != 't':
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!",'red',True)

            return
        if len(args) == 2 and args[1] == 't':
            plt.figure()

        plt.ion()
        try:
            T, yout = step_response(variables[args[0]])
        except Exception as e:
            print(bcolors.FAIL + bcolors.BOLD + "Error! '" + str(e) +"'"+bcolors.ENDC)
            return


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
            #self.gra.update_terminal_log("Number Of Arguments Not Right!",'red',True)
            print(bcolors.FAIL+bcolors.BOLD+"Number Of Arguments Not Right!"+bcolors.ENDC)
            return
       
        if len(args) == 2 and args[1] == 't':
            plt.figure()

        plt.ion()
        try:
            bode_plot(variables[args[0]],dB = True,margins=True,grid= True)
        except Exception as e:
            print(bcolors.FAIL + bcolors.BOLD + "Error! '" + str(e) +"'"+bcolors.ENDC)


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


    def bye(self, args):
        if len(args) != 0:
            # print("Number Of Arguments Not Right!")
            self.gra.update_terminal_log("Number Of Arguments Not Right!",'red',True)

            return
        print('Bye!')
        exit()

    def allCommands(self, args):
        if len(args) != 0:
            print("Number Of Arguments Not Right!")
            # self.gra.update_terminal_log("Number Of Arguments Not Right!", "red")
            return
        
        print()
        print(bcolors.OKGREEN + bcolors.UNDERLINE +"Available Commands" + bcolors.ENDC)
        print()
        keys = list(cD.desc.keys())
        for c in keys:
            print("---> "+bcolors.BOLD + c + " >>> ",end=' ')
            print(bcolors.OKBLUE + cD.desc[c]+ bcolors.ENDC)
            # self.gra.update_terminal_log("---> " + c + " ", bold =True)
            # self.gra.update_terminal_log(cD.desc[c]+"\n","blue", bold =True)

    def clearTerminal(self,args):
        if len(args) != 0:
            # self.gra.update_terminal_log("Number Of Arguments Not Right!\n", "red",True)
            print(bcolors.FAIL+bcolors.BOLD+"Number Of Arguments Not Right!"+bcolors.ENDC)
            return
        try:
            subprocess.call("clear")
        except Exception as e:
            print(bcolors.FAIL + bcolors.BOLD + "Error! '" + str(e) +"'"+bcolors.ENDC)
            return
        
    def clearVariables(self, args):
        if len(args) != 0:
            # self.gra.update_terminal_log("Number Of Arguments Not Right!\n", "red",True)
            print(bcolors.FAIL+bcolors.BOLD+"Number Of Arguments Not Right!"+bcolors.ENDC)
            return
        
        try:
            variables.clear()
            print(bcolors.OKGREEN + "All Variables Cleared" + bcolors.ENDC)

        except Exception as e:
            print(bcolors.FAIL + bcolors.BOLD + "Error! '" + str(e) +"'"+bcolors.ENDC)
            return
        

    def preprocessor(self):
        # if len(arg) == 1 and self.args[0] not in self.commands.keys():
        # print(eval('G',variables))   
        if self.args[0] in self.commands.keys():
            startComma = 0
            endComma = 0
            for i in  range(1,len(self.args) - 1):
                self.args[i] += ',' # adding , for algorithm
                counter = 0
                while True:
                    try:
                        counter +=1
                        k = self.args[i][endComma:].index(',')
                        startComma = endComma
                        endComma += k + 1
                        # value  = eval(self.args[i][startComma:endComma-1],variables)
                        slice = self.args[i][startComma:endComma-1]

                        if slice.isnumeric() is False and slice != '':
                            value = str(self.smartEval(slice,variables))
                            #print(self.args[i], slice, value)
                            self.args[i] = self.args[i].replace(slice, value)
                            endComma = endComma + (len(value) - len(slice))
                            
                    except ValueError:
                        self.args[i] = self.args[i].rstrip(',')

                        # print(self.args[i][endComma:])
                        startComma = 0
                        endComma = 0
                        break

            # print("Final", self.args)
            #if (self.args[0] in toBeMultiprocessed): #Executing Command
            #    self.processController(self.commands[self.args[0]],self.args[1:])
            #else:
            self.commands[self.args[0]](self.args[1:])

        elif (len(self.args) == 1):
            try:
                eqIndex = self.args[0].index('=')
                value = eval(self.args[0][eqIndex+1:],variables)
                variables.update({self.args[0][:eqIndex]:value})
                # self.gra.update_terminal_log(str(self.args[0][:eqIndex]) + ' = ' + str(value) + '\n', "green")
                print(bcolors.OKGREEN+str(self.args[0][:eqIndex]) + ' = ' + str(value)+bcolors.ENDC)
            except ValueError:
                # self.gra.update_terminal_log(str(eval(self.args[0]))+'\n', "green")
                try:
                    print(bcolors.OKGREEN + str(eval(self.args[0],variables) + bcolors.ENDC))
                except:
                    print(bcolors.FAIL+bcolors.BOLD+"Command '" + self.args[0] + "' Not Found!"+bcolors.ENDC)

        else:
            # self.gra.update_terminal_log("Command '" + self.args[0] + "' Not Found!\n", "red", True)
            print("Command '" + self.args[0] + "' Not Found!\n")
              

    def smartEval(self,st, variables):
        'Smarter version of eval() O(n) Complexity'
        if ';' in st:
            print(st)
            strLst = st.split(';')
            fin = ''
            for i in strLst:
                val = str(eval(i,variables))
                fin += val + ';'
            fin = fin.rstrip(';')
            return fin
            
        else:
            fin = eval(st,variables)
            return fin


    def getCommand(self,command):
            self.args = command.split()
            self.preprocessor()
