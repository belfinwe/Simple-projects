# Author: Joakim Rønneberg Nilsen
# A JPS Inc. product!
# Original version, intented for >=Python 3.5

# Meant to create fancy headers surrounded by '#'



###############
#             #
#  Functions  #
#             #
###############



#################
#  Big headers  #
#################

def bigHeader():
    x = 0
    print('Enter header text:')
    x = input()
    y = (len(x) + 6) #Lines of "#" meant to be over and under text.
    z = '#' #The lines in "y".
    print('\n' + '\n') #Spacing between writing the header and printing the result.

    print(z * y + '\n' + z + (' ' * (y-2)) + z) #Upper line and two # at next.

    print('#  ' + x + '  #') #Text/header.

    print(z + (' ' * (y-2)) + z +'\n' + z * y) #Two # and then lower line.

#####################
#  Default headers  #
#####################

def header():
    x = 0
    print('Enter header text:')
    x = input()
    y = (len(x) + 6) #Lines of "#" meant to be over and under text.
    z = '#' #The lines in "y".
    print('\n' + '\n') #Spacing between writing the header and printing the result.

    print(z * y) #Upper line.
    print('#  ' + x + '  #') #Text/header.
    print(z * y) #Lower line.


###########################
#  Simple Header Printer  #
###########################

def SHP():
    b = 0
    print('Welcome to the "Simple Header Printer" (SHP).')
    print('What kind of header? \nbig (b) or default (d)?')
    b = input()
    if b == 'b':
        bigHeader()
    elif b == 'd':
        header()
    else:
        print('Try again (b/d):')
        b = input()
    repeatFunc()


###############
#  Go again?  #
###############

def repeatFunc():
    print(('\n' * 2) + 'Go again: (y/n)')
    a = 0
    a = input()
    if a == 'y':
        SHP()
    elif a == 'n':
        print('Bye.')


################################
#  Running the program/script  #
################################

SHP()
