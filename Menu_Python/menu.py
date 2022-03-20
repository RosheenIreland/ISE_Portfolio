menu_options = {
    1: 'Rock Paper Scissors',

    2: 'Random Story Generator',

    3: 'Text Based Adventure',

    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, "-", menu_options[key] )

def option1():
    print('Handle option \ "Option 1\"')

def option2():
    print('Handle option \ "Option 2\"')

def option3():
    print('Handle option \ "Option 3\"')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try: 
            option = int(input('Enter your choice:'))
        except:
            print('Wrong input. Please enter a number...')
        
        if option == 1. :
            option1()
        elif option == 2.:
            option2()
        elif option == 3. :
            option3()
        elif option == 4. :
            print('Thank You')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

