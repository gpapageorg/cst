import interaction as i
# import commander as c
import commands as c
import readline
from graphics import Graphics

def main():
    i.Interaction()
    # com = c
    com = c.Commands()

    while True:
        try:
            command = input(">> ")
            if command != "":
                com.getCommand(command)
        except KeyboardInterrupt:
            print("\nBye!")
            exit()

if __name__ == "__main__":
    main()
    