import operator

saved_string = ''

def remove_letter(): #Remove letter from string
       print('-Remove-')
       return

def compare_number(): # Compare numbers to determine the larger
       print('-Compare num-')
       return

def print_string(): # Print the prev stored string
    print(saved_string)
    return

def calculator(): # Basic Calculator (add, sub, ext)
    sign_dict = { '+': operator.add , '-': operator.sub, '*':  operator.mul, '%': operator.div }

    num1 = int(raw_input("Input First Number "))
    sign = str(raw_input("Action: "))
    num2 = int(raw_input("Input Second Number "))

    print(sign_dict[sign](num1, num2))


    return

def accept_and_store(): # Accept and store string
    global saved_string
    saved_string = str(raw_input("Input String: "))
    return

def main(): # menu goes here
    option_list = [
        accept_and_store,
        calculator,
        print_string,
        compare_number,
        remove_letter
    ]
    while(True):
        print("SELECT OPTIONS: ")
        print("1\tAccept and Store")
        print("2\tCalculator")
        print("3\tPrint String")
        print("4\tCompare")
        print("5\tRemove")
        opt_choice = int(raw_input('SELECTION: '))
        opt_choice -= 1
        option_list[opt_choice]()
        
    return 

main()

