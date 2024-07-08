import interaction as i
import commander as c
import readline

history = []

def main():
    i.Interaction()
    com = c.Commander()

    while True:
        try:
            command = input(">> ")
            if command != "":
                history.append(command)
                com.getCommand(command)
        except KeyboardInterrupt:
            print("\nBye!")
            exit()

if __name__ == "__main__":
    main()
