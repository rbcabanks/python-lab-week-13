lst = []

def menu():
    """
    prints the menu
    """
    print()
    print("---------------------------------------")
    print("My App")
    print("---------------------------------------")
    print("[p] prints all names")
    print("[s] sorts all names")
    print("[n] adds new name")
    print("[q] quits")
    print("---------------------------------------")

def print_all():
    print("#            Name")
    print("--           ----")
    for x in range (0,len(lst)):
        print(str(x+1)+"            "+str(lst[x]))

def sort_names():
    lst.sort()
    print("Sorted")

def add_name():
    name=input("Enter student's name: ")
    lst.append(name)

def main():
    """
    main function for the app
    """

    # loop until user types q
    user_quit = False
    while (not user_quit):

        # menu
        menu()

        # get first character of input
        user_input = input("Enter a command:")
        lower_input = user_input.lower()
        first_char = lower_input[0:1]
        print()

        # menu choices, use a switch-like if-elif control structure
        if first_char == 'q':
            print("Thank you for using My App!")
            user_quit = True
        elif first_char == 'p':
            print_all()
        elif first_char == 's':
            sort_names()
        elif first_char == 'n':
            add_name()
        else:
            print("ERROR: no such command")


main()
