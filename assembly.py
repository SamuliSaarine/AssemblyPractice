#Memory locations
acc = 0
a = 0
b = 0
c = 0
d = 0
e = 0

#Program save location
program = []

# English instructions
def print_instructions_en():
    print('\nInstructions:\n')

    print('This program allows you to write and run assembly code\n')

    print('Memory locations: A, B, C, D, E and accumulator (accumulator is the default memory location, which is used for operations)\n')

    print('Operations supported: ADD, SUB, DIV, MUL, JUMP, JUMPZERO, LOAD, STORE, PRINT and INPUT\n')

    print(' * ADD (A,B,C,D,E,<Some integer>): Add the value of operand to accumulator\n')

    print(' * SUB (A,B,C,D,E,<Some integer>): Subtract the value of operand from accumulator\n')

    print(' * DIV (A,B,C,D,E,<Some integer>): Divide the value of accumulator by operand\n')

    print(' * MUL (A,B,C,D,E,<Some integer>): Multiply the value of accumulator by operand\n')

    print(' * JUMP <Some integer>: Jump to the specified line of code\n')

    print(' * JUMPZERO <Some integer>: Jump to the specified line of code if accumulator is zero\n')

    print(' * LOAD (A,B,C,D,E,<Some integer>): Load the value of operand to accumulator\n')

    print(' * STORE (A,B,C,D,E): Store the value of accumulator to the specified memory location\n')

    print(' * PRINT: Print the value of accumulator\n')

    print(' * INPUT: Take input from user and store it in accumulator\n')

    return None

# Finnish instructions
def print_instructions_fi():
    print('\nOhjeet:\n')

    print('Tällä ohjelmalla voit kirjoittaa ja suorittaa ohjelmia Assembly kiellellä\n')

    print('Muistipaikat: A, B, C, D, E ja akkumulaattori (akkumulaattori on oletusmuistipaikka, jota käytetään operaatioissa)\n')

    print('Tuetut operaatiot: ADD, SUB, DIV, MUL, JUMP, JUMPZERO, LOAD, STORE, PRINT ja INPUT\n')

    print(' * ADD (A,B,C,D,E,<Joku kokonaisluku>): Lisää operandin arvo akkumulaattoriin\n')

    print(' * SUB (A,B,C,D,E,<Joku kokonaisluku>): Vähennä operandin arvo akkumulaattorista\n')

    print(' * DIV (A,B,C,D,E,<Joku kokonaisluku>): Jaa akkumulaattorin arvo operandilla\n')

    print(' * MUL (A,B,C,D,E,<Joku kokonaisluku>): Kerro akkumulaattorin arvo operandilla\n')

    print(' * JUMP <Joku kokonaisluku>: Hyppää määritettyyn koodiriviin\n')

    print(' * JUMPZERO <Joku kokonaisluku>: Hyppää määritettyyn koodiriviin, jos akkumulaattorin arvo on nolla\n')

    print(' * LOAD (A,B,C,D,E,<Joku kokonaisluku>): Lataa operandin arvo akkumulaattoriin\n')

    print(' * STORE (A,B,C,D,E): Tallenna akkumulaattorin arvo määritettyyn muistipaikkaan\n')

    print(' * PRINT: Tulosta akkumulaattorin arvo\n')

    print(' * INPUT: Pyydä käyttäjältä syöte ja tallenna se akkumulaattoriin\n')

# Parsing memory location or value
def get_value(operand):
    if operand == 'A':
        return a
    elif operand == 'B':
        return b
    elif operand == 'C':
        return c
    elif operand == 'D':
        return d
    elif operand == 'E':
        return e
    else:
        return int(operand)

# Parsing and executing the line in assembly program
def handle_command(command):
    global acc, a, b, c, d, e

    commandParts = command.split()
    operation = commandParts[0]
    operand = None
    if len(commandParts) > 1:
        operand = commandParts[1]

    match operation:
        case 'ADD':
            acc += get_value(operand)
        case 'SUB':
            acc -= get_value(operand)
        case 'DIV':
            acc /= get_value(operand)
        case 'MUL':
            acc *= get_value(operand)
        case 'JUMP':
            location = get_value(operand)
            return location
        case 'JUMPZERO':
            if acc == 0:
                location = get_value(operand)
                return location
        case 'LOAD':
            acc = get_value(operand)
        case 'STORE':
            match operand:
                case 'A':
                    a = acc
                case 'B':
                    b = acc
                case 'C':
                    c = acc
                case 'D':
                    d = acc
                case 'E':
                    e = acc
        case 'PRINT':
            print(acc)
        case 'INPUT':
            acc = int(input("Enter a integer: "))
        case _:
            print('Invalid command')
            return None

    return None

#Running the whole assembly program
def run_program():
    if len(program) == 0:
        print('No program to run')
        return
    location = 0
    print('\nRUNNING PROGRAM\n')
    while location < len(program):
        response = handle_command(program[location])
        if response is None:
            location += 1
        else:
            if response < 0 or response >= len(program):
                break
            location = response

    print('\nPROGRAM FINISHED\n')

# Handling the choice of the user
def get_choice():
    choice = -1
    while choice == -1:
        try:
            choice = int(input(
                '1. Print instructions\n2. Write new program\n3. Continue existing program\n4. Run program\n0. Exit\n'))
            if (len(program) == 0):
                if choice == 3:
                    print('No program to continue\n')
                    choice = -1
                elif choice == 4:
                    print('No program to run\n')
                    choice = -1
                else:
                    return choice
            else:
                return choice
        except:
            print('Invalid choice')
            choice = -1

# Choosing if using debug mode
def debug_mode():
    try:
        choice = input(
            "\nChoose writing mode:\nD. Execute command when submitted\n<Any key>. Don't execute until ready\n")
        if choice == 'D':
            return True
        return False
    except:
        return False

# Writing the program
def write_program():
    global program
    debugMode = debug_mode()
    print('\nEnter your program:')
    currentLine = len(program)
    while True:
        # Starting program where left, command == 0, if program is empty
        command = input(f"{currentLine}:")
        # Empty line stops writing
        if command == '':
            print('\nStopped writing program\n')
            break

        # In debug mode commands are handled rightaway
        if debugMode:
            response = handle_command(command)
            program.append(command)
            # Handling the jump
            while response is not None and response < len(program):
                print(f"{response}: {program[response]}")
                tempResponse = handle_command(program[response])
                if tempResponse is None:
                    response += 1
                else:
                    response = tempResponse
        else:
            program.append(command)
        currentLine += 1
    return None

# Main program
while True:
    #Resetting values
    acc = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    # Handling choice in the menu
    action = get_choice()
    if action == 0:
        break
    elif action == 1:
        try:
            input_language = int(input(
                'Choose language:\n1. In English\n2. Suomeksi\n'))
            if (input_language == 1):
                print_instructions_en()
            elif (input_language == 2):
                print_instructions_fi()
        except:
            print('Invalid choice')

    elif action == 2:
        program = []
        write_program()
    elif action == 3:
        write_program()
    elif action == 4:
        run_program()
