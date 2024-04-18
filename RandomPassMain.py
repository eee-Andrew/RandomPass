import string

def moreinfo():
    import random  # Import random module within the function
    length = input("How long do you want your password: ")
    length = int(length)
    print("Ok, you typed:", length, "Exiting.")
    
    password = ''
    for _ in range(length):
        password = chosen_function(password)
    print("Generated Password:", password)


def addchar(password):
    import random  # Import random module within the function
    return password + random.choice(string.ascii_letters)

def addnum(password):
    import random  # Import random module within the function
    return password + str(random.randint(1, 10))

def alternate_functions(password):
    import random  # Import random module within the function
    return random.choice([addchar, addnum])(password)

chosen_function = alternate_functions


def greeting():
    print("Do you want a new Password? Press Y for YES and N for NO")
    yesorno = input("Type here Y/N: ")
    
    if yesorno.upper() == 'Y':
        print("Ok, you typed 'Y'! Please give me more information.")
        moreinfo()
    elif yesorno.upper() == 'N':
        print("Ok, you typed 'N'. Exiting.")
        # You may want to add an exit or return statement here if needed
    else:
        print("Invalid input. Please type 'Y' for YES or 'N' for NO.")
        greeting()

greeting()
